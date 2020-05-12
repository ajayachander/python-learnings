print0 = ("###","# #","# #","# #","###")
print1 = ("  #","  #","  #","  #","  #")
print2 = ("###","  #","###","#  ","###")
print3 = ("###","  #","###","  #","###")
print4 = ("# #","# #","###","  #","  #")
print5 = ("###","#  ","###","  #","###")
print6 = ("###","#  ","###","# #","###")
print7 = ("###","  #","  #","  #","  #")
print8 = ("###","# #","###","# #","###")
print9 = ("###","# #","###","  #","###")

printList = [print0,print1,print2,print3,print4,print5,print6,print7,print8,print9]

inputVal = int(input("Enter an integer :"))
inputStr = str(inputVal)
inputDigits = [int(x) for x in inputStr]



for j in range(5):
    result =""
    for i in inputDigits:
        result += printList[i][j]+" "
    print (result, sep="\n")



    
