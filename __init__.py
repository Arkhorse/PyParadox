import os
from typing import NamedTuple

class ModuleVersionInfo(NamedTuple):
    major: int
    minor: int
    micro: float
    serial: int
    releaseLevel: str

    @property
    def __version__(self):
        versionParts = "{}: {}.{}.{}".format(
            self.releaseLevel,
            self.major,
            self.minor,
            self.micro)

        return versionParts

try:
    from .Resources import *
except ImportError:
    os.makedirs("Resources")
    from .Resources import *

try:
    from Sorting import *
except ImportError:
    print("Fatal Error: Module is not found")
