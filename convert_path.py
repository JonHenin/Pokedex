import os
import json

directory = os.fsencode("C:\\Users\\jonat\\Documents\\Masters\\YOLOgpu\\Data\\images\\_Target")
fileList = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        fileList.append(filename)

for jsonFile in fileList:
    # Open and read the file, then convert json to a Python dictionary
    with open(jsonFile, "r") as f:
        jsonData = json.loads(f.read())

    # Edit the Python dictionary
    jsonData["asset"]["path"]={"666": "value6","007": "value13"}

    # Convert Python dictionary to json and write to the file
    with open(jsonFile, "w") as f:
        json.dump(jsonData, f)