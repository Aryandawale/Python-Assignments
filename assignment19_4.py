from functools import reduce
a=int(input("Enter number of elements: "))
lst=[]
for i in range(a):
    num=int(input("Enter numbers : "))
    lst.append(num)
    print(lst)

even_nums=list(filter(lambda x: x%2==0,lst))
print("List after filter :",even_nums)

map_squa=list(map(lambda x:x*x,even_nums))
print("List after map :",map_squa)

reduce_map=reduce(lambda x,y:x+y,map_squa)
print("Output of reduce = ",reduce_map)