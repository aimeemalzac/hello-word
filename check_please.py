
def split_check(total, number_of_people):
	if number_of_people <=1:
		raise ValueError ("More than 1 person is required to split")
	cost_per_person = (total / number_of_people)
	return cost_per_person
# tirar o erro da tela do usuário
try:
	total_due = float(input("What is the total?	"))
	number_of_people = int(input("How many people? "))
except NameError:
	print("Oh no! Try again, put the number!")
else:
	amount_due = split_check(total_due, number_of_people)
	print("Each person owes ${}".format(amount_due))