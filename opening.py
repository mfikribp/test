from termcolor import colored
def welcome():
    message = "WELCOME TO THE GAME"
    border = "="*25
    border_side = "|"*2
    print(f"{colored(border,color='black')}\n{colored(border_side,color='black')} {colored(message,color= 'light_magenta')} {colored(border_side,color='black')}\n{colored(border, color='black')} ")