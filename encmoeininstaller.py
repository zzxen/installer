import os
import time
import requests


print("THIS IS INSTALLER FOR MOEIN SOCKET SERVICE ENCRYPTION.../ && wait 3 seconds")
time.sleep(3)

panel_link = "wget --no-check-certificate -O install https://raw.githubusercontent.com/proxykingdev/x-ui/master/install"

print("I WILL CHANGE VMESS PANEL FOR ENCRYPT.../")

def install():
    commands = f"sudo apt update -y && sudo apt full-upgrade && sudo apt install wget && sudo {panel_link} && sudo chmod +x install && sudo ./install"
    os.system(commands)
    ip_get = requests.get("https://api.ipify.org").text
    print("Paste in your browser : http://{}:443".format(ip_get))
    os.system("rm -rf install")
    exit()

confirm = input("HINT ENTER TO INSTALL ALL THINGS : ")



if confirm == "":
    print("Pay attantion : After 10 seconds script will be start to install\n1.Please use 443 port for panel\n2.encryption convert with './install' script\n3.Moein-Encryption install with this installer\nGood luck from MOEIN")
    time.sleep(10)
    install()

else:
    exit()