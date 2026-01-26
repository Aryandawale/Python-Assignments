import Marvellousnum

def ListPrime():
    n = int(input("Enter number of elements: "))
    lst = []
    sum = 0

    for i in range(n):
        ele = int(input("Enter number: "))
        lst.append(ele)

    for i in lst:
        if Marvellousnum.checkPrime(i):
            sum = sum + i

    return sum


result = ListPrime()
print("Sum of prime numbers is:", result)

