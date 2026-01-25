from functools import reduce
num=[2,4,10,1,5,7]
min_num=reduce(lambda x,y:min(x,y),num)
print(min_num)