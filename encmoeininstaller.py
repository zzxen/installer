import os
import time
import requests


print("THIS IS INSTALLER FOR MOEIN SOCKET SERVICE ENCRYPTION.../ && wait 3 seconds")
time.sleep(3)

print("I WILL CHANGE VMESS PANEL FOR ENCRYPT.../")

def install():
    panel_and_encryption = "https://github.com/proxykingdev2/x-ui-with-moein-encryption-protocol.git"
    command1 = "apt update -y && apt full-upgrade && git clone {}".format(panel_and_encryption)
    command2 = "chmod +x xen && ./x-ui-with-moein-encryption-protocol/xen"

    os.system(command1)
    time.sleep(2)
    os.system(command2)

    ip_get = requests.get("https://api.ipify.org").text
    print("Paste in your browser : http://{}:443".format(ip_get))
    os.system("rm -rf install")

confirm = input("HINT ENTER TO INSTALL ALL THINGS : ")

if confirm == "":
    print("Pay attantion : After 10 seconds script will be start to install\n1.Please use 443 port for panel\n2.encryption convert with './install' script\n3.Moein-Encryption install with this installer\nGood luck from MOEIN")
    time.sleep(10)
    install()

else:
    exit()
