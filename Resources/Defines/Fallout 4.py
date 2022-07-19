"""
Defines for the Fallout 4 game
"""

from json import load, dump
from unicodedata import name

from Defines import Defines

class Fallout4(Defines):
    
    def __init__(self):
        self.name               = ""
        self.file               = ""
        self.versions           = [
            "Fallout 4": "",
            "Buffout 4": "1.24.0"
        ]
    
    def F4SEMODS(self):
        f4semods = {
             "SSW": {
                "ModName": "Survival Stats Widget",
                "PluginName": "SSW.dll",
                "Reason": "Incompatible with XDI. Causes dialogue lockups when used with XDI",
                "ModLink": {
                    "Game": "fallout4",
                    "ModID": 38067
                },
                "Incompatible Mods": {
                    "XDI": {}
                }
            },
            "XDI": {
                "ModName": "Extended Dialogue Interface",
                "PluginName": "XDI.dll",
                "Reason": "Incompatible with SSW and can have issues with some quest mods",
                "ModLink": {
                    "Mode": str,
                    "Game": "fallout4",
                    "ModID": int
                },
                "Incompatible Mods": {
                    "SSW": {
                        "PatchLink": None
                    },
                    "SS2": {
                        "PatchLink": "{}",
                        "PatchPluginName": ""
                    }
                }
            }
        }
        return f4semods

