from functools import reduce
n=int(input("Enter number of elements :"))
lst=[]
for i in range(n):
    num=int(input("Enter elements :"))
    lst.append(num)
    print(lst)
gret_nums=list(filter(lambda x:70 <= x <= 90,lst))
print("list after filter",gret_nums)

incre_nums=list(map(lambda x:x+10,gret_nums))
print("list after map",incre_nums)

pro_nums=reduce(lambda x,y:x*y,incre_nums)
print("output of reduce",pro_nums)