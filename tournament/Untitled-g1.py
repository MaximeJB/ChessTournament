import random
import string 


def generate_ids():

    while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            numbers = ''.join(random.choices("1234567890", k=5))  
            new_id = letters + numbers
            
            
            return new_id
            

print(generate_ids())