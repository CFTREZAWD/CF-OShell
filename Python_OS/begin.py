import time
from CF_OShell import prompt
import CF_OShell

def boot():
    CF_OShell.print_welcome_message()
    print("Booting...")

if __name__ == "__main__":
    boot()
    time.sleep(0.5)
    print("Booted !")
    time.sleep(0.2)
    CF_OShell.login()