import time
import CF_OShell
from tqdm import tqdm

def boot():
    print("Welcome to CF-OShell. The worst shell ever created ! ")
    for i in tqdm(range(100)):
        time.sleep(0.1)

if __name__ == "__main__":
    boot()
    time.sleep(5)
    print("Booted !")
    time.sleep(2)
    CF_OShell.login()
