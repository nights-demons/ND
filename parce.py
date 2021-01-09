import requests
from bs4 import BeautifulSoup
import time
def parce(ip):
	HEADER = { 
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
	}
	URL = 'https://iknowwhatyoudownload.com/ru/peer/?ip=' + ip
	response = requests.get(URL, headers = HEADER)
	soup = BeautifulSoup(response.content, 'html.parser')
	items = soup.select('.torrent_files')
	comps = []
	i = 0
	for item in items:
		i += 1
		true = True
		while true:
			global spisok
			spisok = list(item.getText()) 
			spisok.remove("\n")
			spisok.remove(" ")
			spisok.remove(" ")
			spisok.remove(" ")
			spisok.remove(" ")
			spisok.remove(" ")
			spisok.remove(" ")
			spisok.remove(" ")
			spisok.remove(" ")
			spisok.remove(" ")
			spisok.remove(" ")
			spisok.remove(" ")
			spisok.remove(" ")
			spisok.remove(" ")
			spisok.remove(" ")
			spisok.remove(" ")
			spisok.remove(" ")
			if spisok[0] == " ":
				print(spisok)
			else:
				break
		sp = ""
		for spisoks in spisok:
			sp += spisoks
		print("[TorrentName] " + sp)
		time.sleep(0.1)
		if i == 20:
			break
 ##https://iknowwhatyoudownload.com