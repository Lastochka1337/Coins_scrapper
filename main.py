from bs4 import BeautifulSoup
import requests
import lxml
from colored import fg

url = "https://coinmarketcap.com/currencies/dogecoin/"
request = requests.get(url)
content = request.text
soup = BeautifulSoup(content, "lxml")

res = soup.find('div', class_=["priceSection"])
if res is not None:
    price = res.find('div', class_=["priceValue"])
    title = res.find('div', class_=["priceTitle"])
    result = title.text.replace(price.text,'')
    up_down = title.find(class_ = "icon-Caret-down")
    if up_down is not None:
        result = "-"+result
        print(fg('red')+result)
    else:
        result = "+"+result
        print(fg('green')+result)
else:
    print("try again laiter")