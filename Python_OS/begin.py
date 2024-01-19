import time


def main():
    print("Welcome to CF OS, thank you for installing. We will try to help you the best as we can.")
    time.sleep(3)
    print("Booting...")





if __name__ == "__main__":
    main()
    time.sleep(5)
    print("Booted !")
    time.sleep(0.2)
    exec(open('cf.py').read())