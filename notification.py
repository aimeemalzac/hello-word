def yell(text):
	text = text.upper()
	number_of_characters = len(text)
	result = text + "!" * (number_of_characters // 2)
	print(result)

yell("Você está indo bem!")
yell ("Feliz Aniversário")