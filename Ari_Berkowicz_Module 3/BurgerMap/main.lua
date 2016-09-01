-----------------------------------------------------------------------------------------
--
-- main.lua
--
-----------------------------------------------------------------------------------------

-- Your code here

local myMap = native.newMapView(250,500,500,1000)

local function mapmarker(event)
    local opt1 =
    {
        title = "Chick-fil-A",
        subtitle = "Discount in Monday evening",
    }
    myMap:addMarker(34.063327, -118.445130, opt1)
end

if myMap then
    myMap.mapType = "normal"

    timer.performWithDelay(5000,mapmarker)
end