def fi(x):
    fibSeq = []
    while len(fibSeq) < x+1:
        if len(fibSeq) == 0:
            fibSeq.append(0)
        elif len(fibSeq) == 1:
            fibSeq.append(1)
        else:
            fibSeq.append(fibSeq[-1]+fibSeq[-2])
    print("The Fibonacci sequence is:")
    print(str(fibSeq)+"\n")
    print("The number is:")
    print(fibSeq[-1])

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()