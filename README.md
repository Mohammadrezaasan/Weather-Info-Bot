# <p align="center">🌦 Welcome To Weather Info Bot 🌦
 [![Supported Python versions](https://img.shields.io/pypi/pyversions/pyTelegramBotAPI.svg)](https://pypi.python.org/pypi/pyTelegramBotAPI)

<p align="center">A simple and convenient robot that tells you the weather with a few clicks <a href="https://t.me/tester_mohammadreza_asan1_bot">Weather Info Bot</a>.</p>

## <p align="center">Bot API Source : <a href="https://www.weatherapi.com/">Weather Api</a>

## Getting started


* To start the project, we need to build a robot that was built with the help of the <a href="https://t.me/Bot Father">Bot Father</a> :

* When your bot is built, the Bot Father will give you a token at the end { You put that token in the token variable in the config file } :

```
bot = telebot.TeleBot(Token_bot)
```
 ## Next step
 * To get the information you need, you must apply to the source site to receive the information you need after the request { Currently, I am using the prepared and edited source of <a href="https://rapidapi.com/weatherapi/api/weatherapi-com/">Rapid Api</a> site because you waste less time and it makes your work faster. }
 ```
 url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
```
  
## Codes docs
* The following code is related to the beginning part
```
@bot.message_handler(commands=['start']) # Here we set the message handler = start { For when message handler = start, the function does the following }
def handle_start(message): 
   chat_id = message.chat.id 
   text="`"+"The name of the desired city : "+"`" # Here we used the Telegram feature for text format { With this method, the user just clicks on the text and copies it to her clipboard, making the user's work faster. }
   markup = telebot.types.ReplyKeyboardMarkup(True, False) # In this section, we prepare a variable for the buttons, which will send the text inside the button only by clicking on it.
   markup.row("🔴 First, enter the name of your desired city as in the example below 🔴")
   markup.row('The name of the desired city : London')
   bot.send_message(chat_id,'Hello 🙋🏻‍♂️\nwelcome to the Weather Info Bot 👾 '+'\n🔴🔴 IMPORTANT 🔴🔴\nTo enter the name of your desired city, click on the text below and add the name of your desired city to the end of the text.',reply_markup=markup) # In this section, you enter the desired texts, which will be sent as text along with the button page
   bot.send_message(chat_id,text,parse_mode='MarkdownV2')
```
 
 * The code below is for the important part after the start part
 ```
 @bot.message_handler(content_types=['text']) # We put the message handler = content_types=['text'] here { If the user enters any text, our function will be activated and after activation, it will check the conditions that we have written in the form of try, if, and elif inside that function to see if the text entered by the user matches our conditions. or not? , if it matches, it fulfills that condition. }
def handle_text(message):
    message.text = message.text.lower() # In this section, we convert all the messages entered by the user into lowercase letters so that they don't have problems, and we write our codes according to the standard.
 ```
 * The following code is used to get the city name from the user
 ```
     if  'the name of the desired city' in message.text :
        try:

            global city_name
            city_name = message.text.replace('the name of the desired city','')
            city_name =  city_name.replace(":","")
            city_name_test = city_name.replace(" ","")
            city_name_test = city_name_test[0] , city_name_test[1]
            if city_name_test[0]  not in Alphabet :
                bot.reply_to(message,"The city name was not registered successfully ❌")
           
            elif city_name_test[1] not in Alphabet : 
                bot.reply_to(message,"The city name was not registered successfully ❌")

            elif city_name_test[0] in Alphabet : 
                chat_id = message.chat.id 
                markup = telebot.types.ReplyKeyboardMarkup(True, False)
                markup.row("🤖 Introducing The Robot 🤖")
                markup.row('🗝 click here to find out what each keyword does 🗝')
                markup.row('📓 click here to open the list of keywords for you 📓')
                markup.row('🔄 Changing the name of the city 🔄')
                bot.send_message(chat_id,"The city name was successfully registered ✅\nCity Name :"+city_name.title(),reply_markup=markup)
        except: 
            bot.reply_to(message,"The city name was not registered successfully ❌")
 ```
 
 
 
 
 
 
 
 
 
 
 
 
 
