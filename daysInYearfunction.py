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

def dayOfYear(year, month, day):
    monthLength = [31,28,31,30,31,30,31,31,30,31,30,31]
    numberofDays = 0
    for i in range(len(monthLength)):
        if i == (month-1):
            numberofDays += day
            break
        else:
            numberofDays += monthLength[i]
    return numberofDays
# testYr = 2000
# testMo = 12
# testDay = 31
# print(dayOfYear(testYr, testMo, testDay))

yr = int(input("Input Year :")) 
mo = int(input("Input Month :"))
day = int(input("Input Day :"))
print("Number of days in the year : ",dayOfYear(yr, mo, day))