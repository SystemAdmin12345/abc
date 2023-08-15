local reactor = GetPartFromPort(1, "Reactor")
local dispenser = GetPartFromPort(2, "Dispenser")

while wait() do
    local fuel = reactor:GetFuel()
    for i = 1, #fuel do
        if fuel[i] <= 0 then
            dispenser:Trigger()
            wait(1)
            dispenser:Trigger()
        end
    end
end
