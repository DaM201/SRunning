import requests, argparse, os, sys, threading, platform, socket
from colorama import Fore,Back,Style
from time import sleep
from time import *
srunning=f"""{Fore.YELLOW} ____                         _
/ ___| _ __ _   _ _ __  _ __ (_)_ __   __ _
\___ \| '__| | | | '_ \| '_ \| | '_ \ / _` |
 ___) | |  | |_| | | | | | | | | | | | (_| |
|____/|_|   \__,_|_| |_|_| |_|_|_| |_|\__, |
            {Fore.RESET}Version 0.1.1{Fore.YELLOW}             |___/{Fore.RESET}
            """
print(srunning)
parser = argparse.ArgumentParser()
parser.add_argument("-i", type=str, help="")
parser.add_argument("--batch", action="store_true", help="")
args = parser.parse_args()
system = platform.system()
def ErrorMessage(text):
   print(f"[{Style.BRIGHT}{Fore.RED}!{Fore.RESET}{Style.RESET_ALL}] {text}{Fore.RESET}")
def InfoMessage(text):
   print(f"[{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}*{Fore.RESET}{Style.RESET_ALL}] {text}{Fore.RESET}")
def SuccessfullyMessage(text):
   print(f"[{Style.BRIGHT}{Fore.GREEN}+{Fore.RESET}{Style.RESET_ALL}] {text}{Fore.RESET}")
def InputMessage(text):
   Input = input(f"[{Style.BRIGHT}{Fore.BLUE}?{Fore.RESET}{Style.RESET_ALL}] {Fore.BLUE}{text} > {Fore.RESET}")
def TryMessage(text):
   print(f"[{Style.BRIGHT}{Fore.YELLOW}/{Fore.RESET}{Style.RESET_ALL}] {text}{Fore.RESET}")
def exit_command():
    sys.exit()
osname = None
InfoMessage("Checking OS PLATFORM")
if system == "Windows":
        osname = "win"
        SuccessfullyMessage(f"Your OS PLATFORM => {system}")
elif system == "Linux":
        osname = "lnx"
        SuccessfullyMessage(f"Your OS PLATFORM => {system}")
elif system == "Darwin":
        osname = "mac"
        SuccessfullyMessage(f"Your OS PLATFORM => {system}")
else:
        ErrorMessage(f"Can't run program in your OS PLATFORM : {system}")
        threading.Thread(target=exit_command).start()
if args.i:
    if args.batch:
             filename = str(args.batch)
             filename = "ONLINE"
                  
    else:
                filename = None
    
    running = True
    try:
         ip,port = str(args.i).split(":")
    except:
         ErrorMessage("PORT not select")
         port = 8000
         InfoMessage(f"Port => {port}")
    running = True
    checking_info = f"{Fore.YELLOW}UNKNOW{Fore.RESET}"
    status_call = "uknow"
    while running:
        if osname=="win":
                 os.system("cls")
        elif osname=="lnx" or "mac":
                 os.system("clear")
        print(f"""{Fore.RESET}
┌────────[{Fore.GREEN}IP{Fore.RESET}]────────[{Fore.GREEN}PORT{Fore.RESET}]────[{Fore.GREEN}STATUS{Fore.RESET}]
|  {Fore.YELLOW}{ip}{Fore.RESET}      {Fore.YELLOW}{port}{Fore.RESET}     {checking_info}{Fore.YELLOW}{Fore.RESET}
└─────────────────────────────────────<""")
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((ip, int(port)))
            checking_info = f"{Fore.GREEN}ONLINE{Fore.RESET}"
            if filename==None:
                 pass
            else:
                 if filename=="ONLINE" or "online":
                    if status_call=="online":
                         pass
                    else:
                        with open(f"srunning{ip}","a") as f:
                             
                             time_string = strftime("%I:%M:%S %p")
                             f.write(f"\n[ONLINE] {ip}:{port} {time_string}")
                        status_call = "online"
                 else:
                      pass
        except socket.error:
            checking_info = f"{Fore.RED}OFFLINE{Fore.RESET}"
            if filename==None:
                 pass
            else:
                 if filename=="OFFLINE" or "offline":
                    if status_call=="offline":
                         pass
                    else:
                        with open(f"srunning{ip}","a") as f:
                             time_string = strftime("%I:%M:%S %p")
                             f.write(f"\n[OFFLINE] {ip}:{port} {time_string}")
                        status_call = "offline"
                 else:
                      pass
