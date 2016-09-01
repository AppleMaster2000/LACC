-----------------------------------------------------------------------------------------
--
-- main.lua
--
-----------------------------------------------------------------------------------------

-- Your code here
local widget = require("widget")

display.setStatusBar( display.DefaultStatusBar )

local input1 = native.newTextField(370, 450, 230, 40)
local input2 = native.newTextField(370, 550, 230, 40)

local flatRect = display.newRect(250, 640 , 480, 5)

local textAnswer = display.newText("???", 450, 40, native.systemFont, 32)

textAnswer.x = 370
textAnswer.y = 700

local addHandler = function(event)
    if input2.text == "" and input1.text == "" then
	  input2.text = "1"
      input1.text = "1"
    end

    textAnswer.text = input1.text + input2.text
end

local subHandler = function(event)
    if input2.text == "" and input1.text == "" then
	  input2.text = "1"
      input1.text = "1"
    end
    textAnswer.text = input1.text - input2.text
end

local mulHandler = function(event)
    if input2.text == "" and input1.text == "" then
	  input2.text = "1"
      input1.text = "1"
    end
    textAnswer.text = input1.text * input2.text
end

local devHandler = function(event)
    if input2.text == "" and input1.text == "" then
	  input2.text = "1"
      input1.text = "1"
    end
    textAnswer.text = input1.text / input2.text
end

--button1

local button1 = widget.newButton{
    label = "+",
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
    width = 45,
    onRelease = addHandler,
}

button1.x = 30
button1.y = 560

--button2

local button2 = widget.newButton{
    label = "-",
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
    width = 45,
    onRelease = subHandler,
}

button2.x = 80
button2.y = 560

--button3

local button3 = widget.newButton{
    label = "*",
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
    width = 45,
    onRelease = mulHandler,
}

button3.x =  130
button3.y = 560

--button4

local button4 = widget.newButton{
    label = "/",
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
    width = 45,
    onRelease = devHandler,
}

button4.x =  180
button4.y = 560