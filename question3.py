n=int(input("Enter number :"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i

if n==sum:
    print("It is a perfect number")
else:
    print("It is not perfect number")