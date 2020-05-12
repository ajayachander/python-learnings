c0 = int (input("Enter a non-zero positive integer : "))
step_count = 0

if c0 <= 0:
    print ("Invalid entry! ")
    exit()
    
while c0 != 1:
    if c0 % 2 == 1:
        c0 = 3 * c0 + 1
        print (c0)
        step_count += 1
    else:
        c0 = c0 // 2
        print (c0)
        step_count += 1
print ("Steps :", step_count)
