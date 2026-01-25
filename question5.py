from functools import reduce

num=[2,4,10,8,5,3]
max_num=reduce(lambda x,y:max(x,y),num )
print(max_num)