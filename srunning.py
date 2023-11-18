import requests, argparse, os, sys, threading, platform, socket
from colorama import Fore,Back,Style
from time import sleep
from time import *
srunning=f"""{Fore.YELLOW} ____                         _
/ ___| _ __ _   _ _ __  _ __ (_)_ __   __ _
\___ \| '__| | | | '_ \| '_ \| | '_ \ / _` |
 ___) | |  | |_| | | | | | | | | | | | (_| |
|____/|_|   \__,_|_| |_|_| |_|_|_| |_|\__, |
            {Fore.RESET}Version 0.1.4{Fore.YELLOW}             |___/{Fore.RESET}
            """
print(srunning)
if os.path.exists("srunning-language.log"):
    with open("srunning-language.log") as f:
        language = f.read()
        if "ENG" in language:
            language_code = "english"
        elif "CZ" in language:
            language_code = "czech"
        else:
            print("[ERROR] Not Selected Language")
else:
    print("[ERROR] Not Selected Language")
    language = input("[INPUT] Please Enter Language (CZ OR ENG) => ")
    if language=="cz" or "CZ":
        with open("srunning-language.log","+w") as f:
            f.write("language=[CZ]")
            language_code = "czech"
            print(f"[SUCCEFULLY] Set Language => {language_code}")
    elif language=="ENG" or "eng":
        with open("srunning-language.log","+w") as f:
            f.write("language=ENG]")
            language_code = "english"
            print(f"[SUCCEFULLY] Set Language => {language_code}")
    else:
        print("[ERROR] Not Selected language")
            
            
    

