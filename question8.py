num=[2,3,30,5,6,7,8,15]
divisible=list(filter(lambda x:x%3==0 and x%5==0,num))
print(divisible)