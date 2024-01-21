import colorama
import os
import CF_OShell as cf

colorama.init()

color_map = {
        'dir': colorama.Fore.GREEN,
        'exec': colorama.Fore.BLUE,
        'file': colorama.Fore.RED
    }

prompt = f"CF-OShell {os.getcwd()}>"



default_dir = "C:\\Users\\"

