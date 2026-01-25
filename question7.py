string=["mango","apple","banana","pineapple","kiwi","cherry"]
name=list(filter(lambda x: len(x)>5 ,string))
print(name)