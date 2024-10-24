#Password Generator Project

from generator import easyPasswordGenerator, strongPasswordGenerator

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


choice = input("Do you want Easy or Strong Password:\n")
if choice.lower() == "easy":
    print(easyPasswordGenerator(nr_letters, nr_numbers, nr_symbols))
elif choice.lower() == "strong":
    print(strongPasswordGenerator(nr_letters, nr_numbers, nr_symbols))
else: 
    print("Wrong Choice !!!!")




