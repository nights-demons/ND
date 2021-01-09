import sys, os, time
import requests
import random
import json
import platform

banner1 = '''
 _   _ _____
| \ | |  __ \                            
|  \| | |  | | ___ _ __ ___   ___  _ __  
| . ` | |  | |/ _ \ '_ ` _ \ / _ \| '_ \ 
| |\  | |__| |  __/ | | | | | (_) | | | |
|_| \_|_____/ \___|_| |_| |_|\___/|_| |_|

   Script by  ..:t.me/nights_demons:..

1 - Пробив номера        6 - Поиск по фото
2 - Пробив IP            7 - Torrent Tracker
3 - IP Logger            8 - NickName Search
4 - Geo Position Logger  9 - Search Auto (UA)
5 - Instagram Search     10 - Credits
0 - Exit
''' 

def clear_console():
	platforms = platform.system()
	if platforms == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
def clear_and_cls():
	platforms = platform.system()
	print()
	if platforms == 'Windows':
		os.system('cls')
	else:
		os.system('clear')

def say_exit():
	input("\n|: Что-бы выйти, нажмите Enter! :| ")
	clear_and_cls()

def get_number_info(number):
	response = requests.get("https://htmlweb.ru/geo/api.php?json&telcod=" + number)
	infoPhone = response.json()
	try:
		print(	"[Номер] +" + number )
		print(	"[Часть света] : " + infoPhone["country"]["location"] )
		print(  "[Страна] : " + infoPhone["country"]["name"] )
		print(  "[Регион] : " + infoPhone["region"]["name"] )
		print(  "[Округ] : " + infoPhone["region"]["okrug"] )
		print(  "[Оператор] : " + infoPhone["0"]["oper"] )
		
	except Exception as er:
		print(er)

def ipinfo(ip):
	response = requests.get( "https://ipinfo.io/" + ip + "/json" )
	r = response.json()	
	try:   
		print(	"[country] : " + r['country']	) 
		print(	"[region] : " + r['region']	)   
		print(	"[city] : " + r['city']	)  
		print(	"[hostname] : " + r['hostname']	)  
		print(	"[loc] : " + r['loc']	)   
		print(	"[org] : " + r['org']	)   
		print(	"[timezone] : " + r['timezone']	)  
		print(	"[postal] : " + r['postal']	)
	except Exception as er:
		print(er)

def iplogger(port):
	os.system("php -S localhost:" + port)

info_photo_search = '''

 | Привет Username!
 | Поиск по фото будет через теллеграмм бота.
 | Пробив будет работать через сервис FindClone - Бесплатно!!!
 | Подпишись на канал t.me/nights_demons что бы ничего не пропустить!
'''

def intro1():
	nd1 = list(""" 
 _   _ _____
| \ | |  __ \                            
|  \| | |  | | ___ _ __ ___   ___  _ __  
| . ` | |  | |/ _ \ '_ ` _ \ / _ \| '_ \ 
| |\  | |__| |  __/ | | | | | (_) | | | |
|_| \_|_____/ \___|_| |_| |_|\___/|_| |_|

WELCOME TO NIGHTS DEMONS t.me/nights_demons 
	""") 

	for i in range(len(nd1)):
		print(nd1[i], end='',flush=True)
		time.sleep(0.01)
	time.sleep(4)
def geo_logger():
	port = input("[PORT] : ")
	os.system("cd wwws && php -S localhost:" + str(port))

def linker():
	m = input("[Nick] : ")
	links = f"""
[*] Проверьте эти аккаунты:
[+] EyeEm:
https://www.eyeem.com/u/{m}
[+] HackerNews:
https://news.ycombinator.com/user?id={m}
[+] Instagram:
https://www.instagram.com/{m}
[+] ReverbNation:
https://www.reverbnation.com/{m}
[+] Tinder:
https://www.gotinder.com/@{m}
[+] VirusTotal: https://www.virustotal.com/ui/users/{m}/trusted_users
[+] Wattpad:
https://www.wattpad.com/user/{m}
[+] allmylinks:
https://allmylinks.com/{m}
[+] jeuxvideo:
http://www.jeuxvideo.com/profil/{m}?mode=infos
[+] Telegram:
http://www.t.me/{m}"""
	print(links)

def ukauto():
	num = input("[AutoNum] : ")
	req = requests.get("https://fakescreen-3d98a1.eu1.kinto.io/ua?num=" + num).json()
	digits = req['digits']
	vandor = req['vendor']
	region = req['region']['name']
	model = req['model']
	print(
	f'Номер: {digits}\n'								f'Марка: {vandor}\n'
	f'Модель: {model}\n'
	f'Регион: {region}')