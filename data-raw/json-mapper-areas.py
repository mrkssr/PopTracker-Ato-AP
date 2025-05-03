import os
import shutil
import json

types_data_folder = "types"
areas_data_folder = "areas"
transformed_areas_destination_folder = "../pack/locations/areas"

def replace_references(area, type):
    return find_refs(area, type)

def find_refs(area, type):
    if isinstance(area, dict):
        if "ref" in area:
            #print(f'area["ref"]: {type} -> {area["ref"].lower()}')
            if area["ref"].lower().startswith(f'{type}/'):
                area = get_type_object(area["ref"], type)
        else:
            for key, value in area.items():
                area[key] = find_refs(value, type)
    elif isinstance(area, list):
        for idx, item in enumerate(area):
            area[idx] = find_refs(item, type)
    
    return area

def get_type_object(ref, type):
    segments = ref.split("/")
    category = segments[0]
    objectName = segments[1]
    typeData = types[type][0]

    for section in typeData["sections"]:
        if section["name"] == objectName:
            return_section = section

            for key, value in typeData.items():
                if key not in ('name', 'sections'):
                    return_section[key] = value

            return_section["_category"] = category

            return return_section

    print(f"### No Object Found for {objectName} in {category} ###")
    return None

types = {
    "bosses" : None,
    "checkpoints" : None,
    "coins" : None,
    "magic_bars" : None,
    "runes" : None,
    "shards" : None,
    "skills" : None,
    "talismans" : None
}

areas = {
    "Blossom": None,
    "Crimson": None,
    "Fall": None,
    "Forbidden": None,
    "Hills": None,
    "Lake": None,
    "Pillar": None,
    "Swamp": None,
    "Temple": None,
}

for key in types:
    with open(f'{types_data_folder}/{key}.json') as file:
        types[key] = json.load(file)

for key in areas:
    with open(f'{areas_data_folder}/{key}.json') as file:
        areas[key] = json.load(file)

for area, areaData in areas.items():
    for type, typeData in types.items():
        areas[area] = replace_references(areaData, type)

if os.path.exists(transformed_areas_destination_folder) and os.path.isdir(transformed_areas_destination_folder):
    shutil.rmtree(transformed_areas_destination_folder)

os.makedirs(transformed_areas_destination_folder)

for key, value in areas.items():
    with open(f'{transformed_areas_destination_folder}/{key}.json', 'w') as file:
        json.dump(value, file, indent = 4, sort_keys=False)