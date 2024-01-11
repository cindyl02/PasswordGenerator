# Password Generator Project
import random

LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_password(num_letters, num_symbols, num_numbers):
    password_list = [random.choice(LETTERS) for _ in range(0, num_letters)]
    password_list.append([random.choice(SYMBOLS) for _ in range(0, num_symbols)])
    password_list.append([random.choice(NUMBERS) for _ in range(0, num_numbers)])
    random.shuffle(password_list)
    return ''.join(password_list)


if __name__ == '__main__':
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))
    print(gen_password(nr_letters, nr_symbols, nr_numbers))
