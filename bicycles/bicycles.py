#This Bicycle class gives all objects of type 'bicycle' a model name, 
#a weight, and a cost to produce. 

class Bicycle (object):
	def __init__ (self, model, weight):
   		self.model = model
   		self.weight = weight
	def cost (self):
    		return 100 + 1.5*(self.weight)

#This 'Bike Shops' Class gives all bike shops a name, an inventory, the ability to sell bicycles with a margin over their #cost, and the ability to see how much profit they've made. 

class Bike_Shop(object):
	def __init__(self, shop_name, inventory):
    		self.shop_name = shop_name
    		self.inventory = inventory
    		self.profit = 0  
	
	def price (self, Bicycle):
    		return 1.2 * Bicycle.cost()
	
	def margin (self, Bicycle):
		return self.price(Bicycle) - Bicycle.cost()
	
	def buyBike(self, Bicycle, Customer):
		if Customer.fund > self.price(Bicycle):
			Customer.owned.append(Bicycle)
			self.inventory.remove(Bicycle)
			self.profit += self.margin(Bicycle)
			Customer.fund -= self.price(Bicycle)
			return True;
			
#The Customers Class shows that all customers have a name, a fund of $ to buy a new bike,
#and the ability to buy and own a new bicycle

class Customer(object):
	def __init__(self, name, fund, owned):
  		self.name = name
  		self.fund = fund
  		self.owned = owned


