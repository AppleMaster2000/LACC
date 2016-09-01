-----------------------------------------------------------------------------------------
--
-- main.lua
--
-----------------------------------------------------------------------------------------

-- Your code here

local widget = require("widget")

display.setStatusBar( display.DefaultStatusBar )

local input = native.newTextBox(300, 400, 600, 800)
input.fontSize = 30

local saveData = system.pathForFile("random_number_DB.txt", system.ResourceDirectory)

local arr = {}

local read = function(event)
    local file = io.open(saveData, "r")
    for line in file:lines() do
        table.insert (arr, tonumber(line))
        input.text = input.text .. "\n" .. line
    end

    io.close(file)
end

function bubble_sort (given) 
   local a = given 
   local a_length = #a 
   local still_active = true
   local tmp = 0            

   while still_active do 
      still_active = false 
      for i = 1, a_length-1 do 
         if a[i+1]<a[i]       
         then 
            tmp = a[i]   
            a[i] = a[i+1]    
            a[i+1] = tmp  
            still_active = true 
         end
      end 
   end
   return a
end 

local showNewArray = function(event)
    input.text = ""
    for k, line in pairs(bubble_sort(arr)) do
        input.text = input.text .. "\n" .. tostring(line)
    end
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
    onRelease = showNewArray,
}

run.x = 300
run.y = 900

read()
