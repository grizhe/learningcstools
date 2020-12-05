
#!/usr/bin/python

import socket
from termcolor import colored, cprint
#input reads
inp = input("Please enter the IP Adress of the Target: ")
inprange = input("How many ports would you like scanned?: ")
#defines that we're looking for the ports
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)
#host assignment
host = str(inp)
#closed dictionary
closedports = []
#portscanner if statements
def portscanner(port):
        if sock.connect_ex((host,port)):
                closedports.append(port)
        else:
                print(colored("Port %d is open" % (port), 'green'))
#port range assignment
for port in range(1, int(inprange)):
	portscanner(port)
#questionare
print("Thank you for using grizhe's portscanner.")
question = input("Would you like a list of all of the closed ports?[y/n]")
while True:
        if str(question) == 'y':
                print(colored(closedports, 'red'))
                break
        elif str(question) == 'n':
                print(colored("Okay, I hope this was helpful!", 'magenta'))
                break
        else:
                print(colored("Invalid Syntax, try again.", 'red'))
                print(colored("Answer with, [y] (for yes), or [n] (for no).", 'red'))
 
