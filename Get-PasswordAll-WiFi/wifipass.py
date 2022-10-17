import subprocess
from colorama import Fore
import os

os.system("cls")
print(Fore.RED+"""
 __   __ _          __  __      
 |  \/  | |__  _ __ \ \/ /_ __  
 | |\/| | '_ \| '_ \ \  /| '_ \ 
 | |  | | | | | | | |/  \| |_) |
 |_|  |_|_| |_|_| |_/_/\_\ .__/ 
                         |_|     version 2.0""")

print(Fore.RED+"""
------------------------------------------------------
|||           Developer: MahanXp              |||
|||           Contact: Tel: @MahanXp     |||               
------------------------------------------------------             
""")

print("--WelCome To My Tools--")
print()
print(Fore.LIGHTRED_EX+"[1]--Getting All Wi-Fi Passwords Connected To The System")
print()
print(Fore.LIGHTRED_EX+"[2]--LogOut")
print()
num = input("Enter The Number : ")
if num == "1":

    main = subprocess.run(
        ["netsh","wlan","show","profile","Irancell-TF-i60-423C_1","key=clear"], capture_output=True
    ).stdout.decode()

    one = main.find("Key Content")
    zero = main.find("Cost settings")

    finish = main[one:zero]

    file = open("pass.txt","w")
    file.write(finish)
    file.close()

    print("Done...")
else:
    exit
