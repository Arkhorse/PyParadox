import os
from datetime import datetime
import pytz

from json import load, dump
from json import loads, dumps

def HandleTimeCalls(timeformat="%d/%d/%Y %H:%M:%S", region=None):
    
    if region == None:
        now = datetime.now()
        current_time = now.strftime(timeformat)
        return current_time
    else:
        RegionParsed = pytz.timezone(region)
        current_time = datetime.now(RegionParsed)
        return current_time

print(HandleTimeCalls())

class ConfigHandler():

    def __init__(self, data, defaultdata, config, resourcepaths, debug, jsonargs):
        self.data               = {}
        self.defaultdata        = {
            "debug"             : False,
            "patchname"         : ""
        }
        self.config             = "config.json"
        self.resourcepaths      = "./resources"
        self.debug              = False
        self.jsonargs           = 'self.config, "w+", seperators=(",", ":"), indent=4, sort_keys=True'

        super().__init__(data, defaultdata, config, resourcepaths, debug, jsonargs)

    def ConfigCreate(self):
        if os.path.exists(self.resourcepaths + self.config):
            print("File Exists, Skipping")
        else:
            os.makedirs(self.resourcepaths)
            os.chdir(self.resourcepaths)
            with open(self.config, "w+") as config:
                config.write(f"Created Config at {datetime}")

    def ConfigUpdate(self, key, value, jsonArgs='self.config, "w+", seperators=(",", ":"), indent=4, sort_keys=True'):
        """
        Updates any value based on the key value pair.\n
        `key`         = The key of the setting you want to update\n
        `value`       = What value you want to change it to\n
        `jsonargs`    = Extra arguements when loading the json file. You shouldnt need to change this\n
        Example::\n
            ConfigHandler.ConfigUpdate(key='debug', value=True)
            ConfigHandler.ConfigUpdate(key=')
        """
        with open(self.config, 'r+', jsonArgs) as config:
            data = load(config)
            data[key] = value
            config.seek(0)
            dump(data, config)
            config.truncate()

    def ConfigFetch(self, fetch):
        with open(self.config, "w+", self.jsonargs) as config:
            data = load(config)
            for key, value in data:
                if key == fetch:
                    return value
