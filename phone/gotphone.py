import telebot
import gc
bot = telebot.TeleBot('5312788439:AAEkOv2wggJmXMveCEN9mA5dVoaTfLxjs1w')
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message,'Грузи')


@bot.message_handler(func=lambda message: True)
def handler_message(messadge):
    gruz = messadge.text# переменная в которой храниться текст от пользователя
    Korob = gruz.split('\n')#разделяет переносом строки 
    
    ii = ''
    for i in range(len(Korob)):#переменную i в ней сейчас число (строк из переменной злист) перебирает массив переменной Korob
        Korob[i] = Korob[i].split('-')
        price = Korob[i][1]
        name = Korob[i][0]
        price = price.replace('.','')
        f = ''
        
        for i in price[::-1]:
            if i == '0':
                break
            f = i + f
        perv = price#цена и флаг 
        vtor = f#флаг
        price = ([x for x in perv if x not in set(vtor)])
        price = str(price)
        price = price.replace('[','').replace(']','').replace("'",'').replace(',','').replace(' ','')
        price = int(price)
        if price >= 68000:
            price = price + 1500
        elif price <= 68000:
            price = price + 500
        price = str(price)
        price = list(price)
        price.insert(-3, ".")
        price = list(price)
        price = str(price)
        price = price.replace('[','').replace(']','').replace("'",'').replace(',','').replace(' ','')
        itog = (name + ('-') + price + f)
        ii = f'{ii} {itog}\n'
        
        
      
    bot.send_message('-1002041269074', ii)
        

bot.polling(none_stop=True, interval=0)        
 