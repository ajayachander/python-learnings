
rowDict = {}
colDict = {}

def checkIfDuplicates(listOfElems):
    ''' Check if given list contains any duplicates '''    
    for elem in listOfElems:
        if listOfElems.count(elem) > 1:
            return True
    return False

for x in range(1,10):
    rowDict["row{0}".format(x)] = input("Enter a row of numbers (1-9) : ")
    if len(rowDict["row{0}".format(x)]) > 9:
        print("Longer than 9 digits!")
        break
    try:
        rowDict["row{0}".format(x)] = [int (y) for y in (rowDict["row{0}".format(x)])]
        print(rowDict["row{0}".format(x)])
    except ValueError:
        print ("Invalid value found!")
        break
    result = checkIfDuplicates(rowDict["row{0}".format(x)])
    if result:
        print('Row contains duplicate values!')
        break

for x in range(0,9):
    for y in range(1,10):
        colDict["column{0}".format(y)] = []
        colDict["column{0}".format(y)] = rowDict["row{0}".format(y)][x]

for x in range(1,10)
    result = checkIfDuplicates(colDict["column{0}".format(x)])
    if result:
        print('Column contains duplicate values!')
        break
    
print (rowDict)
print (colDict)
