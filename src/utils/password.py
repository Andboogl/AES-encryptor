"""Module for password generation"""


import random


english_alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
english_alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '123456789'
symbols = '/?.,(#'


def generate_password(length):
    """Generate a random password"""
    result = ''

    for _ in range(length):
        symbols_list = random.choice(
            [
                english_alphabet_lower,
                english_alphabet_upper,
                numbers, symbols
            ]
            )
        symbol = random.choice(symbols_list)
        result += symbol

    return result
