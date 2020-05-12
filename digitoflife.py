inputStr = input("Enter birthday in YYYYMMDD : ")

intList = [int (x) for x in inputStr]

while len(intList) > 1:
    dolTotal = 0
    for x in intList:
        dolTotal += x
    dolTotalStr = str(dolTotal)
    intList = [int (y) for y in dolTotalStr]

print (dolTotal)
    