myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 4, 1, 2, 4, 9, 2, 1]
newList = []

for i in myList:
    if i not in newList:
        newList.append(i)
        
print("The list with unique elements only:")
print(newList)
