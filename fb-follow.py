from datetime import datetime
from threading import Thread
import time,os,sys
try:
	import requests
except :
	os.system('pip install requests')
	import requests

dem = 1
list_id = []

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
	banner_logo = """
 \033[1;37m Owner : \033[1;31mBT-TOOL    \033[1;37mCOPPYRIGHT : \033[1;31mSMM MASTER BT
\033[1;34m╔════════════════════════════════════════════════════╗
\033[1;32m     ███╗   ███╗██╗███╗   ██╗██╗  ██╗                ║    
\033[1;31m     ████╗ ████║██║████╗  ██║██║  ██║                ║
\033[1;35m     ██╔████╔██║██║██╔██╗ ██║███████║                ║
\033[1;34m     ██║╚██╔╝██║██║██║╚██╗██║██╔══██║                ║
\033[1;36m     ██║ ╚═╝ ██║██║██║ ╚████║██║  ██║                ║
\033[1;32m     ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝                ║ 
\033[1;31m  VERSION : 0.1                                      ║
\033[1;35m  SUPPORT : @Master_TG_K                             ║
\033[1;34m  COPYRIGHT : SMM MASTER                             ║
\033[1;36m  TITLE TOOL : SOUCRE TOOL FOLLOW FACEBOOK           ║
\033[1;34m╚════════════════════════════════════════════════════╝
\033[1;35m
	"""
	for i in banner_logo:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.00001)
	print(" ",end='\n')
banner()	
cookie = input('COOKIE : ')
id_cookie = cookie.split('c_user=')[1].split(';')[0]
id = input('ID : ')
headers = {
	'cookie': cookie
}
print("In progress Check Live Cookie...", end="\n")
clear()
try:
	find_data = requests.get("https://m.facebook.com/", headers=headers).text
	fb_dtsg = find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
	jazoest = find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
	clear()
	print("Check Live Cookie SUCCESS", end="\n")
except:
	print(f"Cookie {cookie} Die Please Check Again!!!")
	quit()
clear()

data = {
	'fb_dtsg': fb_dtsg,
	'jazoest': jazoest,
	'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
	'doc_id': '5300338636681652'
	}
getidpro5 = requests.post('https://www.facebook.com/api/graphql/', headers = headers, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
for i in getidpro5:
	id_profile = i['profile']['id']
	list_id.append(id_profile)
print(f'ID : {id_cookie} || PAGE : {len(list_id)} PAGE')

so_luong = int(input('NUMBER OF FOLLOWS WANT TO INCREASE: '))
clear()
def follow(id,fb_dtsg,jazoest,cookie,id_profile):
	headers={
		'cookie': f'{cookie} i_user={id_profile} ; ',
		'referer': f'https://www.facebook.com/{id}',
		'sec-ch-prefers-color-scheme': 'light',
		'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
		'sec-ch-ua-full-version-list': '"Not_A Brand";v="99.0.0.0", "Google Chrome";v="109.0.5414.132", "Chromium";v="109.0.5414.132"',
		'sec-ch-ua-platform-version': '"6.0"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
		'x-asbd-id': '198387',
		'x-fb-friendly-name': 'CometUserFollowMutation',
		'x-fb-lsd': '5nDN0iDMb5DJf99P-N7bcm',
		'Connection': 'keep-alive'
	}
	data = {
		'fb_dtsg': fb_dtsg,
		'jazoest': jazoest,
		'fb_api_caller_class': 'RelayModern',
		'fb_api_req_friendly_name': 'CometUserFollowMutation',
		'variables': f'{{"input":{{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1683671356267,923207,190055527696468,","is_tracking_encrypted":false,"subscribe_location":"PROFILE","subscribee_id":"{id}","tracking":null,"actor_id":"100037533160611","client_mutation_id":"3"}}, "scale":1}}',
		'server_timestamps': 'true',
		'doc_id': '6808144429201900'
	}
	buff_follow = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
	print(f'{datetime.now().strftime("%H:%M:%S")} :MASTERBT :{id_profile}')
for id_profile in list_id:
	Thread(target=follow,args=(id,fb_dtsg,jazoest,cookie,id_profile)).start()
	time.sleep(3)
	dem += 1
	if dem == so_luong:
		print('COMPLETE ! ');break;quit()
	else:
		continue