def english():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", type=str, help="scanning and working with IP address")
  parser.add_argument("--batch", action="store_true", help="creating a file from a connection or disconnection from IP Addressi")
  parser.add_argument("--language", type=str, help="selecting a new language from the list (CZ or ENG) EXAMPLE => srunning --language")
  parser.add_argument("--nocolor", action="store_true", help="scripting will not be in colour")
  parser.add_argument("--history", action="store_true", help="history of new connections or disconnections from IP Addressi")
  parser.add_argument("--update", action="store_true",help="updates srunning")

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
  def colored():
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
    with open(f"srunning-IP.log","a") as f:
        f.write("\n\n")
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
                        with open(f"srunning-IP.log","a") as f:
                             
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
                        with open(f"srunning-IP.log","a") as f:
                             time_string = strftime("%I:%M:%S %p")
                             f.write(f"\n[OFFLINE] {ip}:{port} {time_string}")
                        status_call = "offline"
                 else:
                      pass
   if args.language:
       if args.language=="cz" or "CZ":
           with open("srunning-language.log","+w") as f:
               f.write("language=[CZ]")
               SuccessfullyMessage("LANGUAGE => CZECH")
       elif args.language=="ENG" or "eng":
           with open("srunning-language.log","+w") as f:
               f.write("language=[ENG]")
               SuccessfullyMessage("LANGUAGE => ENGLISH")
  def nocolored():
   def ErrorMessage_NoColor(text):
     print(f"[!] {text}")
   def InfoMessage_NoColor(text):
     print(f"[*] {text}")
   def SuccessfullyMessage_NoColor(text):
     print(f"[+] {text}")
   def InputMessage_NoColor(text):
     Input = input(f"[?] > ")
   def TryMessage_NoColor(text):
     print(f"[/] {text}")
   InfoMessage_NoColor("Checking OS PLATFORM")
   if system == "Windows":
        osname = "win"
        SuccessfullyMessage_NoColor(f"Your OS PLATFORM => {system}")
   elif system == "Linux":
        osname = "lnx"
        SuccessfullyMessage_NoColor(f"Your OS PLATFORM => {system}")
   elif system == "Darwin":
        osname = "mac"
        SuccessfullyMessage_NoColor(f"Your OS PLATFORM => {system}")
   else:
        ErrorMessage_NoColor(f"Can't run program in your OS PLATFORM : {system}")
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
         ErrorMessage_NoColor("PORT not select")
         port = 8000
         ip = str(args.i)
         InfoMessage_NoColor(f"Port => {port}")
    running = True
    checking_info = f"{Fore.YELLOW}UNKNOW{Fore.RESET}"
    status_call = "uknow"
    with open(f"srunning-IP.log","a") as f:
        f.write("\n\n")
    while running:
        if osname=="win":
                 os.system("cls")
        elif osname=="lnx" or "mac":
                 os.system("clear")
        print(f"""{Fore.RESET}
┌────────[IP]────────[PORT]────[STATUS]
|  {ip}      {port}     {checking_info}
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
                        with open(f"srunning-IP.log","a") as f:
                             
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
                        with open(f"srunning-IP.log","a") as f:
                             time_string = strftime("%I:%M:%S %p")
                             f.write(f"\n[OFFLINE] {ip}:{port} {time_string}")
                        status_call = "offline"
                 else:
                      pass
   if args.language:
       if args.language=="cz" or "CZ":
           with open("srunning-language.log","+w") as f:
               f.write("language=[CZ]")
               SuccessfullyMessage_NoColor("LANGUAGE => CZECH")
       elif args.language=="ENG" or "eng":
           with open("srunning-language.log","+w") as f:
               f.write("language=[ENG]")
               SuccessfullyMessage_NoColor("LANGUAGE => ENGLISH")
  if args.history:
       if os.path.exists("srunning-IP.log"):
           with open("srunning-IP.log","+r") as f:
               ip_address_history = f.read()
               print(ip_address_history)
  if args.update:
               def step_three():
                        TryMessage("Stahnout SRunning Nejnovejsi verze na GITHUBU")
                        def stahnout_obsah_url(url):
                         try:
                              odpoved = requests.get(url)
                              odpoved.raise_for_status()
                              return odpoved.text
                         except requests.exceptions.HTTPError as errh:
                              ErrorMessage("HTTP Chyba:",errh)
                         except requests.exceptions.ConnectionError as errc:
                              ErrorMessage("Error Pripojeni:",errc)
                         except requests.exceptions.Timeout as errt:
                              ErrorMessage("Chyba casoveho limitu:",errt)
                         except requests.exceptions.RequestException as err:
                              ErrorMessage("Jine Chyby:",err)

                        url = 'https://raw.githubusercontent.com/DaM201/SRunning/main/srunning.py'

                        obsah_stranky = stahnout_obsah_url(url)
                        if obsah_stranky:
                              with open('srunning.py', '+w', encoding='utf-8') as soubor:
                                   soubor.write(obsah_stranky)

                                   aktualni_slozka = os.getcwd()
                                   SuccessfullyMessage(f"Soubor byl stažen a uložen jako \"srunning.py\" ve složce => {aktualni_slozka}")
                                   threading.Thread(target=exit_command).start()
               def step_two():
                   try:
                       TryMessage("Odstranovani srunning")
                       os.unlink(cesta_ke_skriptu)
                       SuccessfullyMessage("Odstraněno srunning")
                       threading.Thread(target=step_three).start()
                   except:
                       ErrorMessage("Cesta k vašemu Srunningu. Zkuste prosím najít cestu k srunningu a smazat srunning. pak přejděte na tuto webovou stránku => https://github.com/DaM201/SRunning/releases/tag/SRunning a stáhněte si nejnovější srunning.")
                       threading.Thread(target=exit_command).start()
               try:
                   TryMessage("získat cestu srunning")
                   cesta_ke_skriptu = os.path.abspath(sys.argv[0])
                   SuccessfullyMessage("získat cestu srunning")
                   threading.Thread(target=step_two).start()
               except:
                   ErrorMessage("Cesta k vašemu Srunningu. Zkuste prosím najít cestu k srunningu a smazat srunning. pak přejděte na tuto webovou stránku => https://github.com/DaM201/SRunning/releases/tag/SRunning a stáhněte si nejnovější srunning.")
                   threading.Thread(target=exit_command).start()
  if args.nocolor:
      threading.Thread(target=nocolored).start()
  else:
      threading.Thread(target=colored).start()






def czech():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", type=str, help="scanovani a pracovaní s IP Address")
  parser.add_argument("--soubor", action="store_true", help="vytvoření souboru ze pripojeni nebo odpojeni ze IP Addressi")
  parser.add_argument("--jazyk", type=str, help="vybraní novýho jazyka ze nabýtky (CZ nebo ENG) EXAMPLE => srunning --jazyk ")
  parser.add_argument("--nebarva", action="store_true", help="scriptovani nebude v barve.")
  parser.add_argument("--historie", action="store_true", help="historie nový připojení nebo odpojení ze IP Addressi")
  parser.add_argument("--aktualizace",action="store_true",help="aktualizuje program srunning")

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
  def colored():
   InfoMessage("Kontroluji OPERACNI SYSTEM")
   if system == "Windows":
        osname = "win"
        SuccessfullyMessage(f"Tvuj OPERACNI SYSTEM => {system}")
   elif system == "Linux":
        osname = "lnx"
        SuccessfullyMessage(f"Tvuj OPERACNI SYSTEM => {system}")
   elif system == "Darwin":
        osname = "mac"
        SuccessfullyMessage(f"Tvuj OPERACNI SYSTEM => {system}")
   else:
        ErrorMessage(f"Program nemuze bezet ve vasim OPERACNIM SYSTEMU : {system}")
        threading.Thread(target=exit_command).start()
   if args.i:
    if args.soubor:
             filename = str(args.soubor)
             filename = "ONLINE"
                  
    else:
                filename = None
    
    running = True
    try:
         ip,port = str(args.i).split(":")
    except:
         ErrorMessage("PORT nebyl zvolen")
         port = 8000
         InfoMessage(f"Port => {port}")
    running = True
    checking_info = f"{Fore.YELLOW}NEZNAMI{Fore.RESET}"
    status_call = "uknow"
    with open(f"srunning-IP.log","a") as f:
        f.write("\n\n")
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
            checking_info = f"{Fore.GREEN}AKTIVNY{Fore.RESET}"
            if filename==None:
                 pass
            else:
                 if filename=="ONLINE" or "online":
                    if status_call=="online":
                         pass
                    else:
                        with open(f"srunning","a") as f:
                             
                             time_string = strftime("%I:%M:%S %p")
                             f.write(f"\n[AKTIVNY] {ip}:{port} {time_string}")
                        status_call = "online"
                 else:
                      pass
        except socket.error:
            checking_info = f"{Fore.RED}NEAKTIVNY{Fore.RESET}"
            if filename==None:
                 pass
            else:
                 if filename=="OFFLINE" or "offline":
                    if status_call=="offline":
                         pass
                    else:
                        with open(f"srunning-IP.log","a") as f:
                             time_string = strftime("%I:%M:%S %p")
                             f.write(f"\n[NEAKTIVNY] {ip}:{port} {time_string}")
                        status_call = "offline"
                 else:
                      pass
   if args.jazyk:
       if args.jazyk=="ENG" or "eng":
           with open("srunning-language.log","+w") as f:
               f.write("language=[ENG]")
               SuccessfullyMessage("JAZYK => ANGLICTINA")
       elif args.jazyk=="cz" or "CZ":
           with open("srunning-language.log","+w") as f:
               f.write("language=[CZ]")
               SuccessfullyMessage("JAZYK => CESTINA")
  def nocolored():
   def ErrorMessage_NoColor(text):
     print(f"[!] {text}")
   def InfoMessage_NoColor(text):
     print(f"[*] {text}")
   def SuccessfullyMessage_NoColor(text):
     print(f"[+] {text}")
   def InputMessage_NoColor(text):
     Input = input(f"[?] > ")
   def TryMessage_NoColor(text):
     print(f"[/] {text}")
   InfoMessage_NoColor("Kontroluji OPERACNI SYSTEM")
   if system == "Windows":
        osname = "win"
        SuccessfullyMessage_NoColor(f"Tvuj OPERACNI SYSTEM => {system}")
   elif system == "Linux":
        osname = "lnx"
        SuccessfullyMessage_NoColor(f"Tvuj OPERACNI SYSTEM => {system}")
   elif system == "Darwin":
        osname = "mac"
        SuccessfullyMessage_NoColor(f"YTvuj OPERACNI SYSTEM => {system}")
   else:
        ErrorMessage_NoColor(f"Program nemuze bezet ve vasim OPERACNIM SYSTEMU : {system}")
        threading.Thread(target=exit_command).start()
   if args.i:
    if args.soubor:
             filename = str(args.soubor)
             filename = "ONLINE"
                  
    else:
                filename = None
    
    running = True
    try:
         ip,port = str(args.i).split(":")
    except:
         ErrorMessage_NoColor("PORT nebyl zvolen")
         port = 8000
         InfoMessage_NoColor(f"Port => {port}")
    running = True
    checking_info = f"{Fore.YELLOW}NEZNAMI{Fore.RESET}"
    status_call = "uknow"
    with open(f"srunning-IP.log","a") as f:
        f.write("\n\n")
    while running:
        if osname=="win":
                 os.system("cls")
        elif osname=="lnx" or "mac":
                 os.system("clear")
        print(f"""{Fore.RESET}
┌────────[IP]────────[PORT]────[STATUS]
|  {ip}      {port}     {checking_info}
└─────────────────────────────────────<""")
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((ip, int(port)))
            checking_info = f"{Fore.GREEN}AKTIVNY{Fore.RESET}"
            if filename==None:
                 pass
            else:
                 if filename=="ONLINE" or "online":
                    if status_call=="online":
                         pass
                    else:
                        with open(f"srunning-IP.log","a") as f:
                             
                             time_string = strftime("%I:%M:%S %p")
                             f.write(f"\n[AKTIVNY] {ip}:{port} {time_string}")
                        status_call = "online"
                 else:
                      pass
        except socket.error:
            checking_info = f"{Fore.RED}NEAKTIVNY{Fore.RESET}"
            if filename==None:
                 pass
            else:
                 if filename=="OFFLINE" or "offline":
                    if status_call=="offline":
                         pass
                    else:
                        with open(f"srunning-IP.log","a") as f:
                             time_string = strftime("%I:%M:%S %p")
                             f.write(f"\n[NEAKTIVNY] {ip}:{port} {time_string}")
                        status_call = "offline"
                 else:
                      pass
   if args.jazyk:
       if args.jazyk=="ENG" or "eng":
           with open("srunning-language.log","+w") as f:
               f.write("language=[ENG]")
               SuccessfullyMessage_NoColor("JAZYK => ANGLICTINA")
       elif args.jazyk=="cz" or "CZ":
           with open("srunning-language.log","+w") as f:
               f.write("language=[CZ]")
               SuccessfullyMessage_NoColor("JAZYK => CESTINA")
  if args.historie:
       if os.path.exists("srunning-IP.log"):
           with open("srunning-IP.log","+r") as f:
               ip_address_history = f.read()
               print(ip_address_history)
  if args.nebarva:
      threading.Thread(target=nocolored).start() 
  else:
      threading.Thread(target=colored).start()
if language_code=="czech":
    threading.Thread(target=czech).start()
if language_code=="english":
    threading.Thread(target=english).start()