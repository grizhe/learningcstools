
#!/usr/bin/python
#thank you for using my program :D
#import sequence
from socket import *
from termcolor import colored
import optparse
from threading import *
#welcome message:)
print(colored(".\n.\n.\n\t\t\tWelcome to griz's advanced PortScanner!\n.\n.\n.", "cyan"))
#main function: parser = options, tgtHost = 'target host'
def main():
	parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest ='tgtPort', type='string', help='specify target ports seperated by comma')
	(options, args)= parser.parse_args())
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if(tgtHos == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)
	#portScan(tgtHost,tgtPorts)'

main()
