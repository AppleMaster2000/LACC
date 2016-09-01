def attackCaesar():
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    fw = open("ciphertext.txt")
    read = fw.read()
    fw.close()
    text2 = ["" for x in range(len(read))]
    text3 = ""
    distanceShift = 0
    
    alphafloat = [0 for f in range(len(alphabet))]
    letterIndex = 0
    g = True
    while(g):
        for h in range(1, len(alphabet)):
            text3 = ""
            b = 0
            for y in range(1, len(alphabet)):
                alphafloat[y - 1] = float(read.count(alphabet[b])) /len(read) * 100
                if(alphafloat[y] > alphafloat[y - 1]):
                    letterIndex = y
                if(alphafloat[y] < alphafloat[y - 1]):
                    letterIndex = y - 1
                b += 1
            distanceShift = len(alphabet) - letterIndex + h
            
            for x in range(len(read)):
                if(alphabet.index(read[x]) - letterIndex <= len(alphabet) + 1):
                    text2[x] = alphabet[alphabet.index(read[x]) + distanceShift - 25]
                    text3 = text3 + text2[x]
                else:
                    text2[x] = alphabet[alphabet.index(read[x]) + distanceShift]
                    text3 = text3 + text2[x]
            if("the" in text3 or "planet" in text3 or "and" in text3 or "that" in text3):
                print text3.upper()
                break
            g = False
attackCaesar()
