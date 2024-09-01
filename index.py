#cre : HuongDev
#zalo : 0362166863
import threading,base64
import os,time,re,json,random
from datetime import datetime, timedelta
from time import sleep,strftime
from bs4 import BeautifulSoup
import requests
import os, sys
import socket

try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
  import socks
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  os.system("pip3 install requests pysocks")
  print('__Vui Lòng Chạy Lại Tool__')
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"

def banner():
 banner = f"""
\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Facebook\033[1;31m : \033[1;97mi.urs.bin.python.TrinhHuong 
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/+77MuosyD-yk4MGY1🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.000001)
def bes4(url):
    # Gửi yêu cầu GET đến URL
    response = requests.get(url)
    
    # Nếu yêu cầu thành công (status code 200)
    if response.status_code == 200:
        # Phân tích nội dung HTML của trang web
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Tìm thẻ <span> chứa thông tin phiên bản và trạng thái bảo trì
        version_tag = soup.find('span', id='version3')
        maintenance_tag = soup.find('span', id='maintenance3')
        
        # Lấy nội dung văn bản bên trong thẻ
        version = version_tag.text.strip() if version_tag else None
        maintenance = maintenance_tag.text.strip() if maintenance_tag else None
        
        return version, maintenance
    
    return None, None

def checkver():
    url = 'https://huongdz.hotrommo.com/'
    version, maintenance = bes4(url)
    
    if maintenance == 'on':
        print("Tool đang được bảo trì. Vui lòng thử lại sau. \nHoặc vào nhóm Tele: https://t.me/+77MuosyD-yk4MGY1")
        sys.exit()
    
    return version

# Sử dụng hàm checkver để kiểm tra phiên bản
current_version = checkver()
if current_version:
  
    print(f"Phiên bản hiện tại: {current_version}")
else:
    print("Không thể lấy thông tin phiên bản hoặc tool đang được bảo trì.")
# Hàm để lấy địa chỉ IP của thiết bị
def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except:
        return None

# Hàm để hiển thị địa chỉ IP của thiết bị
def display_ip_address(ip_address):
    if ip_address:
        banner = """
