import getpass
import time
import random
import requests
import wms
import os
import colorama
from config import color_map, prompt
import stat
from datetime import datetime
import pytz

colorama.init()

timezone = pytz.timezone("Europe/Paris")

WELCOME_MESSAGE = colorama.Fore.YELLOW + "Welcome to CF-OShell! Type 'help' for a list of commands." + colorama.Style.RESET_ALL
def print_welcome_message():
    print(WELCOME_MESSAGE)

current_directory = os.getcwd()

USERS = {'root': 'root'}
COMMANDS = ['help', 'ver', 'team', 'exit', 'ip', 'wms', 'cd', 'ls', 'ren']

def login():
    username = input("Username: ").lower()
    if username in USERS:
        password = getpass.getpass(prompt = "Password: ").lower()
        if password == USERS[username]:
            print(f"Welcome back, {username}!")
            cmd()
        else:
            print(f"Wrong password for {username}")
            login()
    else:
        newuser(username)

def newuser(username):
    global USERS # Declare USERS as a global variable
    new_account = input("Do you want to create a new account? (y/n) ").lower()
    if new_account == 'y':
        password = getpass.getpass(prompt = "New Password: ").lower()
        USERS[username] = password
        login()
    else:
        login()

def ls():
    global current_directory
    files_and_dirs = os.listdir(current_directory)

    for file_or_directory in files_and_dirs:
        file_path = os.path.join(current_directory, file_or_directory)
        file_stat = os.stat(file_path)

        if stat.S_ISDIR(file_stat.st_mode):
            print(color_map['dir'] + file_or_directory + colorama.Style.RESET_ALL)
        elif stat.S_ISREG(file_stat.st_mode) and file_or_directory.endswith('.py'):
            print(color_map['code'] + file_or_directory + colorama.Style.RESET_ALL)
        elif stat.S_ISREG(file_stat.st_mode) and file_or_directory.endswith('.exe'):
            print(color_map['exec'] + file_or_directory + colorama.Style.RESET_ALL)
        else:
            print(color_map['file'] + file_or_directory + colorama.Style.RESET_ALL)

def cmd():
    global current_directory
    cwd_path = colorama.Fore.CYAN + os.path.basename(os.getcwd()) + colorama.Style.RESET_ALL
    print_welcome_message()
    while True:
        inp = input(f"\n{prompt} {cwd_path}{colorama.Fore.BLUE}${colorama.Style.RESET_ALL} ")
        if inp == 'help':
            print("""
                 
                  help : This help page
                  ver : Display version
                  echo : Display the prompt
                  cf : Surprise
                  team : Credits
                  exit : Exit the shell
                  wms : Open the Webhook Message Sender for Discord
                  ip : Show your public IP address
                  ls : Show what's in the current directory
                  cd : Change directory
                  open : Open a file
                  ren : Rename a file
                  """)
        elif inp == 'ver':
            print("CF OS Version: Pre-Beta 0.0.1")
        elif inp == 'echo':
            printer = input("What to echo? : ")
            times = int(input("How many times? : "))
            for i in range(times):
                print(printer)
        elif inp == 'cf':
            surprise = random.choice(COMMANDS)
            print(f"Surprise = {surprise}")
        elif inp == 'team':
            print("Made by CFTREZAWD.")
        elif inp == '':
            pass
        elif inp == 'exit':
            exit_yn = input("Do you want to logout? (y/n) ")
            if exit_yn == 'y':
                login()
            elif exit_yn == 'n':
                pass
            else:
                print("Invalid input")
        elif inp == 'wms':
            wms.wms()
            print("Opened WMS")
        elif inp == 'ip':
            ip = requests.get("https://api.ipify.org").text
            print(ip)
        elif inp == 'ls':
            ls()
        elif inp.startswith('cd '):
            directory = inp[3:].strip()
            if directory == '..':
                os.chdir('..')
            elif directory == '~':
                os.chdir(os.path.expanduser('~'))
            elif os.path.exists(directory):
                os.chdir(directory)
            else:
                print(f"Error: Directory '{directory}' not found.")
                continue

            current_directory = os.getcwd()
            # Update the cwd_path variable after changing the current directory
            cwd_path = colorama.Fore.CYAN + os.path.basename(os.getcwd()) + colorama.Style.RESET_ALL
            
        elif inp.startswith('open '):
            filename = inp[5:]
            try:
                with open(filename) as f:
                    lines = f.read()
                    for i, line in enumerate(lines):
                        print(line, end='')
            except FileNotFoundError:
                print(f"The file {filename} was not found.")
            except Exception:
                print(f"Cannot Open the File : {filename}")
        elif inp.startswith('ren '):
            try:
                file1 = inp[3:].strip()
                newname = input(f'Enter a new name for "{file1}" : ')
                ren_yn = input(f"Are you sure you want to rename {file1} to {newname} ? (y/n) : ")
                if ren_yn == 'y':
                    os.rename(file1, newname)
                elif ren_yn == 'n':
                    pass
                else:
                    print("invalid Input")
            except FileNotFoundError:
                print(f'File {file1} not found.')
        elif inp == 'date':
            date = datetime.now(timezone)
            print(date)
        elif inp.startswith('rm '):
            try:
                filetd = inp[3:]
                rm_yn = input(f"Are you sure you want to delete {filetd} ? (y/n) : ")
                if rm_yn == 'y':
                    os.remove(filetd)
                    print(f"Removed {filetd}")
                elif rm_yn == 'n':
                    pass
                else:
                    print("Invalid Input")
            except FileNotFoundError:
                print("File not found.")
        elif inp.startswith('mk '):
            try:
                filetm = inp[3:]
                aystm = input(f"Are you sure you want to make {filetm} ? (y/n) : ")
                if aystm == 'y':
                    with open(filetm, 'w') as f:
                        print(f"Maked {filetm}.")
                elif aystm == 'n':
                    print("Canceled operation")
                else:
                    print("Invalid Input")
            except Exception as e:
                print(f"Error while making the file : {e}")
        else:
            print("Wrong command, view 'help' for help.")
