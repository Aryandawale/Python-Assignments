import threading

def Prime():
     print("prime numbers:")
     for num in lst:
        if num <= 1:
            continue
 
        count=0
        for i in range(1, num + 1):
          if num%i==0:
            count +=1
        if count==2:
          print(num)
           


def NotPrime():
    print("Not prime numbers:")
    for num in lst:
        if num <= 1:
            print(num)
            continue
       
        count=0
        for i in range(1, num + 1):
          if num%i==0:
            count +=1
        if count!=2:
          print(num)
           



if __name__ == "__main__":
      
    n=int(input("Enter number of elements : ")) 
    lst=[]
    for i in range(n):
        ele=int(input("Enter elements : "))
        lst.append(ele)

t1=threading.Thread(target=Prime,name="primenumber")
t2=threading.Thread(target=NotPrime,name="notprime")

t1.start()
t2.start()

t1.join()
t2.join()