\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool   \033[1;31m  : \033[1;97m☞ \033[1;31mTool Gộp Vip♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Facebook\033[1;31m : \033[1;97mi.urs.bin.python.TrinhHuong 
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/+77MuosyD-yk4MGY1🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜
"""

        os.system('cls' if os.name == 'nt' else 'clear')
        for x in banner:
            print(x, end="")
            time.sleep(0.001)

        print(f"\033[1;32mĐịa chỉ IP : {ip_address}     Version: {current_version}")
    else:
        print("Không thể lấy địa chỉ IP của thiết bị.")

# Hàm để lưu thông tin IP và key vào tệp tin JSON
def luu_thong_tin_ip(ip, key, expiration_date):
    data = {}
    try:
        with open('ip_key.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        pass

    # Lưu key cho IP vào trong dữ liệu
    data[ip] = {'key': key, 'expiration_date': expiration_date.isoformat()}

    # Lưu lại vào tệp tin
    with open('ip_key.json', 'w') as file:
        json.dump(data, file)

# Hàm để kiểm tra xem IP đã sử dụng key chưa và key còn hạn hay không
def kiem_tra_ip(ip):
    try:
        with open('ip_key.json', 'r') as file:
            data = json.load(file)
            if ip in data:
                expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
                if expiration_date > datetime.now():
                    return data[ip]['key']
            return None
    except (FileNotFoundError, KeyError, TypeError):
        return None

# Hàm để tạo key và URL mới dựa trên IP hiện tại
def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    
    # Xử lý địa chỉ IP để chỉ lấy các số
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
        
    key = f'huongdev{key1}{ip_numbers}'
    # Thời gian hết hạn là 23:59:00 hôm nay
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://huongdev.com/?key={key}'
    return url, key, expiration_date

# Hàm để kiểm tra xem đã qua 00:00:01 của ngày mới chưa
def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    start_new_day = midnight + timedelta(seconds=1)
    return now >= start_new_day

# Chương trình chính
# Chương trình chính
def main():
    # Lấy và hiển thị địa chỉ IP của thiết bị
    ip_address = get_ip_address()
    display_ip_address(ip_address)

    # Kiểm tra và tạo link rút gọn để vượt key cho từng địa chỉ IP
    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"\033[1;35mTool còn hạn, mời bạn dùng tool. ")
            sleep(2)
        else:
            url, key, expiration_date = generate_key_and_url(ip_address)
            token_8link = '8c72127ca7e74ebd4b963be7d3cc9f75f4ddd4ead4ee121d9b6ba28a4dfa991b'
            link8_response = requests.get(f'https://partner.8link.io/api/public/gen-shorten-link?apikey={token_8link}&format=json&url={url}&target_domain=https://8link.io')

            # Kiểm tra kết quả trả về từ link rút gọn
            print("\033[1;31mLưu Ý: \033[1;33mKey Free Nên Mỗi Ngày Sẽ Thay Đổi Một Key")
            if link8_response.status_code == 200:
                link8_data = link8_response.json()
                if link8_data.get('status') == "error":
                    print(link8_data.get('message'))
                    quit()
                else:
                    link_key = link8_data.get('shortened_url')
                    token_yeumoney = 'f7e85811bc83948a0a66e121fa312afc03472eabd86a53c4bc9ec86662a480c8'
                    yeumoney_response = requests.get(f'https://yeumoney.com/QL_api.php?token={token_yeumoney}&format=json&url={link_key}')
                    if yeumoney_response.status_code == 200:
                        yeumoney_data = yeumoney_response.json()
                        if yeumoney_data.get('status') == "error":
                            print(yeumoney_data.get('message'))
                            quit()
                        else:
                            link_key = yeumoney_data.get('shortenedUrl')
                            print('Link Để Vượt Key Là:', link_key)  # Sử dụng dấu phẩy thay vì dấu cộng
                    else:
                        print('Không thể kết nối đến dịch vụ rút gọn URL')
                        quit()
            else:
                print('Không thể kết nối đến dịch vụ rút gọn URL')
                quit()

            # Yêu cầu người dùng nhập key
            while True:
                keynhap = input('Key Đã Vượt Là: ')

                # Kiểm tra key nhập vào với key được tạo ra từ IP hiện tại
                if keynhap == key:
                    print('Key Đúng Mời Bạn Dùng Tool')
                    sleep(2)
                    luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                    break
                else:
                    print('Key Sai Vui Lòng Vượt Lại Link:', link_key)
        
        # Kiểm tra nếu đã qua 00:00:01 của ngày mới
        if da_qua_gio_moi():
            print("Key của bạn đã hết hạn. Đợi 2 giây để lấy key mới từ ngày mới...")
            time.sleep(2)
            main()  # Gọi lại main() để lấy key mới từ ngày mới

if __name__ == "__main__":
    main()
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	banner()
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Auto Golike    \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1 \033[1;97m: \033[1;34mTool Auto TikTok \033[1;32m[Online] \033[1;32m[Termux]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2 \033[1;97m: \033[1;34mTool Auto TikTok Tự Động \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3 \033[1;97m: \033[1;34mTool Auto Instagram \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4 \033[1;97m: \033[1;34mTool Auto Twitter \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m5 \033[1;97m: \033[1;34mTool Auto Youtube \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m6 \033[1;97m: \033[1;34mTool Auto Thread \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m7 \033[1;97m: \033[1;34mTool Auto Linkedin \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Tương Tác Chéo \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m8 \033[1;97m: \033[1;34mTool TTC Facebook \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m9 \033[1;97m: \033[1;34mTool TTC Pro5 \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m10 \033[1;97m: \033[1;34mTool TTC Pro5v1 \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m11 \033[1;97m: \033[1;34mTool TTC TikTok \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m12 \033[1;97m: \033[1;34mTool TTC Instagram \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool TraoDoiSub.com \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m13 \033[1;97m: \033[1;34mTool TDS Facebook \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m14 \033[1;97m: \033[1;34mTool TDS Pro5 \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m15 \033[1;97m: \033[1;34mTool TDS Pro5v1 \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m16 \033[1;97m: \033[1;34mTool TDS TikTok \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m17 \033[1;97m: \033[1;34mTool TDS Instagram \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[97m════════════════════════════════════════════════════════")
	chon = input('\033[1;91m┌─╼\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Nhập lựa chọn \033[1;97m \n\033[1;91m└─╼\033[1;91m✈ \033[1;33m : ')
	print('\033[1;39m─────────────────────────────────────────────────────────── ')
	if chon == '1':
		# Thành Công
		exec(requests.get('https://run.mocky.io/v3/e94b0a54-9967-4e12-8cfa-4d69eec9006e').text)
	elif chon == '2':
		exec(requests.get('https://run.mocky.io/v3/fe073faf-cd0d-4ad7-b58c-9d0298e1a08e').text)
	elif chon == '3':
		exec(requests.get('https://run.mocky.io/v3/64823ca1-2088-4833-927d-f7cf22a83d67').text)
	elif chon == '4':
		exec(requests.get('https://run.mocky.io/v3/5d2abfca-51c4-439a-b9e4-9db8117bfa74').text)
	elif chon == '5':
		exec(requests.get('https://run.mocky.io/v3/105c9754-1de0-4138-8d9a-9112edbc6260').text)
	elif chon == '6':
		exec(requests.get('https://run.mocky.io/v3/00a757b8-bc97-4a21-82be-0814bf9f8794').text)
	elif chon == '7':
		exec(requests.get('https://run.mocky.io/v3/56bf2b14-f99c-4daf-a3dd-08666f4a9278').text)
		# TTC
	elif chon == '8':
		exec(requests.get('https://run.mocky.io/v3/229a274b-0066-41de-b9cb-9676830fa544').text)
	elif chon == '9':
		exec(requests.get('https://run.mocky.io/v3/a2df263e-7605-4137-95e3-e5a6be6141fc').text)
	elif chon == '10':
		exec(requests.get('https://run.mocky.io/v3/0f75fe3c-6673-4ab9-bd29-ba0ad6e3d9db').text)
	elif chon == '11':
		exec(requests.get('https://run.mocky.io/v3/17c7e994-5448-4c3d-af5f-6cacc1685fe1').text)
	elif chon == '12':
		exec(requests.get('https://run.mocky.io/v3/02fffba1-0ddc-4738-ba2d-b2c4e68c58f4').text)
		# TDS
	elif chon == '13':
		# Thanh Công
		exec(requests.get('https://run.mocky.io/v3/229a274b-0066-41de-b9cb-9676830fa544').text)
	elif chon == '14':
		# Thanh Công
		exec(requests.get('https://run.mocky.io/v3/2b37a119-9e65-4456-b88e-3a1a0ffb4553').text)
	elif chon == '15':
		# Thanh Công
		exec(requests.get('https://run.mocky.io/v3/2cf9909e-49e5-441f-a328-e633a5a170ac').text)
	elif chon == '16':
		# Thanh Công
		exec(requests.get('https://run.mocky.io/v3/77f21c9f-d763-4261-92ed-b339553bb99d').text)
	elif chon == '17':
		# Thanh Công
		exec(requests.get('https://run.mocky.io/v3/d8a33356-044e-444f-bc08-2ebb948632ee').text)	
	else:
		sys.exit("")