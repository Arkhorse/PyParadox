import os
import sys
import re
# from fnmatch import fnmatch as FNM
import fnmatch
# import pyparsing as pyp
import time
import threading

# Internal Modules
from Resources.CLI import CommandLine

__VERSION__         = 0.1
__LASTVERSION__     = 0
DEBUG               = False

def ThreadingMain():
    MainThread = threading.Thread(target=Main)

    MainThread.start()
    MainThread.join()

    if CommandLine(['-debug']) or DEBUG:
        with open('process.log', 'w+', encoding="UTF-8") as log:
            log.write('\n' + time.time() + '\t' + 'MainThread has finished processing')

def Main():
    start_time      = time.time()
    if CommandLine(['-debug']) or DEBUG:
        with open('process.log', 'w+', encoding="UTF-8") as log:
            log.write('Log Opened At:' + '\t' + start_time)

def confighandler():
    internalpaths = {
        "path_divider"                      : "/",
        "installpathDEV"                    :"O:/SteamLibrary/steamapps/common/Stellaris",
        "stellaris"                         : {
            "sorting_attrib"                : "position_priority = ",
            "buildings"                     : "/common/buildings",
            "ignoredpatterns"               : [
                "convert_to",
                "has_building",
                "icon",
                "upgrades",
                "text"
            ],
            "sortingindex"                      : {
                "capital"                       : 1,
                "event"                         : 25,
                "pop_assembly"                  : 100,
                "gov"                           : 200,
                "resource"                      : 300,
                "manufactoring"                 : 400,
                "research"                      : 500,
                "trade"                         : 600,
                "amenity"                       : 700,
                "unity"                         : 800,
                "army"                          : 900,
                "deposit"                       : 1000
            }
        }
    }

    return internalpaths

# user_documents = os.path.expanduser('~')
# Local

# for file in str(stellaris_install_path):
#     if ( fnmatch.fnmatch(file, "USERDIR.txt") or fnmatch.fnmatch(file, "userdir.txt") ):
#         data = open(file, "r", encoding="utf-8", errors="ignore")
#         readdata = data.readlines()
#         stellaris_mod_dir = readdata[0].strip()
#         data.close()
#     else:
#         stellaris_mod_dir = user_documents + "/Documents/Paradox Interactive/Stellaris/mod"

# print(f"Stellaris Documents Dir: {stellaris_mod_dir}")

BuildingRootName                    = "building_"
EndofLineParadox                    = "= {"


# sorting_attrib_exists = re.search(r"position_priority/s=/s/d", file)