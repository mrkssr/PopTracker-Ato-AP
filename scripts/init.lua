ENABLE_DEBUG_LOG = true

local variant = Tracker.ActiveVariantUID

-- Utils
ScriptHost:LoadScript("scripts/utils.lua")

-- Items
ScriptHost:LoadScript("scripts/items_import.lua")

-- Logic
ScriptHost:LoadScript("scripts/logic/logic_helper.lua")
ScriptHost:LoadScript("scripts/logic/logic_main.lua")
ScriptHost:LoadScript("scripts/logic/logic_access.lua")
ScriptHost:LoadScript("scripts/logic/logic_visible.lua")
ScriptHost:LoadScript("scripts/logic_import.lua")

-- Maps
if Tracker.ActiveVariantUID == "maps-u" then
    Tracker:AddMaps("maps/maps-u.json")  
else
    Tracker:AddMaps("maps/maps.json")  
end  

if PopVersion and PopVersion >= "0.23.0" then
    Tracker:AddLocations("locations/dungeons.json")
end

-- Layout
ScriptHost:LoadScript("scripts/layouts_import.lua")

-- Locations
ScriptHost:LoadScript("scripts/locations_import.lua")

-- AutoTracking for Poptracker
if PopVersion and PopVersion >= "0.18.0" then
    ScriptHost:LoadScript("scripts/autotracking.lua")
end