import threading

def EvenList():
        sum=0
        for i in lst:
             if i%2==0:
            # print("Even numbers are:",i)
              sum=sum+i
        print("sum of even numbers is :",sum)


def OddList():
        sum=0
        for i in lst:
             if i%2!=0:
            # print("odd numbers are:",i)
              sum=sum+i
        print("sum of odd numbers is :",sum)
                  
             
   
   
            


if __name__ == "__main__":
    n=int(input("Enter number of elements : "))

    lst=[]
    for i in range(n):
        ele=int(input("Enter elements :"))
        lst.append(ele)
    
    t1=threading.Thread(target=EvenList,name="EvenListthread")
    t2=threading.Thread(target=OddList,name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


  
    