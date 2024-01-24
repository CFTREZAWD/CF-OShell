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
import log
import functools
import send2trash

colorama.init()

wrong_inputs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']

timezone = pytz.timezone("Europe/Paris")

WELCOME_MESSAGE = colorama.Fore.YELLOW + "Welcome to CF-OShell! Type 'help' for a list of commands." + colorama.Style.RESET_ALL
def print_welcome_message():
    print(WELCOME_MESSAGE)

current_directory = os.getcwd()


ROOTUSERS = ['root']
USERS = {'root': 'root'}
COMMANDS = ['help', 'ver', 'team', 'exit', 'ip', 'wms', 'cd', 'ls', 'ren', 'rm', 'mk']

def login():
    username = input("Username: ").lower()
    if username in USERS:
        password = getpass.getpass(prompt = "Password: ").lower()
        if password == USERS[username]:
            print(f"Welcome back, {username}!")
            cmd(username)
        elif password == '':
            log.Logger.Error(errmessage = "No Password")
            login()
        elif password != USERS[username]:
            log.Logger.Error(errmessage = "Wrong Password")
            login()
    else:
        newuser(username)


def newuser(username):
    global USERS # Declare USERS as a global variable
    new_account = input("Do you want to create a new account? (y/n) ").lower()
    if new_account == 'y':
        is_root = input("Is the User Root ? (y/n) : ")
        password = getpass.getpass(prompt = "New Password: ").lower()
        USERS[username] = password
        if is_root == 'y':
            ROOTUSERS.append(username)
        elif is_root == 'n':
            pass
        elif is_root or new_account in wrong_inputs:
            log.Logger.Error(errmessage = "Invalid input")
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

def cmd(user):
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
                  rm : Remove a file
                  mk : Make a file
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
            print("Made by CFTREZAWD")
        elif inp == '':
            pass
        elif inp == 'exit':
            exit_yn = input("Do you want to logout? (y/n) ")
            if exit_yn == 'y':
                login()
            elif exit_yn == 'n':
                pass
            else:
                log.Logger.Error(errmessage = "Invalid input")
        elif inp == 'wms':
            wms.wms()
            log.Logger.info(infmessage = "Opened WMS")
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
                log.Logger.Error(errmessage = f"File {filename} wasn't found.")
            except Exception:
                log.Logger.Error(errmessage = f"cannot opened File {filename}")
        elif inp.startswith('ren '):
            if user in ROOTUSERS:    
                try:
                    file1 = inp[3:].strip()
                    newname = input(f'Enter a new name for "{file1}" : ')
                    ren_yn = input(f"Are you sure you want to rename {file1} to {newname} ? (y/n) : ")
                    if ren_yn == 'y':
                        os.rename(file1, newname)
                        log.Logger.info(infmessage = f"Renamed {file1} to {newname}")
                    elif ren_yn == 'n':
                        pass
                    else:
                        log.Logger.Error(errmessage = f"Invalid Input")
                except FileNotFoundError:
                    log.Logger.Error(errmessage = f"File {file1} wasn't found.")
            elif user not in ROOTUSERS:
                log.Logger.warning(errmessage = f"User {user} isn't root.")
        elif inp == 'date':
            date = datetime.now(timezone)
            print(date)
        elif inp.startswith('rm '):
            if user in ROOTUSERS:
                try:
                    filetd = inp[3:]
                    rm_yn = input(f"Are you sure you want to delete/send to trash {filetd} ? (y/n) : ")
                    if rm_yn == 'y':
                        rmorsend = input("Remove or Send to Trash ? (rm/st) : ")
                        if rmorsend == 'rm':
                            os.remove(filetd)
                            log.Logger.info(infmessage = f"File {filetd} Removed.")
                        elif rmorsend == 'st':
                            send2trash.send2trash(filetd)
                            log.Logger.info(infmessage = f"File {filetd} sended to trash.")
                        elif rmorsend == wrong_inputs:
                            log.Logger.Warning(errmessage= "Wrong Input ! :)")
                    elif rm_yn == 'n':
                        pass
                    else:
                        log.Logger.Error(errmessage = f"Invalid input")
                except FileNotFoundError:
                    log.Logger.Error(errmessage = f"File {filetd} wasn't found.")
                except PermissionError:
                    log.Logger.Error(errmessage = "Access Denied ! (It's surely a important file or Directory)")
            elif user not in ROOTUSERS:
                log.Logger.warning(warmessage = f"User {user} isn't Root.")
        elif inp.startswith('mk '):
            try:
                filetm = inp[3:]
                aystm = input(f"Are you sure you want to make {filetm} ? (y/n) : ")
                if aystm == 'y':
                    with open(filetm, 'w') as f:
                        log.Logger.info(infmessage = f"Maked {filetm}.")
                elif aystm == 'n':
                    pass
                else:
                    log.Logger.Error(errmessage = "Invalid Input")
            except Exception as e:
                log.Logger.Error(errmessage = f"Couldn't make the file {filetm}.")
        elif inp == 'whoami':
            log.Logger.info(infmessage = f"User : {user}")
        else:
            log.Logger.warning(warmessage = "Invalid Command : View 'help' to view all commands.")
