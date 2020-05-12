rows = []
columns = []
squares = []

totalrows = 9
totalcolumns = 9
totalsquares = 9

def checkIfDuplicates(listOfElems):
    for elem in listOfElems:
        if listOfElems.count(elem) > 1:
            return True
    return False

for x in range(totalrows):
    inputRow = input("Enter a row of numbers (1-9) : ")
    if len(inputRow) > 9:
        print("Longer than 9 digits!")
        print ("Entered values do not make a SUDOKO! - NO!!")
        exit()
    try:
        inputList = [int (y) for y in inputRow]
    except ValueError:
        print ("Invalid value found!")
        print ("Entered values do not make a SUDOKO! - NO!!")
        exit()
    result = checkIfDuplicates(inputList)
    if result:
        print('Row contains duplicate values!')
        print ("Entered values do not make a SUDOKO! - NO!!")
        exit()
    rows.append(inputList)

columns = (list(zip(*[list(i) for i in rows])))

for y in range(totalcolumns):
    result = checkIfDuplicates(columns[y])
    if result:
        print('Column contains duplicate values!')
        print ("Entered values do not make a SUDOKO! - NO!!")
        exit()

rowstartposition = 0
rowendposition = 3

for k in range(3):
    startposition = 0
    endposition = 3

    for j in range(3):
        squaresList=[]

        for i in range(startposition,endposition):
            squaresRow = (rows[i][rowstartposition:rowendposition])
            squaresList.extend(squaresRow)
        squares.append(squaresList)
        startposition += 3
        endposition +=3
        
    rowstartposition += 3
    rowendposition += 3
    
for z in range(totalsquares):
    result = checkIfDuplicates(squares[z])
    if result:
        print('Square contains duplicate values!')
        print ("Entered values do not make a SUDOKO! - NO!!")
        exit()
        
print ("Entered values make a SUDOKO! - YES!!")
print (rows)
print (columns)
print (squares)
