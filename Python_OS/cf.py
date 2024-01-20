import getpass
import time
import random
import requests
import wms
from os import listdir, system
import os

usrd = {'root': 'root'}
commands = ['help', 'ver', 'team', 'exit', 'ip', 'wms']

def login():
    usrname = input("Username : ").lower()
    if usrname in usrd:
        passw = getpass.getpass(prompt = "Password : ").lower()
        if passw == usrd[usrname]:
            print(f"Welcome back, {usrname} !")
            cmd()
        else:
            print(f"Wrong password for {usrname}")
            time.sleep(5)
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

def cmd():
    while True:
        inp = input("CF-OShell>")
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
                
        
        else:
            print("Wrong command, view 'help' for help.")

