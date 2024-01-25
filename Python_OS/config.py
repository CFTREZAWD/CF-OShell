import colorama
import os
import CF_OShell as cf

colorama.init()

color_map = {
        'dir': colorama.Fore.GREEN,
        'code': colorama.Fore.BLUE,
        'file': colorama.Fore.RED,
        'exec': colorama.Fore.MAGENTA
    }

cwd_path = colorama.Fore.CYAN + os.getcwd() + colorama.Style.RESET_ALL
prompt = f"{colorama.Fore.MAGENTA}CF-OShell {colorama.Fore.BLUE}{cwd_path}>{colorama.Style.RESET_ALL}"



