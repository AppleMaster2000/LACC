-----------------------------------------------------------------------------------------
--
-- main.lua
--
-----------------------------------------------------------------------------------------

-- Your code here
local widget = require("widget")

local input = native.newTextBox(250,280,480,480)
input.x = display.actualContentWidth/2
input.size = 50
input.isEditable = true
local saveData = system.pathForFile("save.txt", system.DocumentsDirectory)
local read = function(event)
    local file = io.open(saveData, "r")
    if file then
        local content = file:read("*a")
        input.text = content
        io.close(file)
    end
end
local save = function(event)
    local file = io.open(saveData, "w")
    if file then
        file:write(input.text)
        io.close(file)
    end
end

-- save Button
local saveButton = widget.newButton{
    label = "Save",
    shape = "roundedRect",
    fillColor =
    {
        default = {0.5, 0.5, 0.5},
        over = {0.6, 0.6, 0.6},
    },
    labelColor = 
    {
        default = {1, 1, 1},
    },
    fontSize = 30,
    font = native.SystemFont,
    width = 100,
    onRelease = save,
}

saveButton.x = display.actualContentWidth / 2 
saveButton.y = 560

-- load Button
local loadButton = widget.newButton{
    label = "Load",
    shape = "roundedRect",
    fillColor =
    {
        default = {0.5, 0.5, 0.5},
        over = {0.6, 0.6, 0.6},
    },
    labelColor = 
    {
        default = {1, 1, 1},
    },
    fontSize = 30,
    font = native.SystemFont,
    width = 100,
    onRelease = read,
}

loadButton.x = display.actualContentWidth / 4 
loadButton.y = 560