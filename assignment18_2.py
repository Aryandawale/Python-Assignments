def maxlist():
    n=int(input("Enter number of elements:"))
    lst=[]
    total=0
    for i in range(n):
        num=int(input("Enter elemnts :"))
        lst.append(num)
        total=max(lst)
    return total
result=maxlist()
print("maximum number is :",result)