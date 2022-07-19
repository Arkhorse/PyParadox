import json
import re
import os

"""
PYParadox is a module to handle Paradox code in order to add, remove and alter data in text files formated akin to json format
"""

_FILE_ = "01_pop_assembly_buildings.txt"
stellaris = {
    'buildings': "common/buildings"
}

def decode(data):

    # initial code handling to make paradox code into proper json format

    data = re.sub(r'#.*', '', data)                                                                                 # Remove comments
    data = re.sub(
            r'(?<=^[^\"\n])*(?<=[0-9\.\-a-zA-Z])+(\s)(?=[0-9\.\-a-zA-Z])+(?=[^\"\n]*$)',
            '\n',
            data,
            flags=re.MULTILINE
        )                                                                                                           # One Line Lists
    data = re.sub(r'[\t ]', '', data)                                                                               # remove whitespace

    #region Definitions replace variables with values
    definitions = re.findall(r'(@\w+)=(.+)', data)

    if definitions:
        for definition in definitions:
            data = re.sub(r'^@.+', '', data, flags=re.MULTILINE)
            data = re.sub(definition[0], definition[1], data)
    #endregion
    
    data = re.sub(r'([\w\d_])[\t\ ]+([_\w\d])', r'\1\n\2', data)                                                    # add newline between key = value key = value
    data = re.sub(r'\n{2,}', '\n', data)                                                                            # Remove excessive new lines
    data = re.sub(r'\n', '', data, count=1)                                                                         # Remove the first new line
    data = re.sub(r'{(?=\w)', '{\n', data)                                                                          # reformat one-liners
    data = re.sub(r'(?<=\w)}', '\n}', data)                                                                         # reformat one-liners
    data = re.sub(r'^([\w-]+)', r'"\g<1>"', data, flags=re.MULTILINE)                                               # Add quotes around keys
    data = re.sub(r'([^><])=', r'\1:', data)                                                                        # Replace = with : but not >= or <=
    data = re.sub(r'(?<=:)@?\w*[a-zA-Z_]+\w*', r'"\g<0>"', data)                                                    # Add quotes around string values or @variables
    data = re.sub(r':"yes"', ':true', data)                                                                         # Replace yes with true
    data = re.sub(r':"no"', ':false', data)                                                                         # Replace no with false
    data = re.sub(r'([<>]=?)(.+)', r':{"value":\g<2>,"operand":"\g<1>"}', data)                                     # Handle < > >= <=
    data = re.sub(r'(?<![:{])\n(?!}|$)', ',', data)                                                                 # Add commas
    data = re.sub(r':{([^}{:]*)}', r':[\1]', data)                                                                  # if there's no : between list elements need to replace {} with []

    data = '{' + data + '}'                                                                                         # Add start and finish brackets to finish JSON conversion

    return json.loads(data)

def encode(data):
    data = json.dumps(data, indent=4)
    data = data[2:-2]
    data = data.replace('"', '').replace(':', ' =').replace(',', '')
    data = re.sub(r'\n{2,}', '\n', data)                                                                            # Remove excessive new lines
    data = re.sub(r'\n', '', data, count=1)                                                                         # Remove the first new line
    
    #region Revert decode() changes. These are not acceptable in paradox code
    """TODO
        Revert Operator changes at line 39 
            data = re.sub(r'([<>]=?)(.+)', r':{"value":\g<2>,"operand":"\g<1>"}', data)
        Revert quotations where necassary
    """
    data = re.sub(r'\[', r'{', data)
    data = re.sub(r'\]', r'}', data)
    
    #endregion

    return data

def writefile(file, text):
    
    with open(file, 'w+', encoding='utf-8') as A:
        TEXT = encode(text)
        A.write(TEXT)

def readfile(file):
    
    with open(file, 'r+', encoding='utf-8') as A:
        data = A.read()
        DATA = decode(data)
        
    return DATA

def readlocalisationfile(file):
    import yaml
    with open(file, 'r', encoding='utf-8-sig') as A:
        data = A.read()
        DATA = yaml.safe_load(data)
        
    return DATA

def buildingsorting(file, path, category=str|'current', number=int):
    """Adds sorting to all building files in the given folder
        \n\tArguements::
            \tfile          : This is the file you want to add the position sorting to
            \tpath          : This is where the above file is at. 
            \tcategory      : This will allow you to limit your alterations based on what category the building has. Also used to define what position priority that building is
            \tnumber        : This is for testing only. If you see this please download a live version
        \n\tExamples::
            \t  buildingsorting(file='01_pop_assemble_buildings.txt', path='O:/SteamLibrary/steamapps/common/Stellaris/common/buildings', category='pop_assembly', number=100)
    """
            
    # Handle all possible invalid calls
    if category == None or number == None:
        return print("Required arguments are not filled out")
    if type(number) is not int:
        return print(f"Arguement number is not an integer. Given arguement: {number}")
    if file == None:
        return print("File is not specified")
    if path == None:
        return print("Path is not specified")
    
    cat = str(category)
    num = int(number)
    if path == 'current':
        path = os.getcwd()
    os.chdir(path)
    with open(file, 'w+', encoding='utf-8') as A:
        data = A.read()
        parsed = decode(data)
        if parsed['category'] == cat:
            parsed['position_priority'] = int(num)
        else:
            print(f'The requested category, {cat} is not present in the given file {file}, in path {path}')

def UnitTest():
    building_test_pop_assembly = ''' 
    building_AI_POPS = {
        base_buildtime = @b1_time
        base_cap_amount = 1
        category = pop_assembly
    }
    '''
    building_test_event = """
    building_AI_EVENT = {
        base_buildtime = @b1_time
        base_cap_amount = 1
        category = event
    }
    """

class Operators(name=str, value=int):
    pass

class ParadoxOperators(Operators):
    
    def GreaterThan(self, name, value):
        text = "{} > {}".format(name, value)
        return text
        
    def LessThan(self, name, value):
        text = "{} < {}".format(name, value)
        return text
    
    def GreaterThanEqual(self, name, value):
        text = "{} >= {}".format(name, value)
        return text
    
    def LessThanEqual(self, name, value):
        text = "{} <= {}".format(name, value)
        return text


# with open(_FILE_, 'r+', encoding='utf-8') as file:
#     _DATA_ = file.read()

    
# data = decode(_DATA_)
# # datakey = data.keys()

# for key in data:
#     print(key)
#     for key, value in key:
#         if key == 'category':
#             if value == 'pop_assembly':
#                 data[key]['position_priority'] = 100
#             else:
#                 print(f'Value not found, {value}')
    
#     text = encode(data)
    
# outputfile = "outputfile.txt"

# with open(outputfile, "w+", encoding='utf-8') as output:
#     output.write(text)


# print(text)
# outputfile = "outputfile.txt"

