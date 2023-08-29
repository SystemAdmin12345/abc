local counter = 0
local function wait(value)
    os.execute("sleep "..value)
end

print("Hello")
while counter < 5 do
    counter = counter + 1
    print("Loading.....")
    wait(1)
end
print("Hi")