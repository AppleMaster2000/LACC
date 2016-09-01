-----------------------------------------------------------------------------------------
--
-- main.lua
--
-----------------------------------------------------------------------------------------

-- Your code here

display.setStatusBar( display.DefaultStatusBar )

local widget = require("widget")

local textGravX =  display.newText("Gravity X:", 450, 40, native.systemFont, 32)

textGravX.x = display.actualContentWidth / 2
textGravX.y = 150

local textGravY =  display.newText("Gravity Y:", 450, 40, native.systemFont, 32)

textGravY.x = display.actualContentWidth / 2
textGravY.y = 300

local textGravZ =  display.newText("Gravity Z:", 450, 40, native.systemFont, 32)

textGravZ.x = display.actualContentWidth / 2
textGravZ.y = 450

local textInstantX =  display.newText("Instant X:", 450, 40, native.systemFont, 32)

textInstantX.x = display.actualContentWidth / 2
textInstantX.y = 600

local textInstantY =  display.newText("Instant Y:", 450, 40, native.systemFont, 32)

textInstantY.x = display.actualContentWidth / 2
textInstantY.y = 750

local textInstantZ =  display.newText("Instant Z:", 450, 40, native.systemFont, 32)

textInstantZ.x = display.actualContentWidth / 2
textInstantZ.y = 900

local onAcceleterate = function(event)
    textGravX.text = "Gravity X:" ..  event.xGravity
    textGravY.text = "Gravity Y:" .. event.yGravity
    textGravZ.text = "Gravity Z:" ..  event.zGravity
    textInstantX.text = "Instant X:" .. event.xInstant
    textInstantY.text = "Instant Y:" .. event.yInstant
    textInstantZ.text = "Instant Z:" .. event.zInstant

end

system.setAccelerometerInterval(60)

Runtime:addEventListener("accelerometer", onAcceleterate)