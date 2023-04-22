import random
import string
from colorama import init, Fore, Style

init()

ascii_text = r"""
______                                          _  _____              
| ___ \                                        | ||  __ \             
| |_/ /__ _  ___  ___ __      __ ___   _ __  __| || |  \/  ___  _ __  
|  __// _` |/ __|/ __|\ \ /\ / // _ \ | '__|/ _` || | __  / _ \| '_ \ 
| |  | (_| |\__ \\__ \ \ V  V /| (_) || |  | (_| || |_\ \|  __/| | | |
\_|   \__,_||___/|___/  \_/\_/  \___/ |_|   \__,_| \____/ \___||_| |_|                                                           
"""

def generate_password(length):
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

   
    all_chars = lowercase_letters + uppercase_letters + digits + symbols

    
    password = ''.join(random.sample(all_chars, length))

    return password


password_length = int(input(Fore.CYAN + "Enter the length of the password: "))


password = generate_password(password_length)
print(Fore.GREEN + ascii_text)
print(Fore.YELLOW + "Your password is:", Style.BRIGHT + password)
print(Fore.RESET + Style.RESET_ALL)


while True:
  pass
