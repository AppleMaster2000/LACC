-----------------------------------------------------------------------------------------
--
-- main.lua
--
-----------------------------------------------------------------------------------------

-- Your code here
local widget = require("widget")

local input = native.newTextBox(250,display.actualContentHeight / 2,display.actualContentWidth,display.actualContentHeight / 2)
input.height = display.actualContentHeight
input.x = display.actualContentWidth/2
input.size = 50
input.isEditable = true
local saveData = system.pathForFile("save.txt", system.DocumentsDirectory)
local read = function()
    local file = io.open(saveData, "r")
    if file then
        local content = file:read("*a")
        input.text = content
        io.close(file)
    end
end
local save = function()
    local file = io.open(saveData, "w")
    if file then
        file:write(input.text)
        io.close(file)
    end
end

read()

local onAcceleterate = function(event)
    save()
end

system.setAccelerometerInterval(60)

Runtime:addEventListener("accelerometer", onAcceleterate)