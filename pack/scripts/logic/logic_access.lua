-- Skills
function crystal_break()
    return has("crystalbreak")
end

function dodge()
    return has("dodge") or has("dodge_upgrade")
end

function dash()
    if (has("dash") or has("chaindash") or has("chaindash_upgrade")) then
        return AccessibilityLevel.Normal
    end
    
    if logic_hard() and (double_jump() and armor()) then
        return AccessibilityLevel.SequenceBreak
    end

    return AccessibilityLevel.None
end

function chain_dash()
    if dash_state(2) then
        return AccessibilityLevel.Normal
    end

    if logic_hard() and ((dash_state(1) and (armor() or double_jump() or spin() or dodge()))) then
        return AccessibilityLevel.SequenceBreak
    end

    return AccessibilityLevel.None
end

function chain_dash_upgrade()
    if dash_state(3) then
        return AccessibilityLevel.Normal
    end

    if logic_hard() and ((dash_state(2) and (armor() or double_jump() or spin() or dodge()))) then
        return AccessibilityLevel.SequenceBreak
    end

    return AccessibilityLevel.None
end

function dash_state(amount)
    return amount <= (
        bool_to_number(has("dash")) +
        bool_to_number(has("chaindash")) +
        bool_to_number(has("chaindash_upgrade"))
    )
end

function double_jump()
    if logic_normal() and has("doublejump") then
        return AccessibilityLevel.Normal
    end
    if logic_hard() and (not_has("doublejump") and armor()) then
        return AccessibilityLevel.SequenceBreak
    end
    
    return AccessibilityLevel.None
end

function speed_charge()
    return has("SpeedCharge")
end

function throw()
    return has("throw") or has("throw_upgrade")
end

function armor()
    return has("armor") or has("armor_upgrade")
end

function spin()
    return has("spin") or has("spin_upgrade")
end

function fatal_draw()
    return has("fatal_draw") or has("fatal_draw_upgrade")
end

function vision()
    if has("vision") then
        return AccessibilityLevel.Normal
    end
    if logic_hard() then
        return AccessibilityLevel.SequenceBreak
    end
    
    return AccessibilityLevel.None
end

function demon_blade()
    return has("demonblade")
end
-- End Skills

-- Logic
function logic_normal()
    -- requires the intended skill set
    -- get from settings
    return true
end

function logic_hard()
    -- every special techs like map jumps, groundpound cancle and so on...
    return not logic_normal()
end
-- End Logic

-- Techs
--function use_slash_boost()
--    return true
--end

--function use_double_slash_boost()
--    return true
--end

--function use_map_jump()
--    return true
--end
-- End Techs

-- Events
function prologue_done()
    return has("prologue_done")
end

function is_prologue()
    return not prologue_done()
end
-- End Events

-- Shards
function all_shards()
    return has("blue_shard") and has("red_shard") and has("yellow_shard")
end
-- End Shards