-- * Adjustable Values
local SafeMode = 1 -- Default: 1

-- ? Dictionary
local dict = {
    ["moai"] = "🗿"
}
-- * Safe
for k, v in pairs(dict) do
    print(k, v)
end
-- ! Unsafe
if SafeMode == 0 then
while true do
    print(dict["moai"])
end
end