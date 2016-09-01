def train(training_set, training_set2):
	pixelArray = [[[0 for col in range(20)] for row in range(28)] for num in range(10)]
	imageFile = open(training_set)
	imageText = imageFile.readlines()
	imageFile.close()
	
	imageFile2 = open(training_set2)
	imageText2 = imageFile2.readlines()
	imageFile2.close()
	
	for num in range(len(imageText2)):
		digit = int(imageText2[num])
		for row in range(len(pixelArray[digit])):
			for col in range(len(pixelArray[digit][row])):
				if(" " != imageText[row + len(pixelArray[digit][row]) * num][col]):
					pixelArray[digit][row][col] += 1
	return pixelArray
	
def classify(pixelArray, file):
	imageFile = open(file)
	imageText = imageFile.readlines()
	imageFile.close()
	
	pixelProb = 1
	
	for num in range(len(pixelArray)):
		for row in range(len(pixelArray[num])):
			for col in range(len(pixelArray[num][row])):
				if(imageText[row][col] in pixelArray[num][col]):
					pixelProb *= float((pixelArray[digit][row][col]+ 1)) / (len(pixelArray) + 1)
				else:
					pixelProb *= 1/float((len(pixelArray) + 1))
		
classify(train("trainingimages", "traininglabels"),"testimages")