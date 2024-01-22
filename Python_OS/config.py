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

prompt = f"{colorama.Fore.MAGENTA}CF-OShell>{colorama.Style.RESET_ALL}"



