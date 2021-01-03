import telebot
import config
from string import Template
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):
    menufooter = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Меню")
    menufooter.add(item1)
    bot.send_message(message.chat.id,"Добро пожаловать, {0.first_name}!\nЯ - <b>🤖Бот обменник</b>, созданный чтобы быстро менять тебе криптовалюту.🚀💸".format(message.from_user, bot.get_me()),parse_mode="html", reply_markup=menufooter)

@bot.message_handler(content_types=["text"])

def spam(message):
    if message.text == 'stop0793090900':
        bot.send_message(message.chat.id, reply_markup=a)
        a = types.InlineKeyboardMarkup(row_width=2)

    elif message.text == 'Меню':
        mainmenu = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("💵Обменять", callback_data="Обменять")
        item2 = types.InlineKeyboardButton("💹Обменный курс", callback_data="Обменный курс")
        item3 = types.InlineKeyboardButton("⚖️Баланс бота", callback_data="Баланс бота")
        item4 = types.InlineKeyboardButton("⁉️Частые вопросы", callback_data="Частые вопросы")
        item5 = types.InlineKeyboardButton("⚠️Оператор", url="https://t.me/MDobmen")
        item6 = types.InlineKeyboardButton("👌Отзывы", url="https://t.me/MDobmen_review")
        item7 = types.InlineKeyboardButton("🎲Рулетка", callback_data="Рулетка")
        mainmenu.row(item1)
        mainmenu.add(item2, item3, item4, item5)
        mainmenu.row(item6)
        mainmenu.row(item7)
        pic = "https://i.ibb.co/dgkfZ98/photo-2020-12-29-08-38-19.jpg"
        bot.send_photo(message.chat.id, pic)
        bot.send_message(message.chat.id,"Добро пожаловать, {0.first_name}!\nЯ - <b>🤖Бот обменник</b>, созданный чтобы быстро менять тебе криптовалюту.🚀💸".format(message.from_user, bot.get_me()),parse_mode="html", reply_markup=mainmenu)

    else:
        error = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Назад", callback_data="Меню")
        error.add(item1)
        bot.send_message(message.chat.id, "Прости, я не знаю эту команду. Нажми кнопку ниже чтобы вернуться в главное меню.", reply_markup=error)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
        #Main menu
            if call.data == 'Меню':
                mainmenu = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("💵Обменять", callback_data="Обменять")
                item2 = types.InlineKeyboardButton("💹Обменный курс", callback_data="Обменный курс")
                item3 = types.InlineKeyboardButton("⚖️Баланс бота", callback_data="Баланс бота")
                item4 = types.InlineKeyboardButton("⁉️Частые вопросы", callback_data="Частые вопросы")
                item5 = types.InlineKeyboardButton("⚠️Оператор", url="https://t.me/MDobmen")
                item6 = types.InlineKeyboardButton("👌Отзывы", url="https://t.me/MDobmen_review")
                item7 = types.InlineKeyboardButton("🎲Рулетка", callback_data="Рулетка")
                mainmenu.row(item1)
                mainmenu.add(item2, item3, item4, item5)
                mainmenu.row(item6)
                mainmenu.row(item7)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать,\nЯ - <b>🤖Бот обменник</b>, созданный чтобы быстро менять тебе криптовалюту.🚀💸",parse_mode="html", reply_markup=mainmenu)
            
            elif call.data == 'Обменный курс':
                cursback = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Назад", callback_data="Меню")
                cursback.row(item1)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="‼️ Обменный курс:\n🇺🇸 1 USD - 🇲🇩 19 MDL\n    \nТранзакция меньше 🇺🇸 15 USD:\n🇺🇸 1 USD - 🇲🇩 20 MDL\n   \n🎲💵15$ = 280MDL💵🎲\n🎲💵16$ = 300MDL💵🎲\n🎲💵17$ = 320MDL💵🎲\n🎲💵30$ = 570MDL💵🎲\n🎲💵32$ = 610MDL💵🎲", reply_markup=cursback)
            
            elif call.data == 'Баланс бота':
                balanceback = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Назад", callback_data="Меню")
                balanceback.row(item1)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="‼️ ✅ Сейчас доступно для обмена:\n💰Bitcoin - 0 🇺🇸USD\n💰Litecoin - 82 🇺🇸USD\n", reply_markup=balanceback)
            
            elif call.data == 'Частые вопросы':
                faqback = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Назад", callback_data="Меню")
                faqback.row(item1)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="⁉️Сколько времени занимает транзакция?\n✅Время транзакции обычно не превышает 1-3 минуты.\n   \n⁉️Какие способы оплаты доступны?\n✅Мы принимаем платежи через\n🏧Cash in и 💳P2P.\n   \n⁉️Какие часы работы бота?\n✅Бот работает 24/7\n", reply_markup=faqback)
            
            
            
            
            
            
            
            elif call.data == 'Рулетка':
                ruletkaback = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Записаться✅", url="https://t.me/MDobmen")
                item2 = types.InlineKeyboardButton("Назад", callback_data="Меню")
                ruletkaback.add(item1)
                ruletkaback.row(item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🎉В честь открытия бота мы дарим 5 🇺🇸USD\n одному из первых 20 клиентов.\n   \n‼️Подписка на канал с отзывами обязательна!\nСписок участников:\n1.🎲\n2.🎲\n3.🎲 @lilizxca\n4.🎲\n5.🎲\n6.🎲\n7.🎲 @Borzik777\n8.🎲 @tyrobnk\n9.🎲\n10.🎲\n11.🎲\n12.🎲 @alexandermalii\n13.🎲\n14.🎲\n15.🎲 @moldovaan\n16.🎲\n17.🎲\n18.🎲\n19.🎲@Malatok222\n20.🎲\n   \n‼️Нажми кноку ниже чтобы записаться👇", reply_markup=ruletkaback)
 




 
#Crypto-choose
            
            elif call.data == 'Обменять':
                obmenltcbtc = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("🤑Bitcoin", callback_data="BTC")
                item2 = types.InlineKeyboardButton("🤑Litecoin", callback_data="LTC")
                item3 = types.InlineKeyboardButton("Назад", callback_data="Меню")
                obmenltcbtc.add(item1, item2)
                obmenltcbtc.row(item3)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отлично🔥\nТеперь выбери что хочешь купить:", reply_markup=obmenltcbtc)
        
        #Bank-choose
            
            elif call.data == 'BTC':
                banksbtc = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("🏦MAIB", callback_data="maibBTC")
                item2 = types.InlineKeyboardButton("🏦MICB", callback_data="micbBTC")
                item3 = types.InlineKeyboardButton("🏦Victoriabank", callback_data="vbBTC")
                item4 = types.InlineKeyboardButton("Назад", callback_data="Обменять")
                banksbtc.add(item1, item2)
                banksbtc.row(item3)
                banksbtc.row(item4)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать, \nТы выбрал Bitcoin🚀\nТеперь выбери удобный тебе банк:\n", reply_markup=banksbtc)
            
            elif call.data == 'LTC':
                banksltc = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("🏦MAIB", callback_data="maibLTC")
                item2 = types.InlineKeyboardButton("🏦MICB", callback_data="micbLTC")
                item3 = types.InlineKeyboardButton("🏦Victoriabank", callback_data="vbLTC")
                item4 = types.InlineKeyboardButton("Назад", callback_data="Обменять")
                banksltc.add(item1, item2)
                banksltc.row(item3)
                banksltc.row(item4)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать, \nТы выбрал Litecoin🚀\nТеперь выбери удобный тебе банк:\n", reply_markup=banksltc)
        
        #Payment-waiting
            
            elif call.data == 'maibBTC':
                maibBTCpay = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Далее▶️", callback_data="maibBTCpaydone")
                item2 = types.InlineKeyboardButton("Отменить перевод❌", callback_data="BTC")
                maibBTCpay.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать, \nТы выбрал Bitcoin🚀\nCпособ оплаты: 🏦MAIB\nПереведи нужную тебе сумму на данную карту:\n💳4356 9600 6067 8783\n   \n‼️После перевода нажми кнопку Далее▶️", reply_markup=maibBTCpay)
            
            elif call.data == 'maibLTC':
                maibLTCpay = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Далее▶️", callback_data="maibLTCpaydone")
                item2 = types.InlineKeyboardButton("Отменить перевод❌", callback_data="LTC")
                maibLTCpay.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать, \nТы выбрал Litecoin🚀\nCпособ оплаты: 🏦MAIB\nПереведи нужную тебе сумму на данную карту:\n💳4356 9600 6067 8783\n   \n‼️После перевода нажми кнопку Далее▶️", reply_markup=maibLTCpay)
            
            elif call.data == 'micbBTC':
                micbBTCpay = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Далее▶️", callback_data="micbBTCpaydone")
                item2 = types.InlineKeyboardButton("Отменить перевод❌", callback_data="BTC")
                micbBTCpay.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать, \nТы выбрал Bitcoin🚀\nCпособ оплаты: 🏦MICB\nПереведи нужную тебе сумму на данную карту:\n💳Временно недоступно\n   \n‼️После перевода нажми кнопку Далее▶️", reply_markup=micbBTCpay)
            
            elif call.data == 'micbLTC':
                micbLTCpay = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Далее▶️", callback_data="micbLTCpaydone")
                item2 = types.InlineKeyboardButton("Отменить перевод❌", callback_data="LTC")
                micbLTCpay.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать, \nТы выбрал Litecoin🚀\nCпособ оплаты: 🏦MICB\nПереведи нужную тебе сумму на данную карту:\n💳Временно недоступно\n   \n‼️После перевода нажми кнопку Далее▶️", reply_markup=micbLTCpay)
            
            elif call.data == 'vbBTC':
                vbBTCpay = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Далее▶️", callback_data="vbBTCpaydone")
                item2 = types.InlineKeyboardButton("Отменить перевод❌", callback_data="BTC")
                vbBTCpay.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать, \nТы выбрал Bitcoin🚀\nCпособ оплаты: 🏦Victoriabank\nПереведи нужную тебе сумму на данную карту:\n💳4779 1800 0709 4882\n   \n‼️После перевода нажми кнопку Далее▶️", reply_markup=vbBTCpay)
            
            elif call.data == 'vbLTC':
                vbLTCpay = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Далее▶️", callback_data="vbLTCpaydone")
                item2 = types.InlineKeyboardButton("Отменить перевод❌", callback_data="LTC")
                vbLTCpay.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать,\nТы выбрал Litecoin🚀\nCпособ оплаты: 🏦Victoriabank\nПереведи нужную тебе сумму на данную карту:\n💳4779 1800 0709 4882\n   \n‼️После перевода нажми кнопку Далее▶️", reply_markup=vbLTCpay)
        
        #Getting crypto wallet !!!!!!!!!!!!!!!!!!!!!!
            elif call.data == 'maibBTCpaydone':
                maibBTCgetwallet = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Оператор✅", url="https://t.me/MDobmen")
                item2 = types.InlineKeyboardButton("Отменить перевод❌", callback_data="BTC")
                maibBTCgetwallet.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать,\nТы выбрал Bitcoin🚀\nCпособ оплаты: 🏦MAIB\n    \n️💸Отправь оператору свой\n Bitcoin кошелек и фото чека.", reply_markup=maibBTCgetwallet)
                bot.forward_message(config.chat_id, message_id=call.message.message_id, from_chat_id=call.message.chat.id)
            
            elif call.data == 'maibLTCpaydone':
                maibLTCgetwallet = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Оператор✅", url="https://t.me/MDobmen")
                item2 = types.InlineKeyboardButton("Отменить перевод❌", callback_data="LTC")
                maibLTCgetwallet.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать, \nТы выбрал Litecoin🚀\nCпособ оплаты: 🏦MAIB\n    \n️💸Отправь оператору свой\n Litecoin кошелек и фото чека.", reply_markup=maibLTCgetwallet)
                bot.forward_message(config.chat_id, message_id=call.message.message_id, from_chat_id=call.message.chat.id)
            
            elif call.data == 'micbLTCpaydone':
                micbLTCgetwallet = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Оператор✅", url="https://t.me/MDobmen")
                item2 = types.InlineKeyboardButton("Отменить перевод❌", callback_data="LTC")
                micbLTCgetwallet.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать, \nТы выбрал Litecoin🚀\nCпособ оплаты: 🏦MICB\n    \n️💸Отправь оператору свой\n Litecoin кошелек и фото чека.", reply_markup=micbLTCgetwallet)
                bot.forward_message(config.chat_id, message_id=call.message.message_id, from_chat_id=call.message.chat.id)
            elif call.data == 'micbBTCpaydone':
                micbBTCgetwallet = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Оператор✅", url="https://t.me/MDobmen")
                item2 = types.InlineKeyboardButton("Отменить перевод❌", callback_data="BTC")
                micbBTCgetwallet.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать, \nТы выбрал Bitcoin🚀\nCпособ оплаты: 🏦MICB\n    \n️💸Отправь оператору свой\n Bitcoin кошелек и фото чека.", reply_markup=micbBTCgetwallet)
                bot.forward_message(config.chat_id, message_id=call.message.message_id, from_chat_id=call.message.chat.id)
            elif call.data == 'vbBTCpaydone':
                vbBTCgetwallet = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Оператор✅", url="https://t.me/MDobmen")
                item2 = types.InlineKeyboardButton("Отменить перевод❌", callback_data="BTC")
                vbBTCgetwallet.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать, \nТы выбрал Bitcoin🚀\nCпособ оплаты: 🏦Victoriabank\n    \n️💸Отправь оператору свой\n Bitcoin кошелек и фото чека.", reply_markup=vbBTCgetwallet)
                bot.forward_message(config.chat_id, message_id=call.message.message_id, from_chat_id=call.message.chat.id)
            elif call.data == 'vbLTCpaydone':
                vbLTCgetwallet = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Оператор✅", url="https://t.me/MDobmen")
                item2 = types.InlineKeyboardButton("Отменить перевод❌", callback_data="LTC")
                vbLTCgetwallet.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать, \nТы выбрал Litecoin🚀\nCпособ оплаты: 🏦Victoriabank\n    \n️💸Отправь оператору свой\n Litecoin кошелек и фото чека.", reply_markup=vbLTCgetwallet)
                bot.forward_message(config.chat_id, message_id=call.message.message_id, from_chat_id=call.message.chat.id)


    except Exception as e:
        print(repr(e))

# Run
bot.polling(none_stop=True)