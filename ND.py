import sys, os, time
import requests
import random
import json
from probiv import *
from inst import *
import platform
from parce import parce
clear_console()
intro1()
clear_console()
while True:
	print(banner1)
	function = input("[!] : ")
	if function == '1':
		number = input('[N] : +')
		get_number_info(number)
		say_exit()
	elif function == '2':
		ip = input("[IP] : ")
		ipinfo(ip)
		say_exit()
	elif function == '3':
		pass
	elif function == '4':
		pass
	elif function == '5':
		username = input("[username] : ")
		get_page(username)
		user_info(username)
		say_exit()
	elif function == '6':
		print(info_photo_search)
		say_exit()
	elif function == '7':
		ip = input("[IP] : ")
		parce(ip)
	elif function == '8':
		linker()
		say_exit()
	elif function == '9':
		ukauto()
		say_exit()
	elif function == '0':
		sys.exit()
	else:
		clear_console()