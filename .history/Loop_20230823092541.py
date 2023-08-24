MODE = 0
NUMBER = 0
CYCLE = 0

while CYCLE < 10:
    if MODE == 0 :
        while NUMBER < 10:
            print(NUMBER)
            NUMBER = NUMBER + 1
        print(NUMBER)
        MODE = 1
        CYCLE = CYCLE + 1
    if MODE == 1:
        while NUMBER > 0:
            NUMBER = NUMBER - 1
            print(NUMBER)
        local Screen = GetPartFromPort(1, 'Screen') -- assigning the screen on port 1 to a variable
        local Modem = GetPartFromPort(2, 'Modem')
        Screen:ClearElements()
        Modem:PostRequest(56,'BloxBurg')
        local Chat = Modem:GetRequest(56)
        
        local TextLabel = Screen:CreateElement('TextLabel', {
            AnchorPoint = Vector2.new(0.5, 0.5);
            Position = UDim2.fromScale(0.5, 0.5);
            Size = UDim2.fromScale(1, 1);
            Text = 'Hello, world!';
            TextSize = 20;
            TextScaled = false;
        })
        
        local function Ezpz(text)
        TextLabel:ChangeProperties({ -- change the text and size
            Text = Chat,
            TextSize = 25
        })
        end
        
