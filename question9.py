from functools import reduce
num=[2,3,4]
product=reduce(lambda x,y:x*y ,num)
print(product)