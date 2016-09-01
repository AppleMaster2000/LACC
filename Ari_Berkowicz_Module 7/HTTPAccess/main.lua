-----------------------------------------------------------------------------------------
--
-- main.lua
--
-----------------------------------------------------------------------------------------

-- Your code here
local saveData = system.pathForFile("random_number_DB.txt", system.ResourceDirectory)

local widget = require("widget")

local arr = {}

local read = function(event)
    local file = io.open(saveData, "r")
    for line in file:lines() do
        table.insert (arr, tonumber(line))
    end

    io.close(file)
end

read()

local function networkListener( event )

    if ( event.isError ) then
        print( "Network error!" )
    end
end

-- Access local server over SSL:
local x = 1

local function send(event)
    network.request( "http://localhost:8081?"..tostring(arr[x]), "GET", networkListener )
    x = x + 1
end

local run = widget.newButton{
    label = "Run",
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
    fontSize = 22,
    font = native.SystemFont,
    width = 100,
    onRelease = send,
}

run.x = 300
run.y = 900

