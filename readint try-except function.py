def readint(prompt, min, max):
#
# put your code here
    while True:
        try:
            v = int(input(prompt))
        except ValueError:
            print("Error: wrong input")
        else:
            if v in range(min,(max+1)):
                return v
            else:
                print("Error: the value is not within permitted range (",min,"..",max,")")
                
v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
