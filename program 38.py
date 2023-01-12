class bank_account:
    def getData(self,name,accno,acctype,balance):
        self.name=name
        self.accno=accno
        self.acctype=acctype
        self.balance=balance
    def displaycustomer(self):
        print("customer name:",self.name)
        print("account number:",self.accno)
        print("account type:",self.acctype)
        print("balance:",self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdrawal(self,amount):
        if self.balance-amount<0:
            print("insufficient balance")
        else:
            self.balance=self.balance-amount
print("Hello Welcome To Banking System")
ch=0
obj=bank_account()
while ch!=5:
    print("select your option")
    print("1,New customer")
    print("2,Deposit")
    print("3,withdraw")
    print("4,Display")
    print("5,Exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        obj=bank_account()
        n=input("enter name")
        no=int(input("enter accound number:"))
        t=input("enter account type(SB/C):")
        b=int(input("enter balance"))
        obj.getData(n,no,t,b)
    if ch==2:
        b=int(input("enter amount to deposit:"))
        obj.deposit(b)
    if ch==3:
        b=int(input("enter amount to withdraw:"))
        obj.withdrawal(b)
    if ch==4:
        obj.displaycustomer()
    else:
        print("program terminated!!!")
