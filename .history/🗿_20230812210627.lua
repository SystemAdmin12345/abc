-- * Adjustable Values
local SafeMode = false -- Default: true

-- ? Dictionary
local dict = {
    ["moai"] = "🗿"
}
-- Safe
for k, v in pairs(dict) do
    print(k, v)
end
-- ! Unsafe
if SafeMode == false then
while true do
    print(dict["moai"])
end
end