def isYearLeap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        return True
    else:
        return False
        
        
def daysInMonth(year, month):
    monthLength = [31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(len(monthLength)):
        if i != (mo-1):
            continue
        else:
            if (isYearLeap(yr) == True) and (mo ==2):
                return 29
            else:
                return monthLength[i]
    
testYears = [1900, 2000, 2016, 1987, 2020, 2022, 2400, 2405]
testMonths = [2, 2, 1, 11, 2, 2, 2, 5]
testResults = [28, 29, 31, 30, 29, 28, 29, 31]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")