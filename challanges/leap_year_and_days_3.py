def isYearLeap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):
    if year < 1500 or month < 1 or month > 12:
        return None
    if isYearLeap(year) and month == 2:
        return 29
    elif month == 2:
        return 28
    elif month < 8 and month % 2 != 0:
        return 31
    elif month >= 8 and month % 2 == 0:
        return 31
    else:
        return 30

def dayOfYear(year, month, day):
    count = 0
    if daysInMonth(year, month) == None or daysInMonth(year, month) < day or day < 1:
        return None
    if month == 1:
        count += day
    else:
        for x in range(1, month):
            count += daysInMonth(year, x)       
        count += day
    return count       

def daysLeftInYear(year, month, day):
    yearInDays = 365
    if isYearLeap:
        yearInDays += 1
    count = 0
    if dayOfYear(year, month, day) == None:
        return None
    if month == 1:
        count += day
    else:
        for x in range(1, month):
            count += daysInMonth(year, x)       
        count += day
    leftDays = yearInDays - count
    return leftDays

print(dayOfYear(2000, 12, 31))
