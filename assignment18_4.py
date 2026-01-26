def frequency():
    num=int(input("Enter number of elements : "))
    lst=[]
    count=0
    for i in range(num):
        ele=int(input("Enter numbers :"))
        lst.append(ele)
   
    n=int(input("Enter frequency of number:"))
    for i in lst:
        if i==n:
         count=count+1
    return count
result=frequency()
print("Frequency is: ",result)