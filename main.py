import telebot
from telebot import types



TOKEN = '1222056736:AAGbrbh7iM7l72KFj_4_NbqOrbY9ZFPr7fw' # bot token from @BotFather

bot = telebot.TeleBot(TOKEN)









@bot.message_handler( commands=['start'])
def welcome(message):
    sti = open('Photo/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id,sti)

     # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🌭 Хот-дог")
    item2 = types.KeyboardButton("🍔 Гамбургер")
    item3 = types.KeyboardButton("🍟 Картопля Фрі")
    item4 = types.KeyboardButton("🍕 Піца")
    item5 = types.KeyboardButton("🥪 Сендвіч")
    item6 = types.KeyboardButton("🌮 Тако")
    item7 = types.KeyboardButton("☕ Кава")
    item8 = types.KeyboardButton("🍵 Чай")
    item9 = types.KeyboardButton("🍺 Пиво")



    markup.add(item1, item2,item3,item4,item5,item6,item7,item8,item9)

    bot.send_message(message.chat.id, "Добрий день!, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот для того щоб робити замовлення в фаст фуді".format(message.from_user, bot.get_me()),
        parse_mode='html',reply_markup=markup)

    bot.send_message(message.chat.id,"Ціни:  \n  🌭 Хот-дог=20грн.\n  🍔 Гамбургер=45грн.\n  🍟 Картопля Фрі=32грн.\n"
                                     "  🍕 Піца=25грн.\n  🥪 Сендвіч=16грн.\n  🌮 Тако=20грн.\n  ☕ Кава=12грн.\n  🍵 Чай=10грн\n  🍺 Пиво=27грн.")



words=["🌭 Хот-дог","🍔 Гамбургер","🍟 Картопля Фрі","🍕 Піца","🥪 Сендвіч","🌮 Тако","☕ Кава","🍵 Чай","🍺 Пиво"]

@bot.message_handler( commands=['замовити'])
def crsh(message):
     bot.send_message(message.chat.id,"Лол, красава")


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
         price=0

         if message.text == '🌭 Хот-дог':
             price+=20
             my_price = open("Ціна.txt", 'a')
             my_price.write(str(price)+" ")
             my_price.close()
             with open('Ціна.txt') as file:
                lst = list()
                for line in file.readlines():
                    str(lst.extend(line.rstrip().split( )))
             my_int=[]
             for item in lst:
                my_int.append(float(item))
             P_int=str(sum(my_int))
             bot.send_message(message.chat.id,P_int + " грн.")
         elif message.text == '🍔 Гамбургер':
             price+=45
             my_price = open("Ціна.txt", 'a')
             my_price.write(str(price)+" ")
             my_price.close()
             with open('Ціна.txt') as file:
                lst = list()
                for line in file.readlines():
                    str(lst.extend(line.rstrip().split( )))
             my_int=[]
             for item in lst:
                my_int.append(float(item))
             P_int=str(sum(my_int))
             bot.send_message(message.chat.id,P_int + " грн.")
         elif message.text == '🍟 Картопля Фрі':
             price+=32
             my_price = open("Ціна.txt", 'a')
             my_price.write(str(price)+" ")
             my_price.close()
             with open('Ціна.txt') as file:
                lst = list()
                for line in file.readlines():
                    str(lst.extend(line.rstrip().split( )))
             my_int=[]
             for item in lst:
                my_int.append(float(item))
             P_int=str(sum(my_int))
             bot.send_message(message.chat.id,P_int + " грн.")
         elif message.text == '🍕 Піца':
             price+=25
             my_price = open("Ціна.txt", 'a')
             my_price.write(str(price)+" ")
             my_price.close()
             with open('Ціна.txt') as file:
                lst = list()
                for line in file.readlines():
                    str(lst.extend(line.rstrip().split( )))
             my_int=[]
             for item in lst:
                my_int.append(float(item))
             P_int=str(sum(my_int))
             bot.send_message(message.chat.id,P_int + " грн.")
         elif message.text == '🥪 Сендвіч':
             price+=20
             my_price = open("Ціна.txt", 'a')
             my_price.write(str(price)+" ")
             my_price.close()
             with open('Ціна.txt') as file:
                lst = list()
                for line in file.readlines():
                    str(lst.extend(line.rstrip().split( )))
             my_int=[]
             for item in lst:
                my_int.append(float(item))
             P_int=str(sum(my_int))
             bot.send_message(message.chat.id,P_int + " грн.")
         elif message.text == '🌮 Тако':
             price+=20
             my_price = open("Ціна.txt", 'a')
             my_price.write(str(price)+" ")
             my_price.close()
             with open('Ціна.txt') as file:
                lst = list()
                for line in file.readlines():
                    str(lst.extend(line.rstrip().split( )))
             my_int=[]
             for item in lst:
                my_int.append(float(item))
             P_int=str(sum(my_int))
             bot.send_message(message.chat.id,P_int + " грн.")
         elif message.text == '☕ Кава':
             price+=12
             my_price = open("Ціна.txt", 'a')
             my_price.write(str(price)+" ")
             my_price.close()
             with open('Ціна.txt') as file:
                lst = list()
                for line in file.readlines():
                    str(lst.extend(line.rstrip().split( )))
             my_int=[]
             for item in lst:
                my_int.append(float(item))
             P_int=str(sum(my_int))
             bot.send_message(message.chat.id,P_int + " грн.")
         elif message.text == '🍺 Пиво':
             price+=27
             my_price = open("Ціна.txt", 'a')
             my_price.write(str(price)+" ")
             my_price.close()
             with open('Ціна.txt') as file:
                lst = list()
                for line in file.readlines():
                    str(lst.extend(line.rstrip().split( )))
             my_int=[]
             for item in lst:
                my_int.append(float(item))
             P_int=str(sum(my_int))
             bot.send_message(message.chat.id,P_int + " грн.")
         elif message.text == '🍵 Чай':
             price+=10
             my_price = open("Ціна.txt", 'a')
             my_price.write(str(price)+" ")
             my_price.close()
             with open('Ціна.txt') as file:
                lst = list()
                for line in file.readlines():
                    str(lst.extend(line.rstrip().split( )))
             my_int=[]
             for item in lst:
                my_int.append(float(item))
             P_int=str(sum(my_int))
             bot.send_message(message.chat.id,P_int + " грн.")
         else:
             bot.send_message(message.chat.id,"Я не знаю, що відповісти")






bot.polling(none_stop=True)






