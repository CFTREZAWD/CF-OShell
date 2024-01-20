import time
import cf


def boot():
    print("Welcome to CF OS, thank you for installing. We will try to help you the best as we can.")
    time.sleep(3)
    print("Booting...")





if __name__ == "__main__":
    boot()
    time.sleep(5)
    print("Booted !")
    time.sleep(0.2)
    cf.login()