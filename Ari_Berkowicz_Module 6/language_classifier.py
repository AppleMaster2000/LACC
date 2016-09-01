#-*- coding: utf-8 -*-
#!/usr/bin/python2.6

# Language classifier miniproject for machine learning module
# LACC 2016
#*************************************
# This is where you write your code
#
# train(training_set)
#
# Loads a language training set from a text file
#
# input: name of the training set (for example, "french.txt")
# output: dictionary containing word/frequency pairs 
# 
# Note: You can open a file using open("filename.txt")
# 
# You can get a list containing each line with file.readlines()
#
# You'll need to grab each word from each line, and add 1 to the 
# frequency of that word in your dictionary. Try to strip out symbols.
#
# You can learn more about Python dictionaries online: http://www.tutorialspoint.com/python/python_dictionary.htm
#*************************************
def replaceStuff(text):
	text = text.replace(".", "")
	text = text.replace("?", "")
	text = text.replace(",", "")
	text = text.replace("!", "")
	text = text.replace("-", "")
	text = text.replace(":", "")
	text = text.replace(";", "")
	text = text.replace("\n", " ")
	text = text.lower()
	return text

def train(training_set):
	languageDict = dict()
	languageFile = open(training_set)
	text = languageFile.read()
	languageFile.close()
    
	text = replaceStuff(text)
	wordset = text.split(" ")
	
	for value in range(len(wordset)):
		if(wordset[value] not in languageDict):
			languageDict[wordset[value]] = wordset.count(wordset[value])
	return languageDict

#*************************************
# This is where you write your code
#
# classify(language1, language2, phrase)
#
# Classifies a phrase as being from language1 or language2 
#
# input: the language dictionaries for language1 and language2 
# and the phrase to be classified
# output: 0/1 for which of the two languages 
# 
# You should use a naive Bayes classifier. Break up the phrase 
# to be classified into separate words, and compute the probability
# of each word to be from the French language (with the help of the 
# dictionaries). Use the formula:
# P(word|French) = (# of copies of word in French training set + 1) 
#					/ (# of words in training set + 1)
# The overall probability of the phrase is the product of all the 
# word probabilities (because of the naive independence assumption)
#
# Compute a probability for French and one for Spanish
# The larger is the one we classify to
#*************************************
def classify(language1, language2, phrase):
	frenchDict = language1
	spanishDict = language2
	
	text = phrase
	text = replaceStuff(text)
    
	wordset = text.split(" ")
	frenchProb = 1
	spanishProb = 1
	for x in range(len(wordset)):
		if(wordset[x] in frenchDict):
			frenchProb *= float((frenchDict[wordset[x]] + 1)) / (len(frenchDict) + 1)
		else:
			frenchProb *= 1/float((len(frenchDict) + 1))
		if(wordset[x] in spanishDict):
			spanishProb *= float((spanishDict[wordset[x]] + 1)) / (len(spanishDict) + 1)
		else:
			spanishProb *= 1/ float((len(spanishDict) + 1))
	if(frenchProb < spanishProb):
		return "Spanish"
	if(spanishProb < frenchProb):
		return "French"
print classify(train("french.txt"),train("spanish.txt"), "Faut-il aller au restaurant aujourd'hui?")
