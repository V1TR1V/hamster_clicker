import pyautogui
import time
import os


class colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    PURPLE = "\033[35m"


print(f""" {colors.PURPLE}
 _   _    _    __  __ ____ _____ _____ ____  
| | | |  / \  |  \/  / ___|_   _| ____|  _ \ 
| |_| | / _ \ | |\/| \___ \ | | |  _| | |_) |
|  _  |/ ___ \| |  | |___) || | | |___|  _ < 
|_| |_/_/   \_\_|  |_|____/ |_| |_____|_| \_\  {colors.RESET}
  {colors.RED}                                          
  ____ _     ___ ____ _  _______ ____  
 / ___| |   |_ _/ ___| |/ / ____|  _ \ 
| |   | |    | | |   | ' /|  _| | |_) |
| |___| |___ | | |___| . \| |___|  _ < 
 \____|_____|___\____|_|\_\_____|_| \_\                                    
	"""+colors.RESET)


def clear():
	os.system("clear")
while True:
	try:
		while True:
			
			a = int(input(colors.YELLOW+"enter how many clicks: "+colors.RESET))
			
			def main(n):
				for i in range (n):
					pyautogui.click()
				clear()
				print(str(colors.CYAN+f"done {a} clicks!"+colors.RESET))

			main(a)

	except ValueError:
		clear()
		print(colors.RED+"print only integer!"+colors.RESET)
