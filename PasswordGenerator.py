import random
import string

print("--- Password Generator ---")

def generate_pass():
    characters = string.ascii_letters + string.digits
    
    length = int(input("How many characters do you want the password be? "))
    
    password = "".join(random.choice(characters) for i in range(length))
    
    print("-" * 30)
    print(f"Your Secure Password: {password}")
    print("-" * 30)
    print("Keep it safe!")

generate_pass()
