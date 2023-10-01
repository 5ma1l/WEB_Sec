import sys
from methods import SQLi,path
if __name__=='__main__':
    try :
        url=sys.argv[1].strip()
        lab4=SQLi(url,path)
        c=lab4.type_columns
        if c!=[]:
            print("[+] Columns Type : ",c)
            print("\n".join(lab4.payloads["type of columns"]))

        else:
            print("[-] Failed to detect ... ")
    except IndexError:
        print(f"[-] usage {sys.argv[0]} <url> ")
        print(f'[-]python3 {sys.argv[0]} "https://0aa20014036eae28832434fd00b60028.web-security-academy.net"')