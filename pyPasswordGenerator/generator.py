import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def easyPasswordGenerator(numLetters: int, numNumbers: int, numSymbols: int) -> str:
    """
    Takes in various params to create a easy password.
    Eazy Level - Order not randomised:
    e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    """
    password = ""
    for i in range(numLetters):
        password += random.choice(letters)
    for i in range(numNumbers):
        password += random.choice(numbers)
    for i in range(numSymbols):
        password += random.choice(symbols)

    return password

def strongPasswordGenerator(numLetters: int, numNumbers: int, numSymbols: int) -> str:
    """
    Takes in various params to create a strong password.
    Hard Level - Order of characters randomised:
    e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    """
    password = list(easyPasswordGenerator(numLetters, numNumbers, numSymbols))
    random.shuffle(password)
    return ''.join(password)