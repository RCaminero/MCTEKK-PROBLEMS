# PROBLEM A - Password generator

import random, string

weakLong = random.randint(8, 10) # random length ranges for weak passwords (6-9 digits)
strongLong = random.randint(12, 14) # random length ranges for strong passwords (12-14 digits)

def passGenerator(): # Function to generate strong and weak passwords
    print("=============== PASSWORD GENERATOR ===============")
    print("\nHow strong you want your password to be? ")
    print("\nCHOOSE AN OPTION:\n 1. WEAK PASSWORD (8 - 10 length) \n 2. STRONG PASSWORD (12-14 length)\n")
    option = input("Choose 1 o 2: ")
    char = string.ascii_letters + string.digits + string.punctuation # Using string library for obtain the characters
    if option == '1':
      password=("").join(random.choice(char)for i in range(weakLong)) 
    elif (option == '2'):
      password=("").join(random.choice(char)for i in range(strongLong)) 
    else:
      password="Invalid value, must be 1 or 2. Try again."

    return print(f"\n{password}")

if __name__ == "__main__":
    passGenerator()