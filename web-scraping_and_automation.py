import requests
from bs4 import BeautifulSoup
import smtplib
import time
import socket
socket.getaddrinfo('localhost', 8080)

URL = "https://www.amazon.com/Bandai-S-H-Figuarts-Kamen-Rider-Ohma/dp/B07V2Y1HWD/ref=sr_1_fkmr1_1?keywords=shf+ohma+zio&qid=1578849548&sr=8-1-fkmr1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers = headers)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id = "productTitle")
    price = soup2.find(id = "priceblock_ourprice")
    title_item = title.get_text()
    price_item = price.get_text()
    conv_price = float(price_item[1:6])

    if(conv_price < 130):
        send_email()  
        
    if(conv_price > 130):
        send_email()  

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('mathfordummiesid@gmail.com', 'lcazoforivzogrft')
    
    subject = 'Harga turun, ayo cek email sekarang!'
    body = 'cek link nya gannnn -> https://www.amazon.com/Bandai-S-H-Figuarts-Kamen-Rider-Ohma/dp/B07V2Y1HWD/ref=sr_1_fkmr1_1?keywords=shf+ohma+zio&qid=1578849548&sr=8-1-fkmr1'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail('mathfordummiesid@gmail.com', 'zefanyaaprilia@gmail.com', msg)
    
    print("Email udah dikirim bos")
    
    server.quit()

while(True):    
    check_price()
    time.sleep(360)





