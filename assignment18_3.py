def minlist():
    n=int(input("Enter number of elements:"))
    lst=[]
    total=0
    for i in range(n):
        ele=int(input(" Enter elements :"))
        lst.append(ele)
        total=min(lst)
    return total
result=minlist()
print("minimum number from list is :",result)

