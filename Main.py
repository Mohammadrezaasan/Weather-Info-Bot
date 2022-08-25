from turtle import title
from telebot import TeleBot
import telebot
from telebot import types
from markupsafe import Markup
from rsa import PublicKey
import requests
import json
from decimal import *
from weather_info_config import*
"----------------------------------------------------------------------------------------------------------"
bot = telebot.TeleBot(Token_bot)
url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
"----------------------------------------------------------------------------------------------------------"
@bot.message_handler(commands=['start'])
def handle_start(message):
   chat_id = message.chat.id 
   markup = telebot.types.ReplyKeyboardMarkup(True, False)
   markup.row("🔴 First, enter the name of your desired city as in the example below 🔴")
   markup.row('The name of the desired city : London')
   bot.send_message(chat_id,'Hello 🙋🏻‍♂️\nwelcome to the Weather Info Bot 👾 ', reply_markup=markup)
"----------------------------------------------------------------------------------------------------------"
@bot.message_handler(content_types=['text'])
def handle_text(message):
    message.text = message.text.lower()
    if 'the name of the desired city' in message.text :
        global city_name
        city_name = message.text.replace('the name of the desired city','')
        city_name =  city_name.replace(":","")
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("🤖 Introducing The Robot 🤖")
        markup.row('🗝 click here to find out what each keyword does 🗝')
        markup.row('📓 click here to open the list of keywords for you 📓')
        markup.row('🔄 Changing the name of the city 🔄')
        bot.send_message(chat_id,'The name of the city was successfully registered ✅', reply_markup=markup)
    
    elif message.text == "🤖 introducing the robot 🤖" :
        bot.reply_to(message,"Hello, my name is Weather Info bot. I can give you the current weather information and also have the ability to predict the weather for the next two days.☀️🌦⌚️\nI also have another feature that you can use to find out the local time of the desired location.🌎🕑")
    
    elif message.text == "🗝 click here to find out what each keyword does 🗝" : 
        bot.reply_to(message,'coming soon ....')

    elif message.text == "📓 click here to open the list of keywords for you 📓" : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row("🌦 Click here to get current weather conditions 🌦")
        markup.row("😎 click here to get the weather forecast 😎")
        markup.row("⌚️🌎 Click here to get the local time of your desired location ⌚️🌎")
        markup.row('🔄 Changing the name of the city 🔄')
        markup.row('Return to main page ↩️')
        bot.send_message(chat_id,'Keyword list opened successfully ✅', reply_markup=markup)

    elif message.text == "🌦 click here to get current weather conditions 🌦" :
        try :
            querystring = {"q":city_name,"days":"3"}

            headers = {
	     "X-RapidAPI-Key": RapidAPI_Key,
	     "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
         }

            response = requests.request("GET", url, headers=headers, params=querystring)

            information_received = json.loads(response.text)
            current = information_received["current"]
            location = information_received["location"]
            condition = current['condition']
    
            
            bot.reply_to(message,'Country Name 🌎 : '+location['country']+'\nRegion 🗺 : '+location['region']+'\nCity Name 🏙 : '+location['name']+"\n------------------------------------------------------"+'\nLocal Time ⌚️ : '+location['localtime'].split()[1]+'\nCalendar 🗓 : '+location['localtime'].split()[0]+'\nLatest update on local time ⌚️ : '+current['last_updated'].split()[1]+"\nIt’s "+condition['text']+' Now'+sticker[condition['text']]+'\nTemperature 🌡 : '+str(current['temp_c'])+'°C'+'\nFeels Like 🚻 : '+str(current['feelslike_c'])+'°C'+'\nTemperature 🌡 : '+str(current['temp_f'])+'°F'+'\nFeels Like 🚻 : '+str(current['feelslike_f'])+'°F'+'\nWind Speed According To The Latest Update 🌬 : '+str(current['wind_kph'])+'KPH'+'\nWind Speed According To The Latest Update 🌬 : '+str(current['wind_mph'])+'MPH'+'\nWind Direction 🧭 : '+str(current['wind_dir'])+'\nPressure In Inches 🛫 : '+str(current['pressure_in'])+'\nPrecipitation Amount 🌧 : '+str(current['precip_mm'])+'MM'+'\nPrecipitation Amount 🌧 : '+str(current['precip_in'])+' Inches'+'\nHumidity💧: '+str(current['humidity'])+'%'+'\nCloud Cover ☁️ : '+str(current['cloud'])+'%'+'\nVisibility 🛣 : '+str(current['vis_km'])+'KM'+'\nVisibility 🛣 : '+str(current['vis_miles'])+'MPH'+'\nUV ☀️🕶 : '+str(current['uv']))                                                                                                                                                                
        except : 
            bot.reply_to(message,'🔴🔴 Make sure the city name you entered is correct 🔴🔴')
   
    elif message.text == 'return to main page ↩️' : 
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("🤖 Introducing The Robot 🤖")
        markup.row('🗝 click here to find out what each keyword does 🗝')
        markup.row('📓 click here to open the list of keywords for you 📓')
        markup.row('🔄 Changing the name of the city 🔄')
        bot.send_message(chat_id,'Return to main page was successful ✅', reply_markup=markup)
    
    elif message.text == 'return to the previous page 🔙' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row("🌦 Click here to get current weather conditions 🌦")
        markup.row("😎 click here to get the weather forecast 😎")
        markup.row("⌚️🌎 Click here to get the local time of your desired location ⌚️🌎")
        markup.row('🔄 Changing the name of the city 🔄')
        markup.row('Return to main page ↩️')
        bot.send_message(chat_id,'Return to the previous page was successfully ✅', reply_markup=markup)


    elif message.text == '⌚️🌎 click here to get the local time of your desired location ⌚️🌎' :  
        try :
    
            querystring = {"q":city_name,"days":"3"}

            headers = {
         "X-RapidAPI-Key": RapidAPI_Key,
         "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
         }

            response = requests.request("GET", url, headers=headers, params=querystring)

            information_received = json.loads(response.text)
            current = information_received["current"]
            location = information_received["location"]
            condition = current['condition']
        
                

            bot.reply_to(message,'Country Name 🌎 : '+location['country']+'\nRegion 🗺 : '+location['region']+'\nCity Name 🏙 : '+location['name']+"\nLocal Time ⌚️ : "+location['localtime'].split()[1]+'\nCalendar 🗓 : '+location['localtime'].split()[0]+"\nIt’s "+condition['text']+' Now'+sticker[condition['text']])
        except : 
            bot.reply_to(message,'🔴🔴 Make sure the city name you entered is correct 🔴🔴')




    elif message.text == '😎 click here to get the weather forecast 😎' :
        
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('⏳ Daily Forecast ⏳')
        markup.row('🕥 Hourly Daily Forecast 🕥')
        markup.row('🌌 Day And Night Times 🌄\nFor Example[ sunrise : 5:55 ]')
        markup.row('🔄 Changing the name of the city 🔄')
        markup.row('Return to main page ↩️','Return to the previous page 🔙')
        bot.send_message(chat_id,'🔘 Choose one of the options below 🔘',reply_markup=markup)
    
    elif message.text == '⏳ daily forecast ⏳' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row("🔮 Today's weather forecast 🔮")
        markup.row("🔮 Tomorrow's weather forecast 🔮")
        markup.row("🔮 The weather forecast for the day after tomorrow 🔮")
        markup.row('Return to main page ↩️','Return to the forecast page 🔙')
        bot.send_message(chat_id,'🔘 Choose one of the options below 🔘',reply_markup=markup)

    elif message.text in select_day_for_daily_forecast : 
        global answer_choose_the_day_of_the_daily_forecast
        answer_choose_the_day_of_the_daily_forecast = message.text 
        try :
            querystring = {"q":city_name,"days":"3"}

            headers = {
         "X-RapidAPI-Key": RapidAPI_Key,
         "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

            response = requests.request("GET", url, headers=headers, params=querystring)

            information_received = json.loads(response.text)
            location = information_received["location"]
            forecast = information_received['forecast']["forecastday"][select_day_for_daily_forecast[answer_choose_the_day_of_the_daily_forecast]]['day']
            condition = forecast['condition']
            date1 = information_received['forecast']["forecastday"][select_day_for_daily_forecast[answer_choose_the_day_of_the_daily_forecast]]
                        

            bot.reply_to(message,'Country Name 🌎 : '+location['country']+'\nRegion 🗺 : '+location['region']+'\nCity Name 🏙 : '+location['name']+"\n------------------------------------------------------"+'\nForecast Date 🗓 : '+str(date1['date'])+'\n'+condition['text']+' '+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' '+sticker[condition['text']]+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Maximum Temperature 🌡 : "+str(forecast['maxtemp_c'])+'°C'+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Minimum Temperature 🌡 : "+str(forecast['mintemp_c'])+'°C'+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Average Temperature 🌡 : "+str(forecast['avgtemp_c'])+"°C"+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Maximum Temperature 🌡 : "+str(forecast['maxtemp_f'])+'°F'+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Minimum Temperature 🌡 : "+str(forecast['mintemp_f'])+'°F'+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Average Temperature 🌡 : "+str(forecast['avgtemp_f'])+'°F'+'\nMaximum Wind Speed 🌬 : '+str(forecast['maxwind_kph'])+'KPH'+'\nMaximum Wind Speed 🌬 : '+str(forecast['maxwind_mph'])+'MPH'+'\nAverage Visibility 🛣 : '+str(forecast['avgvis_km'])+'KM'+'\nAverage Visibility 🛣 : '+str(forecast['avgvis_miles'])+'MPH'+'\nAverage Humidity 💧 : '+str(forecast['avghumidity'])+'%'+"\nWill It Rain "+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' 🌧 : '+yes_or_no[str(forecast["daily_will_it_rain"])]+'\nChance Of Rain '+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' 🌧 : '+str(forecast['daily_chance_of_rain'])+'%'+"\nWill It Snow "+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' 🌨 : '+yes_or_no[str(forecast["daily_will_it_snow"])]+'\nChance Of Snow '+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' 🌨 : '+str(forecast['daily_chance_of_snow'])+'%'+'\nTotal Precipitation 🌧 : '+str(forecast['totalprecip_mm'])+'MM'+'\nTotal Precipitation 🌧 : '+str(forecast['totalprecip_in'])+'Inches')                                                        
        except : 
            bot.reply_to(message,'🔴🔴 Make sure the city name you entered is correct 🔴🔴')
    
    elif message.text == 'return to the forecast page 🔙' :
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('⏳ Daily Forecast ⏳')
        markup.row('🕥 Hourly Daily Forecast 🕥')
        markup.row('🌌 Day And Night Times 🌄\nFor Example[ sunrise : 5:55 ]')
        markup.row('🔄 Changing the name of the city 🔄')
        markup.row('Return to main page ↩️','Return to the previous page 🔙')
        bot.send_message(chat_id,'Return to forecast page was successful ✅',reply_markup=markup)

    elif message.text == 'return to the daily forecast list page 🔙' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row("🔮 Today's weather forecast 🔮")
        markup.row("🔮 Tomorrow's weather forecast 🔮")
        markup.row("🔮 The weather forecast for the day after tomorrow 🔮")
        markup.row('Return to main page ↩️','Return to the forecast page 🔙')
        bot.send_message(chat_id,'Return to daily forecast list page was successful ✅',reply_markup=markup)


    elif message.text == '🕥 hourly daily forecast 🕥' : 

        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('🕥 Hourly Forecast Today 🕥')
        markup.row('🕥 Hourly Forecast For Tomorrow 🕥')
        markup.row('🕥 Hourly Forecast The Day After Tomorrow 🕥')
        markup.row('Return to main page ↩️','Return to the forecast page 🔙')
        bot.send_message(chat_id,'🔘 Choose one of the options below 🔘',reply_markup=markup)
    
    elif message.text in select_day_for_hourly_forecast : 
        global hour4
        hour4 = message.text
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('00:00','01:00','02:00','03:00')
        markup.row('04:00','05:00','06:00','07:00')
        markup.row('08:00','09:00','10:00','11:00')
        markup.row('12:00','13:00','14:00','15:00')
        markup.row('16:00','17:00','18:00','19:00')
        markup.row('20:00','21:00','22:00','23:00')
        markup.row('Return to main page ↩️','Return to the hourly daily forecast page 🔙')
        bot.send_message(chat_id,'‼️ Select one of the following hours and you will receive the weather forecast for that hour according to the selected time frame ‼️',reply_markup=markup)
      
    elif message.text in choose_an_hour : 
        try :

            hour2 = message.text
            
            querystring = {"q":city_name,"days":"3"}

            headers = {
         "X-RapidAPI-Key": RapidAPI_Key,
         "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

            response = requests.request("GET", url, headers=headers, params=querystring)

            information_received = json.loads(response.text)
            location = information_received["location"]
            forecast = information_received['forecast']["forecastday"][select_day_for_hourly_forecast[hour4]]['hour'][choose_an_hour[hour2]]
            condition = forecast['condition']
            location = information_received["location"]
            date1 = information_received['forecast']["forecastday"][select_day_for_hourly_forecast[hour4]]            

            bot.reply_to(message,'Country Name 🌎 : '+location['country']+'\nRegion 🗺 : '+location['region']+'\nCity Name 🏙 : '+location['name']+"\n------------------------------------------------------"+'\nForecast Date 🗓 : '+str(date1['date'])+'\n'+condition['text']+' At '+hour2+' '+sticker[condition['text']]+"\nTemperature 🌡 : "+str(forecast['temp_c'])+"°C"+"\nFeels Like 🚻 : "+str(forecast['feelslike_c'])+"°C"+"\nThe Heat We Feel ♨️ : "+str(forecast['heatindex_c'])+'°C'+"\nTemperature 🌡 : "+str(forecast['temp_f'])+"°F"+"\nFeels Like 🚻 : "+str(forecast['feelslike_f'])+"°F"+"\nThe Heat We Feel ♨️ : "+str(forecast['heatindex_f'])+'°F'+"\nWind Speed At "+hour2+" 🌬 : "+str(forecast['wind_kph'])+"KPH"+"\nWind Speed At "+hour2+" 🌬 : "+str(forecast['wind_mph'])+"MPH"+"\nWind Temperature 🌡 : "+str(forecast['windchill_c'])+'°C'+"\nWind Temperature 🌡: "+str(forecast['windchill_f'])+'°F'+"\nWind Direction 🧭 : "+str(forecast["wind_dir"])+"\nPressure In Inches 🛫 : "+str(forecast["pressure_in"])+"\nWill It Rain "+the_name_of_each_day_2[hour4]+' At '+hour2+' 🌧 : '+yes_or_no[str(forecast["will_it_rain"])]+'\nChance Of Rain '+the_name_of_each_day_2[hour4]+' At '+hour2+' 🌧 : '+str(forecast['chance_of_rain'])+'%'+"\nPrecipitation Amount 🌧 : "+str(forecast['precip_mm'])+"MM"+"\nPrecipitation Amount 🌧 : "+str(forecast['precip_in'])+"Inches"+"\nWill It Snow "+the_name_of_each_day_2[hour4]+" At "+hour2+' 🌨 : '+yes_or_no[str(forecast["will_it_snow"])]+'\nChance Of Snow '+the_name_of_each_day_2[hour4]+' At '+hour2+' 🌨 : '+str(forecast['chance_of_snow'])+'%')                                                                                                                                                                
        except : 
            bot.reply_to(message,'🔴🔴 Make sure the city name you entered is correct 🔴🔴')

    elif message.text == 'return to the hourly daily forecast page 🔙':
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('🕥 Hourly Forecast Today 🕥')
        markup.row('🕥 Hourly Forecast For Tomorrow 🕥')
        markup.row('🕥 Hourly Forecast The Day After Tomorrow 🕥')
        markup.row('Return to main page ↩️','Return to the forecast page 🔙')
        bot.send_message(chat_id,'Return to hourly daily forecast page was successful ✅',reply_markup=markup)

    elif message.text == "🌌 day and night times 🌄\nfor example[ sunrise : 5:55 ]" :
        try :

            
            
            querystring = {"q":city_name,"days":"3"}

            headers = {
         "X-RapidAPI-Key": RapidAPI_Key,
         "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
         }

            response = requests.request("GET", url, headers=headers, params=querystring)
            
            information_received = json.loads(response.text)
            location = information_received["location"]
            #p0
            forecast = information_received['forecast']["forecastday"][0]['astro']
            date1 = information_received['forecast']["forecastday"][0]            
            #p1
            forecast1 = information_received['forecast']["forecastday"][1]['astro']
            date11 = information_received['forecast']["forecastday"][1]            
            #p2
            forecast2 = information_received['forecast']["forecastday"][2]['astro']
            date12 = information_received['forecast']["forecastday"][2]            




            bot.reply_to(message,'Country Name 🌎 : '+location['country']+'\nRegion 🗺 : '+location['region']+'\nCity Name 🏙 : '+location['name']+"\n------------------------------------------------------"+'\nDate 🗓 : '+str(date1['date'])+"\nSunrise 🌅 : "+str(forecast['sunrise'])+"\nSunset 🌄 : "+str(forecast['sunset'])+"\nMoonrise 🌃 : "+str(forecast['moonrise'])+'\nMoonset 🏙 : '+str(forecast['moonset'])+'\nMoon phases : '+str(forecast['moon_phase'])+'\nMoon illumination : '+str(forecast['moon_illumination'])+"%"+"\n------------------------------------------------------"+'\nDate 🗓 : '+str(date11['date'])+"\nSunrise 🌅 : "+str(forecast1['sunrise'])+"\nSunset 🌄 : "+str(forecast1['sunset'])+"\nMoonrise 🌃 : "+str(forecast1['moonrise'])+'\nMoonset 🏙 : '+str(forecast1['moonset'])+'\nMoon phases : '+str(forecast1['moon_phase'])+'\nMoon illumination : '+str(forecast1['moon_illumination'])+"%"+"\n------------------------------------------------------"+'\nDate 🗓 : '+str(date12['date'])+"\nSunrise 🌅 : "+str(forecast2['sunrise'])+"\nSunset 🌄 : "+str(forecast2['sunset'])+"\nMoonrise 🌃 : "+str(forecast2['moonrise'])+'\nMoonset 🏙 : '+str(forecast2['moonset'])+'\nMoon phases : '+str(forecast2['moon_phase'])+'\nMoon illumination : '+str(forecast2['moon_illumination'])+"%")                                                                                                  
        except : 
            bot.reply_to(message,'🔴🔴 Make sure the city name you entered is correct 🔴🔴')
    
    elif  message.text =='🔄 changing the name of the city 🔄': 
        bot.reply_to(message,"🔴 To change the desired city name, type as in the example below 🔴\nThe name of the new city : Monaco")

    elif 'the name of the new city' in message.text : 
        update_city_name = message.text.replace("the name of the new city",'')
        update_city_name = update_city_name.replace(":",'')
        city_name = update_city_name
        if city_name == update_city_name : 
            bot.reply_to(message,'The name change was done successfully ✅')
        





"----------------------------------------------------------------------------------------------------------"
bot.polling(none_stop=True)
