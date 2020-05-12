codeInput = input("Enter the code : ")

while True:
    try:    
        valInput = int(input("Enter the cipher shift value (between 1...25): "))
        if (valInput < 1) or (valInput > 25):
            print("Enter valid cipher shift value!")
        else:
            break
    except ValueError:
        print("Invalid Value!")

codeOutput = ""

for inChar in codeInput:
    outChar = inChar
    if inChar.isalpha():
        outChar = chr(ord(inChar)+valInput)
        if inChar.isupper():
            if ord(outChar) > ord('Z'):
                outChar = chr((ord(inChar) - 26)+valInput)
        if inChar.islower():
            if ord(outChar) > ord('z'):
                outChar = chr((ord(inChar) - 26)+valInput)
    codeOutput += outChar
    
print (codeOutput)

