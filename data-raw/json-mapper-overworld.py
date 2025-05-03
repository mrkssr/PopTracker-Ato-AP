import os
import shutil
import json

overworld_data_folder = "locations/overworld"
transformed_overworld_destination_folder = "../pack/locations/overworld"

overworld = ["Blossom", "Crimson", "Fall", "Forbidden", "Hills", "Lake", "Pillar", "Swamp", "Temple"]

def find_sections_with_refs(overworld_region):
    if isinstance(overworld_region, dict):
        if "children" in overworld_region:
            for idx, subarea in enumerate(overworld_region["children"]):
                overworld_region["children"][idx] = find_sections_with_refs(subarea)
        elif "sections" in overworld_region:
            for section in overworld_region["sections"]:
                if "ref" in section:
                    if section["ref"]:
                        room, object = get_room_and_objectname_from_reference(section["ref"])

                        overworld_region["name"] = room
                        section["name"] = object
        else:
            print(f"what are you? {overworld_region}")
    else:
        print(f"overworld region is not a dict: {overworld_region}")
    
    return overworld_region

def get_room_and_objectname_from_reference(ref):
    segments = ref.split("/")
    return segments[-2], segments[-1]
    
if os.path.exists(transformed_overworld_destination_folder) and os.path.isdir(transformed_overworld_destination_folder):
    shutil.rmtree(transformed_overworld_destination_folder)

os.makedirs(transformed_overworld_destination_folder)

for key in overworld:
    with open(f'{overworld_data_folder}/{key}.json') as file:
        overworld_data = json.load(file)

    for idx, overworld_region in enumerate(overworld_data):
        overworld_data[idx] = find_sections_with_refs(overworld_region)

    with open(f'{transformed_overworld_destination_folder}/{key}.json', 'w') as file:
        json.dump(overworld_data, file, indent = 4, sort_keys=False)
