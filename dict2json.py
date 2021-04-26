import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--datalog", type=str,help="Path to dict")
args = parser.parse_args()
    
with open(args.datalog, "r") as f:
    data = f.read().splitlines()

data = data[1:]

info = {}
info["vehicles"] = []

for element in data:
    info["vehicles"].append(eval(element))

with open("new_dataset_json_file.json","w") as infofile:
    json.dump(info, infofile, indent = 2)
    
