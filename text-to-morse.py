import os
from art import logo

# first the letters (a-z), then the numbers (0-9)
morse_letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
                 "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]

WHITE = '\033[0m'    # white
RED = '\033[31m'     # red
GREEN = '\033[32m'   # green
ORANGE = '\033[33m'  # orange
BLUE = '\033[34m'    # blue
PURPLE = '\033[35m'  # purple

def clear():
    os.system('clear')


def is_valid(message):
    validated = True
    for char in message:
        ascii_code = ord(char)
        if char.isalnum() or (ascii_code == 32):
            pass       
        else:            
            print(f"{RED}\nERROR: char '{char}' (Ascii code {ord(char)}) not allowed.")
            validated = False
            break
    return validated


def morse(message):
    if is_valid(message):
        print(f"\n{ORANGE}Morse code")
        for char in message:            
            ascii_code = ord(char)
            if (ascii_code == 32):
                print(" ")  # Used to force one word per row
            else:
                # ternary operator
                offset = 97 if ascii_code >= 97 else 48-26  # offset for 'a' or '0' in the list (0 is after the 26 letters)
                index = ord(char)-offset                    
                print(f"{GREEN}{morse_letters[index]}", end="  ")
        print("\n")
    else:
        print(f"{ORANGE}The message should contain only letters and numbers.\n")


should_end = False
while not should_end:
    clear()
    print(BLUE+logo)
    message = input(f"\n{WHITE}Type your message:  ").lower()
    morse(message)
    restart = input(f"{WHITE}Type 'yes' to encode anothe message. Otherways type 'no': ")
    if restart == "no":
        should_end = True
        print(f"\n{GREEN}Goodbye\n")
