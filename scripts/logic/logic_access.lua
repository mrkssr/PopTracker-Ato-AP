-- Skills
function crystal_break()
    return has("crystalbreak")
end

function dodge()
    return has("dodge") or has("dodge_upgrade")
end

function dash()
    return
        has("dash") or
        has("chaindash") or
        has("chaindashupgrade") or
        (double_jump() and armor())
end

function chain_dash()
    return
        dash_state(2) or
        (dash_state(1) and armor())
end

function chain_dash_upgrade()
    return
        (has("dash") and has("chaindash") and has("chaindash_upgrade")) or
        (dash_state(2) and armor())
end

function dash_state(amount)
    return amount <= (
        bool_to_number(has("dash")) +
        bool_to_number(has("chaindash")) +
        bool_to_number(has("chaindash_upgrade"))
    )
end

function double_jump()
    return has("doublejump") or (not_has("doublejump") and armor())
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

function vision()
    return has("vision")
end

function demon_blade()
    return has("demonblade")
end
-- End Skills

-- Shards
function all_shards()
    return has("blue_shard") and has("red_shard") and has("yellow_shard")
end
-- End Shards