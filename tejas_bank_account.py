class BankAccount:
    def __init__(self,name,balance):
        self.__account_holder=name
        self.__balance=balance
        print(f"account created for {self.__account_holder} with balance",self.__balance)
        
    def show_balance(self):
        print(f"current balance for {self.__account_holder}:{self.__balance}")
    
    def deposit(self,amount):
        if amount<=0:
            print("Invalid Deposit Amount")
        else:    
            self.__balance+=amount
            print(f"{amount} deposited successfully")
            self.show_balance()
    def withdraw(self,amount):
        if amount<=0:
            print("Invalid Withdrawel Amount")
        elif amount>self.__balance:
                print("insufficiant balance")
        else:
            self.__balance-=amount
            print(f"{amount} withdrawn successfully")
            self.show_balance()
    def get_balance(self):
        return self.__balance
    
b1=BankAccount("tejas tanpure",5000)
b1.show_balance()
b1.deposit(2000)
b1.withdraw(2000)
b1.withdraw(6000)
b1.withdraw(-100)

print("final balance via getter:",b1.get_balance())