from functools import reduce
num=[2,3,4,5]
sum=reduce(lambda x,y:x+y,num)
print(sum)