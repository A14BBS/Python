import gc
import telebot
import time
from rss_parser import Parser
from requests import get
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hlink

BOT_TOKEN = '6354127090:AAHnCcqrPxNWr8Sz9jJPVNv3RhZ7Kr4G_Eg'

bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(commands=['start'])
def start(message: types.Message):
    #est
    rss_url_hm = "https://www.hm.ee/rss-feeds/rss.xml"
    rss_url_mkm = "https://mkm.ee/rss-feeds/rss.xml"
    rss_url_kaits = "https://www.kaitseliit.ee/et/rss-uudiste-voog"
    rss_url_tall = "https://tallinn.kaitseliit.ee/et/rss-uudiste-voog"
    rss_url_polv = "https://polva.kaitseliit.ee/et/rss-uudiste-voog"
    rss_url_tart = "https://tartu.kaitseliit.ee/et/rss-uudiste-voog"
    rss_url_voru = "https://vorumaa.kaitseliit.ee/et/rss-uudiste-voog"
    rss_url_atti = "https://attistibaipar.lv/feed/"
    rss_url_riig = "https://riigikantselei.ee/rss-feeds/rss.xml"
    rss_url_parn = "https://parnu.postimees.ee/rss"
    rss_url_saka = "https://sakala.postimees.ee/rss"
    rss_url_pohj = "https://pohjarannik.postimees.ee/rss"
    rss_url_kvak = "https://www.kvak.ee/feed/"
    rss_url_kait = "https://www.kaitseinvesteeringud.ee/feed/"
    rss_url_loun = "https://lounaeestlane.ee/rubriik/uudised/feed/"
    rss_url_peal = "https://pealinn.ee/feed/rss/"
    rss_url_kuul = "https://www.kuulutaja.ee/feed/"
    #rus
    rss_url_vm = "https://vm.ee/ru/rss-feeds/rss.xml"
    rss_url_just = "https://www.just.ee/ru/rss-feeds/rss.xml"
    rss_url_emta = "https://emta.ee/ru/rss-feeds/rss.xml"
    rss_url_sten = "https://www.stena.ee/rss.xml"
    rss_url_gran = "https://www.grani.lv/rss.xml"
    rss_url_goro = "https://gorod.ee/feed/"
    rss_url_prav = "https://pravo.by/novosti/novosti-pravo-by/rss/"
    rss_url_lsme = "https://www.lsm.lv/rss/?lang=lv&catid=14"
    rss_url_lsmr = "https://rus.lsm.lv/rss/" 
    rss_url_gorl = "https://www.gorod.lv/rss?"
    rss_url_mixn = "https://mixnews.lv/feed/"
    #lat
    rss_url_gral = "https://lat.grani.lv/rss.xml"
    rss_url_appo = "https://www.apollo.lv/rss"
    rss_url_tvne = "https://www.tvnet.lv/rss"


    tit = []
    while True:
        with open('base.txt', 'r', encoding="utf-8", errors='ignore') as filehandle:
                for line in filehandle:
                    currentPlace = line[:-1]
                    tit.append(currentPlace)
        filehandle.close()
        func_news_est(rss_url_hm, tit)
        func_news_est(rss_url_mkm, tit)
        func_news_est(rss_url_kaits, tit)
        func_news_est(rss_url_tall, tit)
        func_news_est(rss_url_polv, tit)
        func_news_est(rss_url_tart, tit)
        func_news_est(rss_url_voru, tit)
        func_news_est(rss_url_atti, tit)
        func_news_est(rss_url_riig, tit)
        func_news_est(rss_url_parn, tit)
        func_news_est(rss_url_saka, tit)
        func_news_est(rss_url_pohj, tit)
        func_news_est(rss_url_kvak, tit)
        func_news_est(rss_url_kait, tit)
        func_news_est(rss_url_loun, tit)
        func_news_est(rss_url_peal, tit)
        func_news_est(rss_url_kuul, tit)
        func_news_rus(rss_url_vm, tit)
        func_news_rus(rss_url_just, tit)
        func_news_rus(rss_url_emta, tit)
        func_news_rus(rss_url_sten, tit)
        func_news_rus(rss_url_gran, tit)
        func_news_rus(rss_url_goro, tit)
        func_news_rus(rss_url_prav, tit)
        func_news_rus(rss_url_lsme, tit)
        func_news_rus(rss_url_lsmr, tit)
        func_news_rus(rss_url_gorl, tit)
        func_news_rus(rss_url_mixn, tit)
        func_news_lat(rss_url_gral, tit)
        func_news_lat(rss_url_appo, tit)
        func_news_lat(rss_url_tvne, tit)
        
        

        gc.collect()
        time.sleep(30)

def func_news_est(rss_url, tit):
    xml = get(rss_url)

    parser = Parser(xml=xml.content, limit=5)
    feed = parser.parse()

    for item in reversed(feed.feed):
        if int(item.publish_date.split()[3]) > 2022:
              
            if not item.title in tit:
                tit.append(item.title)
                bot.send_message('-1001936682202',
                                    f'{hbold(item.publish_date)}\n\n{hlink(item.title, item.link)}\n\n')
    with open('base.txt', 'w', encoding="utf-8", errors='ignore') as filehandle:
        for listitem in tit:
            filehandle.write('%s\n' % listitem)
    filehandle.close()        
    time.sleep(10)

def func_news_rus(rss_url, tit):
    xml = get(rss_url)

    parser = Parser(xml=xml.content, limit=5)
    feed = parser.parse()

    for item in reversed(feed.feed):
        if int(item.publish_date.split()[3]) > 2022:
              
            if not item.title in tit:
                tit.append(item.title)
                bot.send_message('-1001936682202',
                                    f'{hbold(item.publish_date)}\n\n{hlink(item.title, item.link)}\n\n')
    with open('base.txt', 'w', encoding="utf-8", errors='ignore') as filehandle:
        for listitem in tit:
            filehandle.write('%s\n' % listitem)
    filehandle.close()        
    time.sleep(10)


def func_news_lat(rss_url, tit):
    xml = get(rss_url)

    parser = Parser(xml=xml.content, limit=5)
    feed = parser.parse()

    for item in reversed(feed.feed):
        if int(item.publish_date.split()[3]) > 2022:
              
            if not item.title in tit:
                tit.append(item.title)
                bot.send_message('-1001936682202',
                                    f'{hbold(item.publish_date)}\n\n{hlink(item.title, item.link)}\n\n')
    with open('base.txt', 'w', encoding="utf-8", errors='ignore') as filehandle:
        for listitem in tit:
            filehandle.write('%s\n' % listitem)
    filehandle.close()        
    time.sleep(10)
if __name__ == "__main__":
     
    bot.polling()

