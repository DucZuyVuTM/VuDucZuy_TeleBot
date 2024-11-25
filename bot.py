import os
import telebot
from telebot import types
import requests
from io import BytesIO

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

#-------------------------------------------------------------------------------
# Biến chung:
welcome_called = False
started = False
#-------------------------------------------------------------------------------

@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda message: message.text.lower() == "start")
@bot.message_handler(func=lambda message: message.text.lower() == "menu")
def send_welcome(message):
    global welcome_called, started
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

        menu = types.KeyboardButton("Menu")
        markup.row(menu)

        exts = ["Common Details", "Career", "Awards", "Products", "Public image"]
        for ext in exts:
            ext_d = types.KeyboardButton(ext)
            markup.row(ext_d)

        menu_cap_spl = ["Hello! You're interested about Suni? Stay tuned for more!\n\n",
                        "Here is the information list about Suni:\n",
                        "1. Common details\n",
                        "2. Career\n",
                        "3. Awards\n",
                        "4. Products\n",
                        "5. Public image\n\n",
                        "Please write the number corresponding to your choice or write the choice directly."]
        if welcome_called == False:
            menu_cap = "".join(menu_cap_spl)
        else:
            menu_cap = "".join(menu_cap_spl[1:])
        bot.send_photo(message.chat.id, photo="images/menu.jpg", caption=menu_cap, reply_markup=markup)
        welcome_called = True
        started = True
    except Exception as e:
        bot.send_message(6180286860, e)

@bot.message_handler(func=lambda message: message.text == "1")
@bot.message_handler(func=lambda message: message.text.lower() == "common details")
def common_details(message):
    if started == True:
        try:
            cd_cap_spl = ["Common details:\n\n",
                          "1. Real name: Ngo Dang Thu Giang\n",
                          "2. Date of Birth: 6/09/1990\n",
                          "3. Place of Birth: Ho Chi Minh City\n",
                          "4. Profession: singer, dancer\n",
                          "5. Education: Victoria University of Wellington\n",
                          "6. Nickname: Suni\n",
                          "7. Record label:\n",
                          "7.1. 4B Nexus (2024 - now)\n",
                          "7.2. Mustation Entertainment (2018 - 2024)\n",
                          "7.3. DreamS Entertainment (2014 - 2017)\n",
                          "8. Genres: V-Pop, R&B, Ballad"]
            cd_cap = "".join(cd_cap_spl)
            bot.send_photo(message.chat.id, photo="images/common_details.jpg", caption=cd_cap)
        except Exception as e:
            bot.send_message(6180286860, e)
    else:
        bot.send_message(message.chat.id, text="Bot is not started")

@bot.message_handler(func=lambda message: message.text == "2")
@bot.message_handler(func=lambda message: message.text.lower() == "career")
def common_details(message):
    if started == True:
        try:
            c_text_spl = ["Suni Ha Linh's singing career:\n\n",
                          "2008: First prize in Cleverteam Superstar contest.\n",
                          "2012: Runner-up in Vietnam's Kpop Star Hunt season 2.\n",
                          "2014: Top 4 in \"Vietnamese Star\".\n",
                          "2015: Changed her stage name to Suni Ha Linh.\n",
                          "2016: A new music product \"Em đã biết\" (\"I have known\").\n",
                          "2016: Released a MV named \"Say Yes\".\n",
                          "2018: Left DreamS Entertainment => Mustation Entertainment.\n",
                          "2018: Released a MV named \"Thích rồi đấy\" (\"I like you\").\n",
                          "2019: Released products \"Không sao mà, em đây rồi\" (\"It's okay, I'm here\").\n",
                          "2020: With band Chillies released the song \"Cứ chill thôi\" (\"Just chill out\").",
                          # -----
                          "Achievements of \"Em đã biết\" (\"I have known\"):\n\n",
                          "+) 101.000.000 streams in Zing MP3.\n",
                          "+) 31.000.000 views on Youtube.\n",
                          "+) TOP 1 Zing MP3 in 2016.\n\n",
                          "Achievements of \"Không sao mà, em đây rồi\" (\"It's okay, I'm here\"):\n\n",
                          "+) 101.000.000 streams in Zing MP3.\n",
                          "+) 76.000.000 views on Youtube.\n",
                          "+) TOP 10 Zing MP3 in 2019.\n\n",
                          "Achievements of \"Cứ chill thôi\" (\"Just chill out\"):\n\n",
                          "+) 7.000.000 streams on Nhaccuatui.\n",
                          "+) 94.000.000 views on Youtube.\n",
                          "+) TOP 10 Nhaccuatui in 2020.",
                          # -----
                          "2022 - \"Hương Mùa Hè\" (\"Summer Scent\"):\n\n",
                          "+) MUSICAL SERIES with a well-written script.\n",
                          "+) 3 EPISODES set in three different locations in Vietnam.\n",
                          "+) STORY: childhood with beautiful and pure memories in summer.\n",
                          "+) SUNI'S PERFORMANCE: 7 songs - 2 solo and 5 with other artists.\n\n",
                          "2023: Released the song \"Ngỏ lời\" (\"Proposal\") in May.\n",
                          "2023: Released the song \"Sự mập mờ\" (\"Ambiguity\") in July.\n",
                          "2024: Left Mustation Entertainment => 4B Nexus.\n",
                          "2024: Suni Ha Linh collaborates with singer Juun D to introduce the song \"Lạc khách\" (\"Castaway\").\n",
                          "2024: Confirmed to participate in the show \"Ride the Wind\" organized by Mango TV in China."]
            c_text_1 = "".join(c_text_spl[:11])
            c_text_2 = "".join(c_text_spl[11:23])
            c_text_3 = "".join(c_text_spl[23:])
            bot.send_photo(message.chat.id, photo="images/career1.jpg", caption=c_text_1)
            bot.send_photo(message.chat.id, photo="images/career2.jpg", caption=c_text_2)
            bot.send_photo(message.chat.id, photo="images/career3.jpg", caption=c_text_3)
        except Exception as e:
            bot.send_message(6180286860, e)
    else:
        bot.send_message(message.chat.id, text="Bot is not started")

