
class Item:
    pay_rate = 0.8
    all = []
    
    def __init__(self, name, price, quantity=0):
        assert price >= 0, "Price  is less than zero"
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
        
    def calculate(self):
        return f"{self.name.upper()} total price = {self.price * self.quantity} Euro"
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"
    def apply_discount(self):
        return f"{self.name.upper()} discount price = {(self.price * self.pay_rate) * self.quantity} Euro"
    
spam = Item("spam", 2, 100)
eggs = Item("eggs", 2, 2000)
print(spam.apply_discount())
print(Item.calculate(spam))
print(Item.all)