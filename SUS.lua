-- * Adjustable values

local MAX = 69420

-- ! Danger Zone, only change if you know what you are doing!

local Limit = 10000    -- Default: 10000
local WarnLimit = 5000 -- Default: 5000
local SafeMode = true  -- Default: true
local MaxBits = 5000   -- Default: 5000

-- ! Code, do not touch unless you know what you are doing!

local COUNTER = 0
local BITS = 0
if SafeMode == true then
    if MAX > Limit then
        while BITS < MaxBits do
            print("ERROR! Limit exceeded, setting to " .. Limit .. ". Bits: " .. BITS .. " / " .. MaxBits)
            MAX = Limit
            BITS = BITS + 1
        end
    elseif MAX > WarnLimit then
        while BITS < MaxBits do
            print("WARNING! Unsafe Numbers Reached! (" .. MAX .. " / " .. WarnLimit ..
                ") Bits: " .. BITS .. " / " .. MaxBits)
            BITS = BITS + 1
        end
    else
        while BITS < MaxBits do
            print("Safe Numbers!" .. " Bits: " .. BITS .. " / " .. MaxBits)
            BITS = BITS + 1
        end
    end
else
    while BITS < MaxBits do
        print("WARNING!!! SAFE MODE OFF!")
        BITS = BITS + 1
    end
end

while COUNTER < MAX do
    print("Amount: " .. COUNTER .. " / " .. MAX)
    COUNTER = COUNTER + 1
end
print("Amount: " .. MAX .. " (max)")
