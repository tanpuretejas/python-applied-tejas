class BankAccount:
    def __init__(self,name,balance):
        self.__account_holder=name
        self.__balance=balance
    def __str__(self):
        return f"account created for {self.__account_holder} with balance {self.__balance}"
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self,value):
        if value<0:
            print(f"Invalid deposit amount {value} amount should be positive")
        else:
            print("depositing",value)
            self.__balance+=value
            print(f"balance after depositing {self.__balance}")
    
    def withdraw(self,amount):
        if amount<0:
            print(f"Invalid amount {amount} withdrawal amount should be positive")
        elif amount>self.__balance:
            print(f"trying to withdraw {amount} Insufficiant Balanace {self.__balance}")
        else:
            self.__balance-=amount
            print(f"withdrawing {amount}\nbalance after withdrawal {self.__balance}")        
        
acc=BankAccount("tejas tanpure",5000)
print(acc)
print(acc.balance)
acc.deposit(1000)
acc.withdraw(1000)
acc.withdraw(9000)
acc.deposit(2000)

