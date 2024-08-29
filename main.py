import telebot  # type: ignore
import event
import random

bot = telebot.TeleBot(event.TOKEN)

facts = {
    "fact 1": """Pigs can recognize themselves in a mirror, indicating a high level of self-awareness.
Свиньи могут узнавать себя в зеркале, что свидетельствует о высоком уровне самосознания.""",
    "fact 2": """Pigs have an excellent sense of time and can remember events.
Свиньи обладают отличным чувством времени и могут запоминать события.

""",
    "fact 3": """Pigs have a keen sense of smell; they can detect scents underground.
 У свиней острое обоняние, они могут обнаружить запахи под землёй.""",
    "fact 4": """Pigs enjoy wallowing in mud to cool down since they lack sweat glands.
Свиньи любят купаться в грязи, чтобы охладиться, так как у них нет потовых желез.""",
    "fact 5": """In the wild, pigs live in groups called sounders, consisting of females and their offspring.
 В дикой природе свиньи живут стадами, которые состоят из самок и их потомства.""",
    "fact 6": """Pigs can produce over 20 different vocalizations for communication.
 Свиньи могут издавать более 20 различных звуков для общения.""",    
    "fact 7": """They are very social and friendly, capable of forming strong bonds with other pigs.
Они очень социальные и дружелюбные, могут завязывать прочные связи с другими свиньями.""",
    "fact 8": """Pigs prefer clean sleeping areas and typically avoid soiling their bedding.
Свиньи предпочитают чистые места для сна и обычно не пачкают свою спальную зону.""",
    "fact 9": """Pigs have facial recognition memory; they can remember people and other animals.
У свиней есть память на лица, они могут запомнить людей и других животных.""",
}

pig_images = [
    "https://imgur.com/a/C2TKU54",
    "https://imgur.com/a/SST1YwM",
    "https://imgur.com/a/nHraZwy",
    "https://imgur.com/a/a0mHNlA",
    "https://imgur.com/a/B0xVUdW",
    "https://imgur.com/a/WFIwCXy",
    "https://imgur.com/a/hzocOC0",
    "https://imgur.com/a/hfZwb94",
    "https://imgur.com/a/p7UqSNg",
    "https://imgur.com/a/hMP5nbJ",
    "https://imgur.com/a/68q6JeI",
    "https://imgur.com/a/U4Lkyll"
]

def create_main_menu():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("/start")
    item2 = telebot.types.KeyboardButton("/pigfact")
    item3 = telebot.types.KeyboardButton("/pigphoto")
    reply_markup=create_main_menu()  
    
   
    markup.add(item1, item2)
    markup.add(item3)
    return markup

@bot.message_handler(commands=['pigfact'])
def send_random_fact(message):
    try:
        random_fact = random.choice(list(facts.values()))
        bot.send_message(message.chat.id, random_fact)
    except Exception as e:
        print(f"Error sending fact: {e}")

@bot.message_handler(commands=['pigphoto'])
def send_random_photo(message):
    try:
        random_photo = random.choice(pig_images)
        bot.send_photo(message.chat.id, random_photo)
    except Exception as e:
        print(f"Error sending photo: {e}")

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(
        message.chat.id, 
        """Hello, this is khriu bot! Pig bot!
You can find out an interesting fact about pigs by writing: /pigfact
You can get a cute pig photo by writing: /pigphoto
To restart the bot write: /start
--------------------------------
Здравствуйте, это khriu бот! Бот свинок!
Вы можете узнать интересный факт про свинок написав : /pigfact
Вы можете получить милое фото свинки написав: /pigphoto
Чтобы перезапустить бота напишите: /start""",
        
    )



print("Bot is polling...")
bot.polling(none_stop=True)

