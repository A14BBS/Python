import telebot
import time
from rss_parser import Parser
from requests import get
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hlink

BOT_TOKEN = '...'

bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(commands=['start'])
def start(message: types.Message):
    rss_url_B = "..."
    rss_url_G = "..."
    rss_url_R = "..." 

    tit = []
    while True:
        with open('base.txt', 'r', encoding="utf-8", errors='ignore') as filehandle:
                for line in filehandle:
                    currentPlace = line[:-1]
                    tit.append(currentPlace)
        filehandle.close()
        b = (func_news(rss_url_B, tit))
        g = (func_news(rss_url_G, tit))
        r = (func_news_1(rss_url_R, tit))


        tit.extend(b)
        tit.extend(g)
        tit.extend(r)

        tit1 = list(set(tit))

        with open('base.txt', 'w', encoding="utf-8", errors='ignore') as filehandle:
                for listitem in tit1:
                    filehandle.write('%s\n' % listitem)
        filehandle.close()

def func_news(rss_url, tit):
    xml = get(rss_url)

    parser = Parser(xml=xml.content, limit=5)
    feed = parser.parse()

    for item in reversed(feed.feed):
        if int(item.publish_date.split()[3]) > 2022:
              
            if not item.title in tit:
                tit.append(item.title)
                bot.send_message('-1001882321146',
                                    f'{hbold(item.publish_date)}\n\n{hlink(item.title, item.link)}\n\n')
            # print(item.publish_date)
        time.sleep(10)
    return tit
def func_news_1(rss_url, tit):
    xml = get(rss_url)

    parser = Parser(xml=xml.content, limit=5)
    feed = parser.parse()

    for item in reversed(feed.feed):
        if int(item.publish_date.split()[3]) > 2022:

            if not item.title in tit:
                tit.append(item.title)
                bot.send_message('-1001866349606',
                                       f'{hbold(item.publish_date)}\n\n{hlink(item.title, item.link)}\n\n')
                # print(item.publish_date)

    # await asyncio.sleep(100)
    return tit


if __name__ == "__main__":
     
    bot.polling()

