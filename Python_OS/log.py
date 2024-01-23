import colorama

colorama.init()


class Logger:
    def __init__(self):
        super().__init__
        pass

    def info(infmessage):
        print(f"{colorama.Fore.GREEN}INFO ||{colorama.Style.RESET_ALL} {infmessage} {colorama.Fore.GREEN}|| {colorama.Style.RESET_ALL}")

    def warning(warmessage):
        print(f"{colorama.Fore.YELLOW}WARNING ||{colorama.Style.RESET_ALL} {warmessage} {colorama.Fore.YELLOW}|| {colorama.Style.RESET_ALL}")
    
    def Error(errmessage):
        print(f"{colorama.Fore.RED}ERROR ||{colorama.Style.RESET_ALL} {errmessage} {colorama.Fore.RED}|| {colorama.Style.RESET_ALL}")