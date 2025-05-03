
function A(result)
    if result then
        return AccessibilityLevel.Normal
    else
        return AccessibilityLevel.None
    end
end

function all(...)
    local args = { ... }
    local min = AccessibilityLevel.Normal
    for i, v in ipairs(args) do
        if type(v) == "boolean" then
            v = A(v)
        end
        if v < min then
            if v == AccessibilityLevel.None then
                return AccessibilityLevel.None
            else
                min = v
            end
        end
    end
    return min
end

function any(...)
    local args = { ... }
    local max = AccessibilityLevel.None
    for i, v in ipairs(args) do
        if type(v) == "boolean" then
            v = A(v)
        end
        if tonumber(v) > tonumber(max) then
            if tonumber(v) == AccessibilityLevel.Normal then
                return AccessibilityLevel.Normal
            else
                max = tonumber(v)
            end
        end
    end
    return max
end

function has(item, amount)
    local count = Tracker:ProviderCountForCode(item)
    amount = tonumber(amount)
    if not amount then
        return count > 0
    else
        return count >= amount
    end
end

function not_has(item)
    return not has(item)
end

--function has(item, amount, amountInLogic)
--    local count
--    local amount
--    local amountInLogic

--    if amountInLogic then
--        if count >= amountInLogic then
--            return AccessibilityLevel.Normal
--        elseif count >= amount then
--            return AccessibilityLevel.SequenceBreak
--        else
--            return AccessibilityLevel.None
--        end
--    end
--    if not amount then
--        return count > 0
--    else
--        amount = tonumber(amount)
--        return count >= amount
--    end
--end
            