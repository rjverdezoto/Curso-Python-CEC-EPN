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

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

