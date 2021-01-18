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
		print("[TorrentName] " + item.getText().strip())
		time.sleep(0.1)
		if i == 30:
			break
 ##https://iknowwhatyoudownload.com
