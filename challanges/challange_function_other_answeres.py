#answere 1
def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True


for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()

#answere 2
def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2,x):
        if x % n == 0:
            return False
    return True

print(is_prime(9))