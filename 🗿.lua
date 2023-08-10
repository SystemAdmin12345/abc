-- * Dictionary
local dict = {
    ["moai"] = "🗿"
}
-- * Safe
for k, v in pairs(dict) do
    print(k, v)
end
-- ! Unsafe
while true do
    print(dict["moai"])
end