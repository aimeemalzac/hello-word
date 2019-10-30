TICKET_PRICE = 10

tickets_remaining = 100

	
name = input("What is you name?	")
print("Hello", name)
print("There are {} tickets remaining!".format(tickets_remaining))
many = int(input("How many tickets do you like, {}?	".format(name)))
total =(many) * (TICKET_PRICE)
print("It will cost you $ {} dolar.".format(total))
ask = input("Do you want to proceed?	s/n ")
if ask.lower() == "s":
	print("SOLD!")
else:
	print("No problem, thanks {}!". format(name))
