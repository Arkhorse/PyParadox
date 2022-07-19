import yaml

def NameListLoad(NameListFile):
    namelistfile = NameListFile
    with open(namelistfile, 'r+') as file:
        NAMELIST = yaml.safe_load(file)

    return NAMELIST

class NameListCreate():

    def __init__(self):
        pass

    def NameListDicts(self):
        self.types = {
            "SEQ"               : "%C%",
            "ORD"               : "%0%",
            "ROM"               : "%R%",
            "ships"             : "_SHIP_",
            "fleets"            : "_FLEET_",
            "planets"           : "_PLANET_",
            "leadernames"       : "_CHR_",
            "class"             : "_CLASS_",
            "RulerNames"        : "_RULER_",
            "armies"            : "_ARMY_"
        }
        self.armies = {
            "primitive"         : "PRIMITIVEARMYxx",
            "industrial"        : "INDUSTRIALARMYxx",
            "postatomic"        : "POSTATOMICARMYxx"
        }

    def createShipName(self, name, species):
        self.species    = species
        self.name       = name
        SHIPNAME        = self.species + self.types["ships"] + self.name
        return SHIPNAME
