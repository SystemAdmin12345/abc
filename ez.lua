local abc = 0
local def = 69

print(abc)

abc = abc + 1

print(abc)

print(def)

abc = 0
print("Activating Loop")
while abc <= 50 do
    if abc > 25 then
        print(abc)
    else
        print("Number hidden until 25")
    end

    abc = abc + 1
end
