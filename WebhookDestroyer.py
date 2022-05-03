from dhooks import Webhook
import os


os.system("")

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.GREEN + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Welcome To Webhook Destroyer V0.1")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

hook = input("What is the webhook you'd like to spam?: ")
hook = Webhook(hook)
print("")
data = input("What Should I Spam It With?: ")
print("")
amount = int(input("How many times should i spam the webhook?: "))
print("")


for i in range(0,amount):
    hook.send(data)
    print("Spam message sent [{}] times.".format(i+1))
    



end = input("")
