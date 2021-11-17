import random as r
import math as m
import pyperclip as p
import string


class PasswordGenerator:
    def __init__(self, length=16, upper=2, lower=2, numbers=2, symbols=2, spaces=1):
        self.min_length = length
        self.min_upper = upper
        self.min_lower = lower
        self.min_numbers = numbers
        self.min_symbols = symbols
        self.min_spaces = spaces
        self.alphabet = string.ascii_lowercase
        self.symbols = ['-', '(', ')', '{', '}', '[', ']', '_', '=', '+', '$', '#', '%', '!', '?', '/', '<', '>']

    def generate(self):
        password = ""

        # Add uppercase letters
        for i in range(r.randint(self.min_upper, m.floor(self.min_length / 3))):
            password += r.choice(self.alphabet.upper())

        # Add lowercase letters
        for i in range(r.randint(self.min_lower, m.floor(self.min_length / 3))):
            password += r.choice(self.alphabet)

        # Add numbers
        for i in range(r.randint(self.min_numbers, m.floor(self.min_length / 3))):
            password += str(r.randint(0, 10))

        # Add symbols

        for i in range(r.randint(self.min_symbols, m.floor(self.min_length / 3))):
            password += r.choice(self.symbols)

        # Add spaces
        for i in range(r.randint(self.min_spaces, m.floor(self.min_length / 3))):
            password += " "

        l = list(password)
        r.shuffle(l)
        password = ''.join(l)
        p.copy(password)
        return password
