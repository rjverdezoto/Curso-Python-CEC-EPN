def isPrime(num):
    for x in range(2,num):
        if num % x == 0:
            return False
    return True


for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()

#2 3 5 7 11 13 17 19