@bot.message_handler(func=lambda message: message.text == "3")
@bot.message_handler(func=lambda message: message.text.lower() == "awards")
def common_details(message):
    if started == True:
        try:
            a_cap_spl = ["Suni Ha Linh's Awards:\n\n",
                         "1. Zing Music Awards 2016: Best R&B / Soul Song of the Year\n",
                         "2. Làn sóng Xanh 2016 (\"The Green Wave\"): Top 10 Song of the Year\n",
                         "3. V-Live Awards 2016: Best Rising Star\n",
                         "4. Yan Music Awards 2016: Top 20 Song of the Year\n",
                         "5. Keeng Young Awards 2017: Best Pop Song of the Year"]
            a_cap = "".join(a_cap_spl)
            bot.send_photo(message.chat.id, photo="images/awards.jpg", caption=a_cap)
        except Exception as e:
            bot.send_message(6180286860, e)
    else:
        bot.send_message(message.chat.id, text="Bot is not started")

@bot.message_handler(func=lambda message: message.text == "4")
@bot.message_handler(func=lambda message: message.text.lower() == "products")
def common_details(message):
    if started == True:
        try:
            p_cap_spl = ["*) 41 is the number of products, including new songs and covers\n\n",
                         "Top 10 Featured Songs:\n\n",
                         "1. Cảm ơn người đã rời xa tôi (\"Thank you for leaving me\") (2015)\n",
                         "2. Em đã biết (\"I’ve known\") (2016)\n",
                         "3. Say yes (2016)\n",
                         "4. Cảm nắng (\"Falling in love\") (2017)\n",
                         "5. Một ngày rất khác (\"A very different day\") (2017)\n",
                         "6. Thích rồi đấy (\"I like you\") (2018)\n",
                         "7. Không sao mà, em đây rồi (\"It’s okay I’m here\") (2019)\n",
                         "8. Cứ chill thôi (\"Just chill out\") (2020)\n",
                         "9. Ngày tỏ tình bạn (\"Friendship day\") (2021)\n",
                         "10. Nắng thủy tinh (\"Glass Sunshine\") (Cover) (2022)"]
            p_cap = "".join(p_cap_spl)
            bot.send_photo(message.chat.id, photo="images/products.jpg", caption=p_cap)
        except Exception as e:
            bot.send_message(6180286860, e)
    else:
        bot.send_message(message.chat.id, text="Bot is not started")

@bot.message_handler(func=lambda message: message.text == "5")
@bot.message_handler(func=lambda message: message.text.lower() == "public image")
def common_details(message):
    if started == True:
        try:
            pi_cap_spl = ["Influence on social media:\n\n",
                          "+) 386.000 Followers on Instagram\n",
                          "+) 1.200.000 Followers on Facebook\n",
                          "+) 261.000 Subscribers on Youtube\n",
                          "+) 2.200.000 Listeners on Spotify\n\n",
                          # -----
                          "BSI Top 10 Influencers: She has become one of the most influential celebrities on social media.\n",
                          "(BSI – Buzzmetrics Social Index)\n\n",
                          "Public Activity: She has performed in many concerts in universities and festivals in Vietnam or in South Korea.\n\n",
                          "The Face: She has become the face of many cosmetic brands and appeared in many advertisements on cosmetics and perfumes.\n\n",
                          "Autobiography: She has written a biography named \"SUNI STORY\", sharing some lifehacks, experience and optimism to other people."]
            pi_cap_1 = "".join(pi_cap_spl[:5])
            pi_cap_2 = "".join(pi_cap_spl[5:])

            bot.send_photo(message.chat.id, photo="images/public_image1.jpg", caption=pi_cap_1)
            bot.send_photo(message.chat.id, photo="images/public_image2.jpg", caption=pi_cap_2)
        except Exception as e:
            bot.send_message(6180286860, e)
    else:
        bot.send_message(message.chat.id, text="Bot is not started")

@bot.message_handler(commands=['exit'])
@bot.message_handler(func=lambda message: message.text.lower() == "exit")
def exit(message):
    global welcome_called, started
    try:
        bot.send_message(message.chat.id, text="Thank you for your interest in Suni!")
        welcome_called = False
        started = False
    except Exception as e:
        bot.send_message(6180286860, e)

@bot.message_handler(func=lambda message: True)
def echo_unav(message):
    try:
        bot.send_message(message.chat.id, text="Invalid message")
    except Exception as e:
        bot.send_message(6180286860, e)

bot.infinity_polling()
