# latte.py
from coffee import Coffee
from resources import Resources

class Latte(Coffee):
    water=50
    milk=150
    coffee=15
    money=150.55

    def prepare(self, resources:Resources) -> Resources:
        print("Preparing Latte")
        resources.set_water(resources.get_water()-self.water)
        resources.set_milk(resources.get_milk()-self.milk)
        resources.set_coffee(resources.get_coffee()-self.coffee)
        resources.set_money(resources.get_money()+self.money)

        print("After latte preparation:\n")
        resources.__str__()
        return resources
    
    def checkResource(self, resource) -> bool:
        print("Checking resources for Latte")
        print("get_water()-self.water: ", (resource.get_water()-self.water))
        print("get_milk()-self.milk: ", (resource.get_milk()-self.milk))
        print("get_coffee()-self.coffee: ",(resource.get_coffee()-self.coffee))
        isEnoughWater = (resource.get_water()-self.water) >= 0
        isEnoughMik = ((resource.get_milk()-self.milk) >= 0)
        isEnoughCoffee = ((resource.get_coffee()-self.coffee) >= 0)
        return [isEnoughWater, isEnoughMik, isEnoughCoffee]
    
    def checkMoney(self, resource:Resources, userMoney):
        print("Check money - user: ", self.money - float(userMoney))
        return (self.money - userMoney)