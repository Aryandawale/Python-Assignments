def sumdigi(n):
    sum=0
    while n > 0:
        num=n%10
        sum=sum+num
        n=n//10
    return sum
a=int(input("Enter number"))
print(sumdigi(a))