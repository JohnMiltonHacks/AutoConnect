import time
import os,urllib.request,time,schedule
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False
#Script by tx.me/l_J0hnMilt0n_l | 4AllFreeModApks.blogspot.com
#This Script will automatically connect to particular wifi at particular time.
t="connect"   

def run():
    while(True):
        time.sleep(2)
        print("Checking Internet Connectivity...")
        if time.localtime().tm_hour==6:
                    os.system("shutdown /s -t 5")
        if(not connect()):
            print("Network status: Not Connected")
            try:
                print("Trying to ",t)
                os.system(f'''cmd /c "netsh wlan connect J0h1Milt01"''')
                #os.system(f'''"""netsh interface ipv4 set address name="Wi-Fi" static 192.168.126.1 255.255.255.0 192.168.126.48"""''')
                os.system(f'''"""netsh interface teredo set state disabled
                netsh interface ipv6 6to4 set state state=disabled undoonstop=disabled
                netsh interface ipv6 isatap set state state=disabled"""''')
            except:
                pass
        time.sleep(2)
        if(connect()==True):
            print("Network status: Connected")
            time.sleep(10)
        else:
            print("Failed To ",t)
            os.system(f'''cmd /c "netsh interface set interface name="Wi-Fi" admin=DISABLED"''')
            time.sleep(5)
            os.system(f'''cmd /c "netsh interface set interface name="Wi-Fi" admin=ENABLED"''')
            
schedule.every().day.at("00:02").do(run)
while True:
    schedule.run_pending()
    time.sleep(30)
