import getpass
import time
import random
import requests
import wms
import os
import colorama
import stat
from config import color_map, default_dir, prompt

colorama.init()


WELCOME_MESSAGE = colorama.Fore.YELLOW + "Welcome to CF-OShell! Type 'help' for a list of commands." + colorama.Style.RESET_ALL
def print_welcome_message():
    print(WELCOME_MESSAGE)
current_dir = os.getcwd()

usrd = {'root': 'root'}
commands = ['help', 'ver', 'team', 'exit', 'ip', 'wms', 'cd', 'ls']

def login():
    usrname = input("Username : ").lower()
    if usrname in usrd:
        passw = getpass.getpass(prompt = "Password : ").lower()
        if passw == usrd[usrname]:
            print(f"Welcome back, {usrname} !")
            cmd()
        else:
            print(f"Wrong password for {usrname}")
            login()
    else:
        newuser(usrname)

def newuser(user):
    global usrd # Declare usrd as a global variable
    new_account_yn = input("Do you want to create a new account ? (y/n) : ")
    if new_account_yn == 'y':
        newpass = getpass.getpass(prompt = "New Password : ")
        usrd[user] = newpass
        login()
    else:
        login()

def ls():
    current_dir = os.getcwd()
    files_and_dir = os.listdir(current_dir)

    for file_or_directory in files_and_dir:
        file_path = os.path.join(current_dir, file_or_directory)
        file_stat = os.stat(file_path)

        if stat.S_ISDIR(file_stat.st_mode):
            print(color_map['dir'] + file_or_directory + colorama.Style.RESET_ALL)
        elif stat.S_ISREG(file_stat.st_mode) and file_or_directory.endswith('.py'):
            print(color_map['exec'] + file_or_directory + colorama.Style.RESET_ALL)
        else:
            print(color_map['file'] + file_or_directory + colorama.Style.RESET_ALL)





def cmd():
    cwd_path = color_map['dir'] + os.path.basename(default_dir) + colorama.Style.RESET_ALL
    print_welcome_message()
    current_dir = os.getcwd()
    while True:
        inp = input(f"{prompt + cwd_path}{color_map['file'] + colorama.Style.RESET_ALL}")
        if inp == 'help':
            print("""
                  
                  help : This Help Page

                  ver : Display Version

                  echo : Display the prompt

                  cf : Surprise

                  team : Credits

                  exit : Exit the Shell
                  
                  wms : Open the Webhook Message Sender for Discord

                  ip : Show your public IP Address

                  ls : show what's in the current directory

                  cd : change directory
                  
                  """)
        elif inp == 'ver':
            print("CF OS Version : Pre-Beta 0.0.1")
        elif inp == 'echo':
            printer = input("What to echo ? : ")
            times = int(input("How many times ? : "))
            for i in range(times):
                print(printer)
        elif inp == 'cf':
            surprise = random.choice(commands)
            print(f"Surprise = {surprise}")
        elif inp == 'team':
            print("Made by CFTREZAWD.")
        elif inp == '':
            pass
        elif inp == 'exit':
            exit_y_n = input("Do you wanna logout ? (y/n)")
            if exit_y_n == 'y':
                login()
            elif exit_y_n == 'n':
                pass
            else:
                print('Invalid Input')
        elif inp == 'wms':
            wms.wms()
            print("Opened WMS")
        elif inp == 'ip':
            ip = requests.get("https://api.ipify.org").text
            print(ip)
        elif inp == 'ls':
            ls()
        elif inp.startswith('cd'):
            os.chdir(inp[3])
        else:
            print("Wrong command, view 'help' for help.")