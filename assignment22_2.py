class Circle:
    PI=3.14

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0
        
    def Accept(self):
     self.Radius=float(input("Enter radius of a circle : "))

    def calculateArea(self):
     self.Area=Circle.PI*self.Radius*self.Radius

    def calculateCircumference(self):
        self.Circumference=2*Circle.PI*self.Radius

    def Display(self):
       print("Radius :",self.Radius,"Area : ",self.Area,"Circumference : ",self.Circumference)

obj1=Circle()
obj1.Accept()
obj1.calculateArea()
obj1.calculateCircumference()
obj1.Display()