class BankAccount:
    ROI=10.5

    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount

    def Display(self):
       
        print("Name : ",self.Name,"Current Balance :",self.Amount)
        print()

    def Deposit(self):
        deposit_amount=int(input("Enter Deposit Amount :"))
        self.Amount=self.Amount+deposit_amount
        print()

    def Withdraw(self):
        withdraw_amount=int(input("Enter Amount of Withdraw:"))
        if withdraw_amount <= self.Amount:
            self.Amount = self.Amount - withdraw_amount
            print("current Balance :", self.Amount)
           
        else:
            print("your balance is not sufficient")
        print()

    def CalculateInterest(self):
        Interest=(self.Amount*BankAccount.ROI)/100
        print("Total Interest : ",Interest)
        

obj1=BankAccount("Aryan",5000)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()


    