class Arithmetic:

    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        self.Value1=int(input("Enter VAlue 1 :"))
        self.Value2=int(input("Enter Value2 : "))

    def Addition(self):
        self.Add=self.Value1+self.Value2
        print("ADDITION : ",self.Add)

    def Subtraction(self):
        self.Sub= self.Value1- self.Value2
        print("SUBTRACTION : ",self.Sub)

    def Multiplication(self):
        self.mul=self.Value1*self.Value2
        print("Multiplication : ",self.mul)

    def Division(self):
        if self.Value2 == 0:
         print("Division not possible (cannot divide by zero)")
        else:
         self.Div=self.Value1/self.Value2
         print("DIVISION : ",self.Div)

obj=Arithmetic()
obj.Accept()
obj.Addition()
obj.Subtraction()
obj.Multiplication()
obj.Division()

    

    