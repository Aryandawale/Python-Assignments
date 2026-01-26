import threading

def EvenFactor(n):
    evensum=0
    print("Even Factors")
    for i in range(1,n+1):
        if n%i==0 and i%2==0:
            print(i)
            evensum=evensum+i
    print("sum of even factors is :",evensum)


def OddFactor(n):
    oddsum=0
    print("odd Factors")
    for i in range(1,n+1):
        if n%i==0 and i%2!=0:
            print(i)
            oddsum=oddsum+i
    print("sum of odd factors is :",oddsum)

    
if __name__ == "__main__":
     n=int(input("enter number : "))
     t1=threading.Thread(target=EvenFactor,args=(n,))
     t2=threading.Thread(target=OddFactor,args=(n,))

     t1.start()
     t2.start()

     t1.join()
     t2.join()

     print("exit from main")