import requests
import telebot
import time
import gc
import requests as r
from bs4 import BeautifulSoup as bs
import telebot
from telebot import types
from translate import Translator
from fake_useragent import FakeUserAgent

ua = FakeUserAgent().random
headers = {
    'user-agent': ua
}

bot = telebot.TeleBot('tokken')

@bot.message_handler(commands=['start'])
def start(message: types.Message):
    https_url_Sait = 'https://www._____/lenta' 

    tit = []  
    while True:  
        with open('base.txt', 'r', encoding="utf-8",
                  errors='ignore') as filehandle:  
            for line in filehandle:  
                currentPlace = line[:-1]  
                tit.append(currentPlace)  
        filehandle.close() 
        f_n_news(https_url_Sait,tit)
        gc.collect() 
        time.sleep(150)  

def send_message(old_text):  
    translator = Translator(from_lang='en', to_lang='ru')  
    text = translator.translate(old_text)  
    return text
def f_n_news(https_url, tit):  
    r = requests.get(https_url)  
    soup = bs(r.text, "html.parser")  
    vacancies_names = soup.find_all('a', class_='newsitem news_item_title')
    for name in vacancies_names:  
        x = f'www._____.com{name.a["href"]}'
        if not x in tit:  
            y = send_message(' '.join(name.text.split()))
            tit.append(x)  
            bot.send_message('-1000040000070', f'{x} {y}' )  
    with open('base.txt', 'w', encoding="utf-8",
              errors='ignore') as filehandle:  
        for listitem in tit:  
            filehandle.write('%s\n' % listitem)  
    filehandle.close()  
    print(https_url) 

if __name__ == "__main__": 
    bot.polling() 