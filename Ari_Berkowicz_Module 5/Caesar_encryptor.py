# This is a caeser encoder with random distance. 
#Everytime you run this python script will give your a different pair of plaintext and ciphertext 
#in plaintext.txt and ciphertext.txt 
import sys, time
import math
import random
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# The caeser encoder
def caesar(plaintext,shift):
	
	dic=dict() #Create our substitution dictionary
	for i in range(0,len(alphabet)):
		dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]
	ciphertext=""
	for j in range(0,len(plaintext)):
		for k in plaintext[j].lower():
			if k in dic:
				k=dic[k]
				ciphertext+=k
	return ciphertext

#Read the original report on kepler_452b
fr = open('original_text.txt','r')
content = fr.readlines()
fr.close()

original_texts = (" ").join(content).replace('\n',' ').lower();
original_texts_length = len(original_texts)

random.seed()
#random select 1000 consequent characters from the original_texts to encode
encode_texts_length = 100
start_ind = random.randint(0,original_texts_length-1 - encode_texts_length)
selected_part = original_texts[start_ind : start_ind + encode_texts_length]
plaintext = ""
for char in selected_part:
	if(char in alphabet):
		plaintext += char
#write the original text to be encoded
fw = open('plaintext.txt','w')
fw.write(plaintext)
fw.close()

#Random generate an encoded distance from 1 to 25
encoded_distance = random.randint(1,25)

#encoded the selected texts
ciphertext = caesar(plaintext,encoded_distance)
#write the cncoded ciphertext to file, which is used to decoded
fw = open('ciphertext.txt','w')
fw.write(ciphertext)
fw.close()
