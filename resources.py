# resources.py

class Resources:
    def __init__(self, water = 600, milk = 150, coffee = 100, money = 0.0): 
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

    # getter % setter methods 
    def get_water(self): 
        return self.water 
      
    def set_water(self, value): 
        self.water = value

    def get_milk(self): 
        return self.milk 
      
    def set_milk(self, value): 
        self.milk = value

    def get_coffee(self): 
        return self.coffee 
      
    def set_coffee(self, value): 
        self.coffee = value 

    def get_money(self):
        return self.money
    
    def set_money(self, value):
        self.money = value

    def __str__(self) -> str:
        report = "Water: "+ str(self.get_water()) + " mL\n"
        report += "Milk: " + str(self.get_milk()) + " mL\n"
        report += "Coffee: " + str(self.get_coffee()) + " gr\n"
        report += "Money: $" + str(self.get_money())
        return report

