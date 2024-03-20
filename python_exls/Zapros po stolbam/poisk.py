import pandas as pd
import telebot
import config

bot = telebot.TeleBot(config.token)

sales = pd.read_excel("C:/tit/tit_test2.xlsx",  header = 0) #переменная которая читает фаил который лежит по этому адресу
df = pd.DataFrame(sales) #перевод в формат DataFrame это двумерная структура данных, представляющая собой таблицу с метками для строк и столбцов. 
df = df.astype(str)# перевел все столбцы в строки 

@bot.message_handler(commands=['start','help']) #бот запускается с комнады старт и команды хелп
def handle_start(message):
    bot.reply_to(message, 'Имя')
    
@bot.message_handler(func=lambda message: True)#ставим эту строчку когда хотим обработать все текстовые сообщения от пользователя
def handle_message(message):
    poisk = message.text# переменная в которой полученный текст
    viborka = df.loc[df['Имя']==poisk]#вывожу всю строку в которой в столбце "Имя" совпадет с введенным мной в переменную список
    print(viborka)
    writer = pd.ExcelWriter('res.xlsx') #создаем Excel Writer

    viborka.to_excel(writer) # написать фрейм данных в лист Excel 
    writer.close()#сохранить файл Excel
    with open( 'C:\\Users\\Web\\python_exls\\Zapros po stolbam\\res.xlsx', 'rb') as f1:# откр фаил(rb-только чтение) и принимаем его как обьект пер.f1
        bot.send_document(message.chat.id, f1)

if __name__ == "__main__":                        
     bot.polling()      
    
   


#sales = pd.read_excel("C:/tit/tit_test2.xlsx",  header = 0) #переменная которая читает фаил который лежит по этому адресу
# df = pd.DataFrame(sales) #перевод в формат DataFrame это двумерная структура данных, представляющая собой таблицу с метками для строк и столбцов. 
# poisk = input('')# ввожу имя
# df.loc[df['Имя']==poisk]#вывожу всю строку в которой в столбце "Имя" совпадет с введенным мной в переменную список
# if __name__ == "__main__":                        
#bot.polling()
 
  
#@bot.message_handler(content_types=['text'])  #реагирует на любые сообщения
