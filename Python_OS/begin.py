import time
from CF_OShell import prompt
import CF_OShell

def boot():
    print("Welcome to CF-OShell. The worst shell ever created ! ")
    time.sleep(0.5)
    print("Booting...")

if __name__ == "__main__":
    boot()
    time.sleep(5)
    print("Booted !")
    time.sleep(2)
    CF_OShell.login()