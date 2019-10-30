TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining >= 1:	
	name = input("What is you name?	")
	print("Hello", name)
	print("There are {} tickets remaining!".format(tickets_remaining))
	many = int(input("How many tickets do you like, {}?	".format(name)))
	total = (many) * int(TICKET_PRICE)
	print("It will cost you $ {} dolar.".format(total))
	ask = input("Do you want to proceed?	s/n ")
	if ask.lower() == "s":
		print("SOLD!")
	tickets_remaining =- many
	else:
		print("No problem, thanks {}!". format(name))
print ("Sorry, the tickets are all sold out!")