import requests 
import re 
from bs4 import BeautifulSoup
#print(dir(BeautifulSoup))
#token = '8673735646:AAEIuyPeDwZ3R5RFnxc1AV2R6AwWeBmzVwg'
#chat_id= '6634360090'
#def send_telegram(msg):
 #   telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"
  #  try:
        
   #     response = requests.post(
    #        telegram_url, data={"chat_id": chat_id, "text": msg}, timeout=10
        #)
     #   print("رد تليجرام:", response.json())
    #except Exception as e:
     #   print("💡 فشل الاتصال بتليجرام! السبب:")
      #  print(e)

targetPrice = 60.0
url='http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
geturl=requests.get(url)
soup= BeautifulSoup(geturl.text, "html.parser")
price=soup.find('p' , class_="price_color")
price_text=price.text
clean_price= re.findall(r"\d+\.\d+", price_text)[0]
fprice= float(clean_price)

if fprice <= targetPrice:
    msg=" the item is on sale "
    print(msg)
    #send_telegram(msg)
else:
    print("no updates ")
 

