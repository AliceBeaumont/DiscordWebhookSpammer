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

print(style.GREEN + '''
         _    _      _     _                 _      _____          _
        | |  | |    | |   | |               | |    |  _  \        | |                            
        | |  | | ___| |__ | |__   ___   ___ | | __ | | | |___  ___| |_ _ __ ___  _   _  ___ _ __ 
        | |/\| |/ _ \ '_ \| '_ \ / _ \ / _ \| |/ / | | | / _ \/ __| __| '__/ _ \| | | |/ _ \ '__|
        \  /\  /  __/ |_) | | | | (_) | (_) |   <  | |/ /  __/\__ \ |_| | | (_) | |_| |  __/ |   
         \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |___/ \___||___/\__|_|  \___/ \__, |\___|_|   
                                                                                  __/ |          
                                                                                 |___/          

      ''')


      



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
