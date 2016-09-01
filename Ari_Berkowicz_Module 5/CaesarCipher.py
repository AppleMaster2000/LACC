def caesarCipher(text, distanceShift):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    text = text.lower()
    text = text.replace(" ", "")
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("!", "")
    text = text.replace("-", "")
    text = text.replace(":", "")
    text = text.replace(";", "")
    text2 = ["" for x in range(len(text))]
    text3 = ""
    for x in range(len(text)):
        if(alphabet.index(text[x]) + distanceShift >= len(alphabet)):
            text2[x] = alphabet[alphabet.index(text[x])  + distanceShift - 25]
            text3 = text3 + text2[x]
        else:
            text2[x] = alphabet[alphabet.index(text[x]) + distanceShift]
            text3 = text3 + text2[x]
    print text3.upper()
caesarCipher("Hello Kevin", 10)
