class Numbers:

    def __init__(self):
     self.value=int(input("Enter value : "))

     
    def ChkPrime(self):
        
        if self.value <= 1:
            print("Not Prime")
            return

        for i in range(2, self.value):
            if self.value % i == 0:
                print("Not Prime")
                return
        print("Prime")

    def ChkPerfect(self):
      

       sum = 0

       for i in range(1, self.value):
           if self.value % i == 0:
            sum = sum + i

       if sum == self.value:
        print(self.value, "is a Perfect Number")
       else:
         print(self.value, "is NOT a Perfect Number")

    def Factors(self):
        for i in range(1,self.value+1):
          if self.value%i==0:
           print(" factor :",i)

    def SumFactor(self):
       sum=0
       for i in range(1,self.value+1):
          if self.value%i==0:
             sum=sum+i
       print(" sum of factor :",sum)

obj1=Numbers()
obj1.ChkPrime()
obj1.ChkPerfect()
obj1.Factors()
obj1.SumFactor()

