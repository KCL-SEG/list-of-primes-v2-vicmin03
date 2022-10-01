"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

from unicodedata import numeric


def is_prime(no):
    if no == 2:
        return True
    for i in range (2, no):
        if (no%i == 0):
            return False
    return True

def primes(number_of_primes):
    if (number_of_primes > 0):
        primes_list = []
        current = 2
        while len(primes_list) < number_of_primes:
            if (is_prime(current)):
                primes_list.append(current)
            current += 1
        print(number_of_primes, primes_list)
        return primes_list
    else:
        raise ValueError("Enter a positive integer greater than 0")