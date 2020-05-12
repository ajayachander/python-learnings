def isPrime(num):
    for j in range(2,num+1):
        if ((num % j == 0) and (num == j)):
            return True
            break
        elif num % j !=0:
            continue
        elif num % j == 0:
            return False
            break
            
for i in range(1, 40):
    if isPrime(i + 1):
	    print(i + 1, end=" ")
print()