import json

json_file = "savedObject.json"

with open(json_file, 'r') as f:
    data = f.read()

json_data = json.loads(data)

objects = json_data["objects"]

panels = objects[0]["attributes"]["panelsJSON"]
print("Panels:", panels)

# print(json_data)