from json import load, dump

class Defines():
    """
    Class to standardize all defines
    """

    def __init__(self, name='', versions=[], file='', data={}):
        self.name           = name
        self.versions       = versions
        self.file           = file
        self.data           = data

        super().__init__(name, versions, file, data)

    def loadfile(self):
        with open(self.file, "r+") as config:
            FileData = load(config)
            return FileData

    def savefile(self, data):
        with open(self.file, "r+") as config:
            dump(data, config)

class ModList():

    def __init__(self, listname):
        self.NAMETUPLE = dict
        self.listname = {
            str : {
                "ModName"                   : str,
                "PluginName"                : str,
                "Reason"                    : str,
                "ModLink": {
                    "Mode"                  : str,
                    "Game"                  : str,
                    "ModID"                 : int
                },
                "Incompatible Mods": {
                    str: {
                        "PatchLink"         : str,
                        "PluginName"        : str,
                        "Reason"            : str
                    }
                }
            }
        }
        super.__init__(listname)