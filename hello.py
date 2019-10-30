first_name = input("what is your first name?    ")
print("hello,", first_name)
if first_name == "aimee":
    print(first_name, "is learning python")
elif first_name == "joao":
    print(first_name, "is learning with fellow students!")
else:
    age = int (input ("How old are you?"  ))
    # pergunta sobre a idade
    if age <=6:
        print ("Wow you're {}! If you're confident with your reading already...".format(age))
        print("You should totally learn Python, {}!".format(first_name))
print("have a great day {}!".format(first_name))






def square(number):
    total = number * number
	result = ("The square of {} is {}".format(number, total))
	print(result)

square(10)

# código rodando certinho aqui:

def big (first_number):
	result_1 = first_number * first_number
	result = ("The number {} squared is {}".format(first_number, result_1))
	print(result)

big(10)

    