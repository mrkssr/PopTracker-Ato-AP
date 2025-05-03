import os
import shutil
import json

legend_data_folder = "legend"
transformed_legend_destination_folder = "../pack/locations/legend"

legend = ["Bosses", "Obstacles", "Skills"]

def find_sections_with_refs(type):
    if isinstance(type, dict):
        if "children" in type:
            for idx, subarea in enumerate(type["children"]):
                type["children"][idx] = find_sections_with_refs(subarea)
        elif "sections" in type:
            for section in type["sections"]:
                if "ref" in section:
                    object = get_objectname_from_reference(section["ref"])

                    section["name"] = object
        else:
            print(f"What are you? {type}")
    else:
        print(f"Legend type is not a dict: {type}")
    
    return type

def get_objectname_from_reference(ref):
    segments = ref.split("/")
    return segments[-1]

if os.path.exists(transformed_legend_destination_folder) and os.path.isdir(transformed_legend_destination_folder):
    shutil.rmtree(transformed_legend_destination_folder)

os.makedirs(transformed_legend_destination_folder)

for key in legend:
    with open(f'{legend_data_folder}/{key}.json') as file:
        legend_data = json.load(file)

    for idx, type in enumerate(legend_data):
        legend_data[idx] = find_sections_with_refs(type)

    with open(f'{transformed_legend_destination_folder}/{key}.json', 'w') as file:
        json.dump(legend_data, file, indent = 4, sort_keys=False)
