def lookandsay(number):
    result = ""
 
    repeat = number[0]
    number = number[1:]+" "
    times = 1
 
    for actual in number:
        if actual != repeat:
            result += str(times)+repeat
            times = 1
            repeat = actual
        else:
            times += 1
 
    return result
 
num = "1"

inputFile = "C:/Users/ajayachander/Desktop/MorrisSequence.txt"


    # print (i+1, ":", num)
with open(inputFile, "w") as f:
    for i in range(50):
        # num_str = str(num)
        f.write(str(i+1) + "   :   " + str(num) + "\n")
        # print (num)
        num = lookandsay(num)
