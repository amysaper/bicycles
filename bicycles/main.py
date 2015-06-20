from bicycles import Bicycle, Bike_Shop, Customer

bike1 = Bicycle("bike1", 100)
bike2 = Bicycle("bike2", 200)
bike3 = Bicycle("bike3", 300)
bike4 = Bicycle("bike4", 400)
bike5 = Bicycle("bike5", 500)
bike6 = Bicycle("bike6", 600)

stanford_store = Bike_Shop("stanford",[bike1, bike2, bike3, bike4, bike5, bike6, bike1, bike3])

amy = Customer("Amy", 1000,[])
michael = Customer("Michael", 500, [bike2])
dan = Customer("Dan", 350, [bike1])
customers_list = [dan,amy,michael]

for cust in customers_list:
	print cust.name	
	for bike in stanford_store.inventory:
		if (stanford_store.buyBike (bike,cust)):	
			print (bike.model)
			print("%s has %s left over" % (cust.name, cust.fund))
			break;
print ("stanford_store has %s left in stock, and made %s on these sales" %([bike.model for bike in stanford_store.inventory], stanford_store.profit))