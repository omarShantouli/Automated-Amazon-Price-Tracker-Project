from bs4 import BeautifulSoup
import requests
import os

url = "https://www.amazon.com/Aluminum-Ergonomic-Adjustable-Notebook-Compatible/dp/B08JD7FN44/ref=sr_1_5?keywords=laptop+stand&qid=1660475398&sprefix=laptop%2Caps%2C740&sr=8-5"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
"Accept-Language" : "en-US,en;q=0.9",
}
response = requests.get(url= url, headers= headers)

soup = BeautifulSoup(response.text, 'html.parser')
price = int(soup.find(name= "span", class_= "a-price-whole").getText().split('.')[0])
if price < 30:
    BOT_KEY = os.environ["BOT_KEY"]
    CHAT_ID = os.environ["CHAT_ID"]
    msg = f"The laptop stand became cheaper, its price became below your target (less than 30$), its price now is {price}$. By now!"
    response = requests.get(url=f"https://api.telegram.org/bot{BOT_KEY}/sendMessage?chat_id={CHAT_ID}&text={msg}")