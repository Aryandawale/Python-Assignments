def addsum(no):
    sum=0
    for i in range(1,no+1):
        if no%i==0:
             sum=sum+i
    return sum
  
n=int(input("Enter number: "))
print(addsum(n))