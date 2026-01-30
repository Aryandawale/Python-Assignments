class   BookStore:
    NoOfBooks=0

    def __init__(self,name,author):
        self.name=name
        self.author=author
        BookStore.NoOfBooks+=1


    def Display(self):
        print(self.name,"by",self.author,"No of books :", BookStore.NoOfBooks )





obj1=BookStore("Linux System Programming","Robert Love")
obj1.Display()
books:1


obj2=BookStore("C Programming","Denis Ritchi")
obj2.Display()