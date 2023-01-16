import telebot
import config
import openai

bot = telebot.TeleBot(config.tg_token)
openai.api_key = config.openai_token


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я разбираюсь во всех областях. Чем я могу тебе помочь?')


@bot.message_handler(func=lambda message: True)
def GPT_answer(message):
    print(f'Пользователь: {message.from_user.username}\nЗапрос: {message.text}\n')
    bot.send_message(message.from_user.id, 'Думаю...\nНемного подожди🥸')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=2048,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(chat_id=message.chat.id, text=f"Мой ответ:\n{response['choices'][0]['text']}")


bot.polling()
