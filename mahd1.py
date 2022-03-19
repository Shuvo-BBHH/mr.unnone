#!/usr/bin/python3
#-*-coding:utf-8-*-
# Update V1.6

### Import Module
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,platform,base64
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote


### Perumpamaan Module & Syntax
_req_ses_  = requests.Session()
_req_get_  = requests.get
_req_post_ = requests.post
_js_lo_    = json.loads
_cici_azimvau_    = input
_azimvau_dapunta_ = open
_cici_cici_       = exit

### Warna
Z = "\033[1;30m" # Hitam
P = "\033[1;37m" # Putih
M = "\033[1;31m" # Merah
H = "\033[1;32m" # Hijau
K = "\033[1;33m" # Kuning
B = "\033[1;34m" # Biru
U = "\033[1;35m" # Ungu
O = "\033[1;36m" # Biru Muda
N = "\033[0m"    # Warna Mati

### Host & Penampungan
host = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []
count = 1
data_1 = {}
data_2 = {}
data_change_1 = {}
data_change_2 = {}
data_user = []
header_grup = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
header_nama = {"origin": "https://mbasic.facebook.com","accept-language": "en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7","accept-encoding": "gzip, deflate","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent": "Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Host": "".join(bs4.re.findall("://(.*?)$","https://m.facebook.com")),"referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","cache-control": "max-age=0","upgrade-insecure-requests": "1","content-type": "application/x-www-form-urlencoded"}
header_hashtag = {'authority': 'mbasic.facebook.com','method': 'GET','path': '/favicon.ico','scheme': 'https','accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8','accept-encoding': 'gzip, deflate','accept-language': 'en-US,en;q=0.9','user-agent': 'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com'}

r = str(random.randint(1,9999))
rx = r.replace("1","A").replace("2","C").replace("3","B").replace("4","E").replace("5","H").replace("6","I").replace("7","Y")
plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'N').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', 'R').replace("5","X").replace("1","X")

try:
    rq = requests.get('https://github.com/Shuvo-BBHH/paid/blob/main/mahdi.txt').text
except requests.exceptions.ConnectionError:
    print('\nNO INTERNET CONNECTION\n')
    exit()
    ### Waktu & Tanggal
__sekarang__ = datetime.now()
__tahun__ = __sekarang__.year
__bulan__ = __sekarang__.month
__hari__  = __sekarang__.day

bulan_ttl = {"01": "JAN", "02": "FEB", "03": "MAR", "04": "APR", "05": "MAY", "06": "JUN", "07": "JUL", "08": "AUG", "09": "SEP", "10": "OCT", "11": "NOV", "12": "DEC"}
_list_bulan_ = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

try:
    if __bulan__ < 0 or __bulan__ > 12:
        _cici_cici_()
    _bulan_sekarang_ = __bulan__ - 1
except ValueError:
    _cici_cici_()
_bulan_ = _list_bulan_[_bulan_sekarang_]
tanggal = ("%s-%s-%s"%(__hari__,_bulan_,__tahun__))

_my_account_ = [
    '100045203855294','100014839270205']

### User Agent
ua_intelmac = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36;]'
ua_nokia   = 'Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20'
ua_asus    = 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)/CLDC-1.1;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAZ-AL10; HMSCore 5.3.0.312; GMSCore 20.39.15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.1.0.302 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]' #DONE
ua_vivo    = 'Mozilla/5.0 (Linux; Android 10; V2027) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 4.1.1; X909 Build/JRO03L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.92 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9515 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36;]'
ua_windows = 'Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.7.8) Gecko/20050511 Firefox/1.0.4;]'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 11; Mi 9T Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.80 Mobile Safari/537.36 Reddit/Version 2021.38.0/Build 365032/Android 11 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]'
### Clear Login Session
def bersih():
    try:os.remove('token.txt')
    except:pass
    try:os.remove('cookies.txt')
    except:pass

### Display Text
def jalan(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)


### Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")

### Logo
def banner():
        os.system("clear")
        os.system('echo "\n\33[93m███╗   ███╗ █████╗ ██╗  ██╗██████╗ ██╗    \n\033[91m████╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m      \n         ╔═════════════════════════════╗\n         ║ TOOL NAME: { CRACK-PRO }    ║\n         ║ AUTHOR   : MAHDI       ║\n         ║ GITHUB   : Shuvo-BBHH       ║\n         ║ Bikash/cont;01887408882     ║\n         ╚═════════════════════════════╝" | lolcat -a -d 2 -s 50')
        print("")
        
def cek_dev():
    _isi_dev_ = _azimvau_dapunta_('cookies.txt','r').read()
    if 'null' in _isi_dev_:jalan('%s [%s!%s] %INVALID COOKIES, RE-LOGIN WITH COOKIES'%(M,P,M,P));bersih();_cici_cici_()
    else:pass

