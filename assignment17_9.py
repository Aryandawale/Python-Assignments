def digicount(n):
 count=0
 while n > 0:
    count=count+1
    n=n//10
 return count
a=int(input("Enter number : "))
result=digicount(a)
print(result)