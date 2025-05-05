#location_sizes = {
#    "Overworld": {"sizeX" :  32.800, "sizeY" :  32.857, "frameX" :  8, "frameY" : 16},
#    "Blossom"  : {"sizeX" :  80.375, "sizeY" :  80.375, "frameX" :  7, "frameY" :  9},
#    "Crimson"  : {"sizeX" : 136.417, "sizeY" : 136.800, "frameX" : 16, "frameY" : 14},
#    "Fall"     : {"sizeX" :  59.250, "sizeY" :  58.917, "frameX" :  8, "frameY" :  4},
#    "Forbidden": {"sizeX" :  63.615, "sizeY" :  63.545, "frameX" :  5, "frameY" : 12},
#    "Hills"    : {"sizeX" : 120.700, "sizeY" : 120.400, "frameX" : 16, "frameY" : 17},
#    "Lake"     : {"sizeX" :  77.762, "sizeY" :  77.667, "frameX" :  9, "frameY" : 13},
#    "Pillar"   : {"sizeX" :  88.385, "sizeY" :  88.375, "frameX" :  7, "frameY" :  5},
#    "Swamp"    : {"sizeX" : 100.444, "sizeY" : 100.000, "frameX" :  9, "frameY" : 13},
#    "Temple"   : {"sizeX" : 100.783, "sizeY" : 100.714, "frameX" : 11, "frameY" : 10}
#}

location_sizes = {
    "Overworld": {"sizeX" : 2788 / 85, "sizeY" : 690 / 21, "frameX" :  8, "frameY" : 16},
    "Blossom"  : {"sizeX" : 1286 / 16, "sizeY" : 643 /  8, "frameX" :  7, "frameY" :  9},
    "Crimson"  : {"sizeX" : 2319 / 17, "sizeY" : 684 /  5, "frameX" : 16, "frameY" : 14},
    "Fall"     : {"sizeX" : 1185 / 20, "sizeY" : 707 / 12, "frameX" :  8, "frameY" :  5},
    "Forbidden": {"sizeX" :  827 / 13, "sizeY" : 699 / 11, "frameX" :  6, "frameY" : 12},
    "Hills"    : {"sizeX" : 1207 / 10, "sizeY" : 602 /  5, "frameX" : 16, "frameY" : 17},
    "Lake"     : {"sizeX" : 1633 / 21, "sizeY" : 699 /  9, "frameX" :  7, "frameY" : 13},
    "Pillar"   : {"sizeX" : 1149 / 13, "sizeY" : 707 /  8, "frameX" :  7, "frameY" :  6},
    "Swamp"    : {"sizeX" : 1808 / 18, "sizeY" : 700 /  7, "frameX" : 10, "frameY" : 13},
    "Temple"   : {"sizeX" : 2318 / 23, "sizeY" : 705 /  7, "frameX" : 12, "frameY" : 10}
}

def get_position(locations):
    for location in locations:
        size = location_sizes[location["map"]] # a pixel off every two rooms
        column = location.get("column", 0) # 1-index
        columnOffset = location.get("columnOffset", 0)
        row = location.get("row", 0) # 1-index
        rowOffset = location.get("rowOffset", 0)

        location["x"] = int((size["sizeX"] * (column - 1)) + (size["sizeX"] * 0.5)  + size["frameX"] + columnOffset)
        location["y"] = int((size["sizeY"] * (row - 1)) + (size["sizeY"] * 0.5) + size["frameY"] + rowOffset)
    
    return locations
