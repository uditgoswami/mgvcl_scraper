
# coding: utf-8

# In[7]:

from bs4 import BeautifulSoup    
import requests
import os

filename= "mgvcl.csv"
f= open(filename,"w")

f.write("Consumer_No"+ "," +"Consumer_Name"+ "," +"Bill-Date"+ "," +"Bill_Amount"+ "," +"Payable_Amount\n")

f.close()

Loop= input('Enter no. of enteries to make: ')
Loop= int(Loop)

GetUrl="https://www.mgvcl.in:7013/PortalWeb/appmanager/LaunchPortal/LaunchDesktop?_nfpb=true&_windowLabel=portletInstance_55&_nffvid=%2FPortalWeb%2Fpages%2Fpayment%2FquickPay.jspx&_pageLabel=portal_homeportal_portal_page_5#wlp_portletInstance_55"

RGetUrl=requests.get(GetUrl)

S1= BeautifulSoup(RGetUrl.text, 'html.parser')

Tag1=S1.select('input[name="org.apache.myfaces.trinidad.faces.STATE"]')[0]['value']

Cookie=RGetUrl.headers['Set-Cookie'].split(";")[0]

for x in range(0, Loop) :   
        ConsumerNumber= input('Enter consumer number:  ')
        URL='https://www.mgvcl.in:7013/PortalWeb/appmanager/LaunchPortal/LaunchDesktop?_nfpb=true&_windowLabel=portletInstance_55&_nffvid=%2FPortalWeb%2Fpages%2Fpayment%2FquickPay.jspx&_pageLabel=portal_homeportal_portal_page_5'
        Data={"_id3:rangeStart": "0","_noJavaScript": "false","idCircleDivSubDivCode": "","idConsumerNo": ConsumerNumber,"org.apache.myfaces.trinidad.faces.FORM": "idForm","org.apache.myfaces.trinidad.faces.STATE": Tag1}
        Referer='https://www.mgvcl.in:7013'
        
        Head= {'Referer': Referer,'Cookie':Cookie}
        
        Rdata= requests.post(URL, data=Data,headers=Head)
        S2= BeautifulSoup(Rdata.text, 'html.parser')
        
        try :
            Name=S2.select('span[id="idConsumerName"]')[0].text
            
        except IndexError:
            print ('You Have entered a wrong Consumer Number.')
            os.system("pause")
            
        Date=S2.select('input[id="idBillMonthYear"]')[0]['value']
        Amount=S2.select('input[id="idAmount"]')[0]['value']
        Payment=S2.select('input[id="idPayment"]')[0]['value']
    
        print("Consumer Name : %s" % (Name))
        print("Bill Date : %s " % (Date))
        print("Bill Amount : %s " % (Amount))
        print("Payable Amount : %s \n\n" % (Payment))
    
    
        append= open(filename, "a")
        append.write(ConsumerNumber + "," + Name.replace(",","") + "," + Date + "," + Amount.replace(",","")+ "," + Payment.replace(",","") + "\n")
        append.close()
 
os.system("pause")


# In[ ]:



