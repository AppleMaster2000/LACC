-----------------------------------------------------------------------------------------
--
-- main.lua
--
-----------------------------------------------------------------------------------------

-- Your code here

local captureText = display.newText("You captured a pokemon!", display.actualContentWidth / 2, 750, native.systemFont, 32)
captureText.alpha = 0

local test1 = display.newText("", display.actualContentWidth / 2, 800, native.systemFont, 32)
local titleName = ""
local myMap = native.newMapView(display.actualContentWidth / 2,300, display.actualContentWidth, display.actualContentHeight / 1.5)

local randomNumber = math.random(1,150)
local markerID = ""

local distanceText =  display.newText("", display.actualContentWidth / 2, 900, native.systemFont, 32)

local currentLocation = myMap:getUserLocation()

local opt1 =
    {
        title = titleName,
        subtitle = "Ackerman Union",
		imageFile = imageName,
		latitude = 34.070383,
		longitude = -118.444225
    }

local pokeCaptureSound = audio.loadSound("pokemonCaught.mp3")
pokeNames = {
	"001. Bulbasaur", "002. Ivysaur", "003. Venusaur", "004. Charmander", "005. Charmeleon", "006. Charizard", "007. Squirtle", "008. Wartortle", "009. Blastoise", "010. Caterpie", 
	"011. Metapod", "012. Butterfree", "013. Weedle", "014. Kakuna", "015. Beedrill", "016. Pidgey", "017. Pidgeotto", "018. Pidgeot", "019. Rattata", "020. Raticate", 
	"021. Spearow", "022. Fearow", "023. Ekans", "024. Arbok", "025. Pikachu", "026. Raichu", "027. Sandshrew", "028. Sandslash", "029. Nidoran (female)", "030. Nidorina", 
	"031. Nidoqueen", "032. Nidoran (male)", "033. Nidorino", "034. Nidoking", "035. Clefairy", "036. Clefable", "037. Vulpix", "038. Ninetales", "039. Jigglypuff", "040. Wigglytuff", 
	"041. Zubat", "042. Golbat", "043. Oddish", "044. Gloom", "045. Vileplume", "046. Paras", "047. Parasect", "048. Venonat", "049. Venomoth", "050. Diglett", 
	"051. Dugtrio", "052. Meowth", "053. Persian", "054. Psyduck", "055. Golduck", "056. Mankey", "057. Primeape", "058. Growlithe", "059. Arcanine", "060. Poliwag", 
	"061. Poliwhirl", "062. Poliwrath", "063. Abra", "064. Kadabra", "065. Alakazam", "066. Machop", "067. Machoke", "068. Machamp", "069. Bellsprout", "070. Weepinbell", 
	"071. Victreebel", "072. Tentacool", "073. Tentacruel", "074. Geodude", "075. Graveler", "076. Golem", "077. Ponyta", "078. Rapidash", "079. Slowpoke", "080. Slowbro", 
	"081. Magnemite", "082. Magneton", "083. Farfetch&#039;d", "084. Doduo", "085. Dodrio", "086. Seel", "087. Dewgong", "088. Grimer", "089. Muk", "090. Shellder", 
	"091. Cloyster", "092. Gastly", "093. Haunter", "094. Gengar", "095. Onix", "096. Drowzee", "097. Hypno", "098. Krabby", "099. Kingler", "100. Voltorb", 
	"101. Electrode", "102. Exeggcute", "103. Exeggutor", "104. Cubone", "105. Marowak", "106. Hitmonlee", "107. Hitmonchan", "108. Lickitung", "109. Koffing", "110. Weezing", 
	"111. Rhyhorn", "112. Rhydon", "113. Chansey", "114. Tangela", "115. Kangaskhan", "116. Horsea", "117. Seadra", "118. Goldeen", "119. Seaking", "120. Staryu", 
	"121. Starmie", "122. Mr. Mime", "123. Scyther", "124. Jynx", "125. Electabuzz", "126. Magmar", "127. Pinsir", "128. Tauros", "129. Magikarp", "130. Gyarados", 
	"131. Lapras", "132. Ditto", "133. Eevee", "134. Vaporeon", "135. Jolteon", "136. Flareon", "137. Porygon", "138. Omanyte", "139. Omastar", "140. Kabuto", 
	"141. Kabutops", "142. Aerodactyl", "143. Snorlax", "144. Articuno", "145. Zapdos", "146. Moltres", "147. Dratini", "148. Dragonair", "149. Dragonite", "150. Mewtwo", 
}

local function addmarker(event)
	local imageName = "d"
	if randomNumber < 100 and randomNumber > 9 then
		imageName = imageName .. "0" .. tostring(randomNumber) .. ".png"
		titleName = string.sub(pokeNames[randomNumber], 6)
	elseif randomNumber < 10 then
		imageName = imageName .. "00" .. tostring(randomNumber) .. ".png"
		titleName = string.sub(pokeNames[randomNumber], 6)
	elseif randomNumber > 99 and randomNumber < 151 then
		imageName = imageName .. tostring(randomNumber) .. ".png"
		titleName = string.sub(pokeNames[randomNumber], 6)
	end

	markerID = myMap:addMarker(opt1.latitude, opt1.longitude, opt1)
end

local removeMarker = function(event)
	myMap:removeAllMarkers()
end

if myMap then
    myMap.mapType = "normal"
end

local hideWord = function(event)
	captureText.alpha = 0
end

-- Calculate distance
local function distance(from, to)
	local distance = 0
	local radius = 6367000
	local radian = math.pi / 180
	local deltaLatitude = math.sin(radian * (from.latitude - to.latitude) /2)
	local deltaLongitude = math.sin(radian * (from.longitude - to.longitude) / 2)

	local circleDistance = 2 * math.asin(math.min(1, math.sqrt(deltaLatitude * deltaLatitude + math.cos(radian * from.latitude) * math.cos(radian * to.latitude) * deltaLongitude * deltaLongitude)))
	distance = math.abs(radius * circleDistance)
	return distance
end

local onAcceleterate = function(event)
	--test1.text = tostring(randomNumber)
	test1.text = titleName
	userLoc = user
	if markerID == "" then
		timer.performWithDelay(1000,addmarker)
	else
        if event.isShake then
			captureText.alpha = 1
			audio.play(pokeCaptureSound)
			if myMap then
				timer.performWithDelay(200, removeMarker)
			end
            timer.performWithDelay(500, hideWord)
		timer.performWithDelay(1000,addmarker)
		randomNumber = math.random(1,150)
		end
	end
end

local frameUpdates = function (event)
	distanceText.text = distance(currentLocation, opt1)
end

system.setAccelerometerInterval(60)

Runtime:addEventListener("accelerometer", onAcceleterate)
Runtime.addEventListener("enterFrame", frameUpdates)