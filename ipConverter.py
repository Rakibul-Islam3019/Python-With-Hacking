#Domain to Ip converter
import socket
import pyfiglet
from termcolor import colored

print(colored("*************** Domain To IP Converter ***************",'green'))

print(colored("*************** Create By Rakibul Islam ***************",'red'))

design = colored(pyfiglet.figlet_format("Domain To Ip Converter"),'yellow')
print(design)
domain_name = input("Enter your targated domain :")

ip = socket.gethostbyname(domain_name)

print("IP For {} : {}".format(domain_name,ip))