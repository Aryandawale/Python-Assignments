from functools import reduce

num=int(input("Enter number of elements :"))
lst=[]
def is_prime(no):
    if no <= 1:
        return False
    
    for i in range(2,no):
        if no%i==0:
            return False
    return True
# print("Prime number is :",is_prime())
for i in range(num):
    n=int(input("Enter elements : "))
    lst.append(n)
    print(lst)

filter_num=list(filter(is_prime ,lst))
print("List after filter ",filter_num)

map_num=list(map(lambda x : x*2,filter_num))
print("List after map : ",map_num)

reduce_num=reduce(lambda x,y:x if x > y else y,map_num)
print("Output of reduce = ",reduce_num)