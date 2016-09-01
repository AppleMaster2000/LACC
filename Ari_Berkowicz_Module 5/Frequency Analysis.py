def numberFrequency(paragraph):
    paragraph = paragraph.lower()
    paragraph = paragraph.replace(" ", "")
    frequencyA = float(paragraph.count("a")) /len(paragraph) * 100
    frequencyE = float(paragraph.count("e")) /len(paragraph) * 100
    frequencyI = float(paragraph.count("i")) /len(paragraph) * 100
    frequencyO = float(paragraph.count("o")) /len(paragraph) * 100
    frequencyV = float(paragraph.count("v")) /len(paragraph) * 100
    frequencyX = float(paragraph.count("x")) /len(paragraph) * 100
    frequencyZ = float(paragraph.count("z")) /len(paragraph) * 100
    numberA = paragraph.count("a")
    numberE = paragraph.count("e")
    numberI = paragraph.count("i")
    numberO = paragraph.count("o")
    numberV = paragraph.count("v")
    numberX = paragraph.count("x")
    numberZ = paragraph.count("z")

    print "The number of a's are " + str(numberA) + " and the frequency is " + str(frequencyA)
    print "The number of e's are " + str(numberE) + " and the frequency is " + str(frequencyE)
    print "The number of i's are " + str(numberI) + " and the frequency is " + str(frequencyI)
    print "The number of o's are " + str(numberO) + " and the frequency is " + str(frequencyO)
    print "The number of v's are " + str(numberV) + " and the frequency is " + str(frequencyV)
    print "The number of x's are " + str(numberX) + " and the frequency is " + str(frequencyX)
    print "The number of z's are " + str(numberZ) + " and the frequency is " + str(frequencyZ)
    print len(paragraph)

numberFrequency("Under the terms of a special appropriation made by the State Legislature in the Spring of 1943, a College of Engineering was established at UCLA in November of 1944. L.M.K. Boelter, the Associate Dean of Engineering at UCBerkeley, was invited to come to Los Angeles and be the founding Dean of the new College.")
