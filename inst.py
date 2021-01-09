import requests 
import json
import random

nu = "\033[0m"
re = "\033[1;31m"
gr = "\033[0;32m"
cy = "\033[0;36m"
wh = "\033[0;37m"
ye = "\033[0;34m"

su = f"\033[1;31m[\033[1;36m+\033[1;31m]{nu}"
fa = f"\033[1;31m[\033[1;31m!\033[1;31m]{nu}"
er = f"\033[1;31m[\033[1;34m?\033[1;31m]{nu}"


useragent = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7']
def user_info(usrname):

	global total_uploads, is_private
	
	resp_js = get_page(usrname)
	js = json.loads(resp_js)
	js = js['graphql']['user']
	
	if js['is_private'] != False:
		is_private = True
	
	if js['edge_owner_to_timeline_media']['count'] > 12:
		pass
	else:
		total_uploads = js['edge_owner_to_timeline_media']['count']

	usrinfo = {
		'[username] : ': js['username'],
		'[user id] : ': js['id'],
		'[name] : ': js['full_name'],
		'[followers] : ': js['edge_followed_by']['count'],
		'[following] : ': js['edge_follow']['count'],
		'[posts img] : ': js['edge_owner_to_timeline_media']['count'],
		'[posts vid] : ': js['edge_felix_video_timeline']['count'],
		'[reels] : ': js['highlight_reel_count'],
		'[bio] : ': js['biography'].replace('\n', ', '),
		'[external url] : ': js['external_url'],
		'[private] : ': js['is_private'],
		'[verified] : ': js['is_verified'],
		'[business account] : ': js['is_business_account'],
		#'connected to fb': js['connected_fb_page'],  -- requires login
		'[joined recently] : ': js['is_joined_recently'],
		'[business category] : ': js['business_category_name'],
		'[category] : ': js['category_enum'],
		'[has guides] : ': js['has_guides'],
	}

	for key, val in usrinfo.items():
		print(key, val)


def get_page(usrname):
	global resp_js
	session = requests.session()
	session.headers = {'User-Agent': random.choice(useragent)}
	resp_js = session.get('https://www.instagram.com/'+usrname+'/?__a=1').text
	return resp_js
