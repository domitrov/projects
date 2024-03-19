import csv

class Item:
    pay_rate = 0.8 # pay rate after discount(20 %) offered
    all = []
    def __init__(self,name: str,price: float,quantity=0 ):
        
        # running validations of arguments recieved
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"
        
        
        # assign to self object
        self.name = name
        self.quantity = quantity
        self.price = price
        
        # actions to execute
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("Item.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get("name"),
                price=int(item.get("price")),
                quantity=int(item.get("quantity")),
            )        
      
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        


print(Item.instantiate_from_csv())
# 1:05:55












