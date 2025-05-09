import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(
    "7263604478:AAHWJCmBcf-6l6F5fGk3-c20wBpWPvBfH2s"
)  # ← вставь сюда свой токен от @BotFather

products = {
    "Чай": [
        {
            "name": 'Зелёный чай "Сенча"',
            "desc": "Японский чай. 5.99€",
            "url": "https://example.com/sencha",
            "img": "https://images.unsplash.com/photo-1518977956815-dee006421f4d",
        },
        {
            "name": 'Чёрный чай "Ассам"',
            "desc": "Крепкий индийский чай. 4.49€",
            "url": "https://example.com/assam",
            "img": "https://images.unsplash.com/photo-1505576399279-565b52c7f86e",
        },
    ],
    "Аксессуары": [
        {
            "name": "Чайник керамический",
            "desc": "500 мл, ручная работа. 12.00€",
            "url": "https://example.com/kettle",
            "img": "https://images.unsplash.com/photo-1632824110400-6b041a2c0410",
        },
        {
            "name": "Ситечко для заварки",
            "desc": "Металлическое, удобное. 2.50€",
            "url": "https://example.com/strainer",
            "img": "https://images.unsplash.com/photo-1617115186583-df846d5f3139",
        },
    ],
}


@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup()
    for category in products:
        markup.add(InlineKeyboardButton(category, callback_data=category))
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def show_products(call):
    category = call.data
    for product in products[category]:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Перейти на сайт", url=product["url"]))
        bot.send_photo(
            call.message.chat.id,
            product["img"],
            caption=f"{product['name']}\n{product['desc']}",
            reply_markup=markup,
        )


bot.polling()
