distance = float(input("What is the distance in km?"))
MPG = float(input("How much does the car take per 100km?"))
price_per_liter = float(input("what is the gas price in euros?"))

print("The cost of the trip will be: " + str(distance*MPG*price_per_liter) + " euros")
