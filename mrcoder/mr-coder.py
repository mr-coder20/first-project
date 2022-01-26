import requests
from bs4 import BeautifulSoup
from os import system
import hashlib
import socket















def clear_console():
    system('cls')
def menu():
    print("\n")
    print("     ■■■■■■■■■■-MR-CoDe-■■■■■■■■■■■■■■■■\n          Hi Dear Glad you are here\n     ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("1= Price of anything              2= Weather\n3= hash anything                  4= dycript hash\n5= time & date                    6= my Ip\n")
    print("     ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n          ↓please enter number↓ ")   
def one():
    print("     ■■■■■■■■■■-MR-CoDe-■■■■■■■■■■■■■■■■\n          Hi Dear Glad you are here\n     ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("7= dollar-euro-pond             8= gold\n9= coin                         10= Digital currency\n")
    print("     ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n          ↓please enter number↓ ")
def myip():
    fqn = os.uname()[1]
    ext_ip = urllib2.urlopen('http://whatismyip.org').read()
    print ("Asset: %s " % fqn, "Checking in from IP#: %s " % ext_ip)
menu()
num=input("                     ")


if num=="1":
    clear_console()
    one()
    num=input("                     ")
    clear_console()
    if num=="7":
        dollar=requests.get("https://www.tgju.org/profile/price_dollar_rl")
        euro=requests.get("https://www.tgju.org/profile/price_eur")
        pond=requests.get("https://www.tgju.org/profile/price_gbp")
        soup1=BeautifulSoup(dollar.text,"html.parser")
        soup2=BeautifulSoup(euro.text,"html.parser")
        soup3=BeautifulSoup(pond.text,"html.parser")
        dollar=soup1.find('td',attrs={'class':'text-left'})
        euro=soup2.find('td',attrs={'class':'text-left'})
        pond=soup3.find('td',attrs={'class':'text-left'})
        print("dollar to rial= ",dollar.text,"      ","\n""euro to rial=   ",euro.text,"      ","\n""pond to rial=   ",pond.text,"      ","\n")
    if num=="8":
        gold=requests.get("https://www.tgju.org/profile/geram18")
        soup4=BeautifulSoup(gold.text,"html.parser")
        gold=soup4.find('td',attrs={'class':'text-left'})
        print("gold to rial= ",gold.text)
    if num=="9":
        coin=requests.get("https://www.tgju.org/profile/retail_sekeb")
        soup5=BeautifulSoup(coin.text,"html.parser")
        coin=soup5.find('td',attrs={'class':'text-left'})
        print("coin to rial= ",coin.text)
    if num=="10":
        bitcoin=requests.get("https://www.tgju.org/profile/crypto-bitcoin")
        ethereum=requests.get("https://www.tgju.org/profile/crypto-ethereum")
        soup6=BeautifulSoup(bitcoin.text,"html.parser")
        soup7=BeautifulSoup(ethereum.text,"html.parser")
        bitcoin=soup6.find('td',attrs={'class':'text-left'})
        ethereum=soup7.find('td',attrs={'class':'text-left'})
        print("bitcoin to dollar= ",bitcoin.text,"\n""ethereum to dollar= ",ethereum.text,"\n")

if num=="2":
    
    clear_console()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    def weather(city):
        city = city.replace(" ", "+")
        res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
        print("Searching...\n")
        soup = BeautifulSoup(res.text, 'html.parser')
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()
        print(location)
        print(weather+"°C")
    city = input("Enter the Name of City=  ")
    city = city+" weather"
    weather(city)
    print("Have a Nice Day:)")
    
if num=="3":
    print("\n","\n""11= hash by md5 algoritm   or   12= hash by sha256 algoritm""\n""\n")
    num=input("                     ")
    if num=="11":
        hasH=input("please enter world for hash md5= ")
        hasH=hashlib.md5(hasH.encode())
        print(hasH.hexdigest())
    if num=="12":
        hasH=input("please enter world for hash sha256= ")
        hasH=hashlib.sha256(hasH.encode())
        print(hasH.hexdigest())

if num=="4":
       
    print("\n","\n""13= un hash by md5 algoritm   or   14= un hash by sha256 algoritm""\n""\n")
    num=input("                     ")
    if num=="13":
        
        unhash=input("please enter hash for crack (md5 algoritm)= ")
        for i in range(0,999999999999):
            cunt=i
            i=str(i)
            i=hashlib.md5(i.encode()).hexdigest()
            if i==unhash:
                print("crack hash seccess and your code=",cunt)
                break
                cunt+=1
            if cunt==1000000000000:
                print("i cant crack code (out of the range)")
    if num=="14":
        
        unhash=input("please enter hash for crack (sha256 algoritm)= ")
        for i in range(0,999999999999):
            cunt=i
            i=str(i)
            i=hashlib.sha256(i.encode()).hexdigest()
            if i==unhash:
                print("crack hash seccess and your code=",cunt)
                break
                cunt+=1
            if cunt==1000000000000:
                print("i cant crack code (out of the range)")
                
if num=="5":
    clear_console()
    time= requests.get("https://www.timeanddate.com/worldclock/iran/tehran")
    soup8=BeautifulSoup(time.text,"html.parser")
    time1=soup8.find('span',attrs={'id':'ct'})
    time2=soup8.find('span',attrs={'id':'ctdat'})
    print("time=",time1.text,"\n""date=",time2.text) 
    
if num=="6":
    clear_console()
    ip =requests.get('https://api.ipify.org').content.decode('utf8')   
    print('My public IP address is: {}'.format(ip))

    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    #▀                                                                                        ▀
    #▀                        MR-coder   ■■■■    id telegram= yalan_donya_0                   ▀
    #▀                                                                                        ▀
    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                            