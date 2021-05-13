
def testWordCount(userString):
    spaceCount = 1
    for i in range(0,len(userString)):
        if(userString[i] == " "):
            spaceCount += 1
    return spaceCount
