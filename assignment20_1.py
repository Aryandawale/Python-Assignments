import threading

def even():
    print("even thread")
    for i in range(1,21):
        if i%2==0:
            print(i)
    
def odd():
    print("odd thread")
    for i in range(1,21):
        if i%2!=0:
            print(i)

if __name__=="__main__":
    
    t1=threading.Thread(target=even,name="even")

   
    t2=threading.Thread(target=odd,name="odd")
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()



  