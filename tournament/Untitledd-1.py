
import random
import string


def generate_ids():
    numbers = "1234567890"
    random.seed(10)
    letters = string.ascii_lowercase
    rand_letters = random.choices(letters,k=2) # where k is the number of required rand_letters
    first_part = "".join(rand_letters)
    rand_numbers = random.choices(numbers, k=4)
    print(rand_numbers)
    second_part ="".join(rand_numbers)
    final = first_part + second_part
    print(final)

generate_ids()