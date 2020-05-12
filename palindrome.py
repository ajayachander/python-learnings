inputStr = input("Enter the string to check : ")
inputStr = inputStr.upper()
newStr=""
for char in inputStr:
    if char.isalpha():
        newStr += char
    else:
        continue
print(newStr)
lenStr = len(newStr)
print(lenStr)
if lenStr % 2 == 0:
    print ("Even length string")
else:
    print ("Odd length string")
halflenStr = lenStr//2
print (halflenStr)

if (newStr[0:halflenStr] == newStr[-1:halflenStr:-1]):
    print("Palin")
else:
    print("No")

halfnewStr = newStr[0:halflenStr]
print(halfnewStr)    
secondhalfnewStr = newStr[(halflenStr+1):]
print(secondhalfnewStr)    
reverseStr = secondhalfnewStr[::-1]
print (reverseStr)

if halfnewStr == reverseStr:
    print("Palindrome")
else:
    print("Not a palindrome")
