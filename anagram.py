def rearrangeStr(inputStr):
    outputStr = ""
    for char in inputStr:
        if char.isalpha():
            outputStr += char
        else:
            continue
    return sorted(outputStr)
        
firstStr = (input("First string : ")).lower()
secondStr = (input("Second string : ")).lower()

firstopStr = rearrangeStr(firstStr)
secondopStr = rearrangeStr(secondStr)

print (firstopStr," : ",secondopStr)

if firstopStr == secondopStr:
    print ("Anagrams.")
else:
    print("Not anagrams.")
