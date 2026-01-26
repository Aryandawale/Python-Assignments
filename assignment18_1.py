def listadd():
    n=int(input("Enter number of elements : "))
    lst=[]
    total=0
    for i in range(n):
     num=int(input("Enter number: "))
     lst.append(num)
     total=total+num
    return total
result=listadd()
print("sum is :",result)



    

