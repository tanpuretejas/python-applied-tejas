class Laptop:
    def __init__(self):
        self.ram=None
        self.processor=None
        self.brand_name=None
        self.storage=None
    def show_config(self):
        self.brand_name=input("enter brand name:")
        self.ram=int(input("enter ram of your laptop:"))
        self.storage=float(input("enter storage of your laptop:"))
        self.processor=input("enter processor of your laptop:")

        print("\nbrand name is:",self.brand_name)
        print("ram of your laptop is:",self.ram)
        print("storage of your laptop is:",self.storage)
        print("processor of your laptop is:",self.processor)

    def is_gaming_laptop(self):
        if self.ram>=16 and ("i7" in self.processor or "i9" in self.processor):
            print("this laptop is the gaming laptop:",self.brand_name,"\n")
        else:
            print("this laptop is not for gaming:",self.brand_name,"\n")

l1=Laptop()
l2=Laptop()
l1.show_config()
l1.is_gaming_laptop()
l2.show_config()
l2.is_gaming_laptop()