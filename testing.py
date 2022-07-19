import json
import os

with open("testingfile.txt", "r+", encoding="utf-8") as test:
    # filedata = {}
    # lines = test.readlines()
    # for i in lines:
    #     filedata.append(test.read())
    filedata = test.read()
    lines = test.readlines()
    linesdict = {}

    linesdict = {key:value for line in test for key, value in [line.rstrip().split("=", 2)]}
    print(linesdict)
