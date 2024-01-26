import getpass
import time
import random
import requests
import wms
import os
import colorama
from config import color_map
import stat
import pytz
import log
import functools
import send2trash
from tqdm import tqdm
import sys



colorama.init()

wrong_inputs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']

timezone = pytz.timezone("Europe/Paris")

WELCOME_MESSAGE = colorama.Fore.YELLOW + "Welcome to CF-OShell! Type 'help' for a list of commands." + colorama.Style.RESET_ALL
def print_welcome_message():
    print(WELCOME_MESSAGE)

current_directory = os.getcwd()


ROOTUSERS = ['root']
USERS = {'root': 'root'}
COMMANDS = ['help', 'ver', 'team', 'exit', 'ip', 'wms', 'cd', 'ls', 'ren', 'rm', 'mk', 'open', 'whoami']

def login():
    username = input("Username: ")
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
    new_account = input("Do you want to create a new account? (y/n) ")
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
        elif stat.S_ISREG(file_stat.st_mode) and file_or_directory.endswith('.py' or '.go'):
            print(color_map['code'] + file_or_directory + colorama.Style.RESET_ALL)
        elif stat.S_ISREG(file_stat.st_mode) and file_or_directory.endswith('.exe'):
            print(color_map['exec'] + file_or_directory + colorama.Style.RESET_ALL)
        else:
            print(color_map['file'] + file_or_directory + colorama.Style.RESET_ALL)

def cmd(user):
    global current_directory
    global cwd_path
    print_welcome_message()
    cwd_path = f"{colorama.Fore.CYAN + os.path.basename(os.getcwd()) + colorama.Style.RESET_ALL}"
    prompt = f"{colorama.Fore.MAGENTA}CF-OShell {colorama.Fore.BLUE}{cwd_path}>{colorama.Style.RESET_ALL}"
    while True:
        inp = input(f"\n{prompt}")
        if inp == 'help':
            print("""
                 
                  help : This help page
                  ver : Display version
                  echo : Display the prompt
                  cf : Surprise
                  team : Credits
                  logout : Logout from the current account
                  wms : Open the Webhook Message Sender for Discord
                  ip : Show your public IP address
                  ls : Show what's in the current directory
                  cd : Change directory
                  open : Open a file
                  ren : Rename a file
                  rm : Remove a file
                  mk : Make a file
                  whoami : See the current User
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
        elif inp == 'logout':
            exit_yn = input("Do you want to logout? (y/n) ")
            if exit_yn == 'y':
                login()
            elif exit_yn == 'n':
                pass
            elif exit_yn in wrong_inputs:
                log.Logger.Error(errmessage = "Invalid input")
        elif inp == 'wms':
            try:
                wms.wms()
                log.Logger.info(infmessage = "Opened WMS")
            except Exception:
                log.Logger.Error(errmessage = "Failed to open WMS")
        elif inp == 'ip':
            ip = requests.get("https://api.ipify.org").text
            print(ip)
        elif inp == 'ls':
            ls()
        elif inp.startswith('cd '):
            directory = inp[3:].strip()
            if directory == '..':
                os.chdir('..')
                cwd_path = f"{colorama.Fore.CYAN + os.path.basename(os.getcwd()) + colorama.Style.RESET_ALL}"
                prompt = f"{colorama.Fore.MAGENTA}CF-OShell {colorama.Fore.BLUE}{cwd_path}>{colorama.Style.RESET_ALL}"
            elif directory == '~':
                os.chdir(os.path.expanduser('~'))
                cwd_path = f"{colorama.Fore.CYAN + os.path.basename(os.getcwd()) + colorama.Style.RESET_ALL}"
                prompt = f"{colorama.Fore.MAGENTA}CF-OShell {colorama.Fore.BLUE}{cwd_path}>{colorama.Style.RESET_ALL}"
            elif os.path.exists(directory):
                os.chdir(directory)
                cwd_path = f"{colorama.Fore.CYAN + os.path.basename(os.getcwd()) + colorama.Style.RESET_ALL}"
                prompt = f"{colorama.Fore.MAGENTA}CF-OShell {colorama.Fore.BLUE}{cwd_path}>{colorama.Style.RESET_ALL}"
            else:
                print(f"Error: Directory '{directory}' not found.")
                continue
            current_directory = os.getcwd()
            
            

            
            
        elif inp.startswith('open '):
            filename = inp[5:]
            for i in tqdm(range(random.randint(20, 100))):
                time.sleep(0.1)
            try:
                with open(filename) as f:
                    lines = f.read()
                    print('')
                    print(f"{colorama.Fore.BLUE}{lines}{colorama.Style.RESET_ALL}", end='')
                    print('')
            except FileNotFoundError:
                log.Logger.Error(errmessage = f"File {filename} wasn't found.")
            except PermissionError:
                log.Logger.Error(errmessage = f"You don't have the permission to open the file.")
            except Exception:
                log.Logger.Error(errmessage = f"Cannot opened File {filename}")
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
                    elif ren_yn in wrong_inputs:
                        log.Logger.Error(errmessage = f"Invalid Input")
                except FileNotFoundError:
                    log.Logger.Error(errmessage = f"File {file1} wasn't found.")
            elif user not in ROOTUSERS:
                log.Logger.warning(errmessage = f"User {user} isn't root.")
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
                        elif rmorsend in wrong_inputs:
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
            except Exception:
                log.Logger.Error(errmessage = f"Couldn't make the file {filetm}.")
        elif inp == 'whoami':
            log.Logger.info(infmessage = f"User : {user}")
        else:
            log.Logger.warning(warmessage = "Invalid Command : View 'help' to view all commands.")
