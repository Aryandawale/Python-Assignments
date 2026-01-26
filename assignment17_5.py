n=int(input("Enter number :"))
count=0
for i in range(2,n):
    if n%i==0:
     count=count+1 
if count==2:
    print("It is not prime number")
else:
    print("It is prime number")