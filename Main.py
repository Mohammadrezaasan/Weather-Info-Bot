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
from telegram import ParseMode
from telegram import Bot
"----------------------------------------------------------------------------------------------------------"
bot = telebot.TeleBot(Token_bot)
url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
"----------------------------------------------------------------------------------------------------------"
@bot.message_handler(commands=['start'])
def handle_start(message):
   chat_id = message.chat.id 
   text="`"+"The name of the desired city : "+"`" 
   markup = telebot.types.ReplyKeyboardMarkup(True, False)
   markup.row("š“ First, enter the name of your desired city as in the example below š“")
   markup.row('The name of the desired city : London')
   bot.send_message(chat_id,'Hello šš»āāļø\nwelcome to the Weather Info Bot š¾ '+'\nš“š“ IMPORTANT š“š“\nTo enter the name of your desired city, click on the text below and add the name of your desired city to the end of the text.',reply_markup=markup)
   bot.send_message(chat_id,text,parse_mode='MarkdownV2')


"----------------------------------------------------------------------------------------------------------"
@bot.message_handler(content_types=['text'])
def handle_text(message):
    message.text = message.text.lower()
    if  'the name of the desired city' in message.text :
        try:

            global city_name
            city_name = message.text.replace('the name of the desired city','')
            city_name =  city_name.replace(":","")
            city_name_test = city_name.replace(" ","")
            city_name_test = city_name_test[0] , city_name_test[1]
            if city_name_test[0]  not in Alphabet :
                bot.reply_to(message,"The city name was not registered successfully ā")
           
            elif city_name_test[1] not in Alphabet : 
                bot.reply_to(message,"The city name was not registered successfully ā")

            elif city_name_test[0] in Alphabet : 
                chat_id = message.chat.id 
                markup = telebot.types.ReplyKeyboardMarkup(True, False)
                markup.row("š¤ Introducing The Robot š¤")
                markup.row('š click here to find out what each keyword does š')
                markup.row('š click here to open the list of keywords for you š')
                markup.row('š Changing the name of the city š')
                bot.send_message(chat_id,"The city name was successfully registered ā\nCity Name :"+city_name.title(),reply_markup=markup)
        except: 
            bot.reply_to(message,"The city name was not registered successfully ā")
    
    elif message.text == "š¤ introducing the robot š¤" :
        bot.reply_to(message,"Hello, my name is Weather Info bot. I can give you the current weather information and also have the ability to predict the weather for the next two days.āļøš¦āļø\nI also have another feature that you can use to find out the local time of the desired location.šš")
    
    elif message.text == "š click here to find out what each keyword does š" : 
        bot.reply_to(message,'coming soon ....')

    elif message.text == "š click here to open the list of keywords for you š" : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row("š¦ Click here to get current weather conditions š¦")
        markup.row("š click here to get the weather forecast š")
        markup.row("āļøš Click here to get the local time of your desired location āļøš")
        markup.row('š Changing the name of the city š')
        markup.row('Return to main page ā©ļø')
        bot.send_message(chat_id,'Keyword list opened successfully ā', reply_markup=markup)

    elif message.text == "š¦ click here to get current weather conditions š¦" :
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
    
            
            bot.reply_to(message,'Country Name š : '+location['country']+'\nRegion šŗ : '+location['region']+'\nCity Name š : '+location['name']+"\n------------------------------------------------------"+'\nLocal Time āļø : '+location['localtime'].split()[1]+'\nCalendar š : '+location['localtime'].split()[0]+'\nLatest update on local time āļø : '+current['last_updated'].split()[1]+"\nItās "+condition['text']+' Now'+sticker[condition['text']]+'\nTemperature š” : '+str(current['temp_c'])+'Ā°C'+'\nFeels Like š» : '+str(current['feelslike_c'])+'Ā°C'+'\nTemperature š” : '+str(current['temp_f'])+'Ā°F'+'\nFeels Like š» : '+str(current['feelslike_f'])+'Ā°F'+'\nWind Speed According To The Latest Update š¬ : '+str(current['wind_kph'])+'KPH'+'\nWind Speed According To The Latest Update š¬ : '+str(current['wind_mph'])+'MPH'+'\nWind Direction š§­ : '+str(current['wind_dir'])+'\nPressure In Inches š« : '+str(current['pressure_in'])+'\nPrecipitation Amount š§ : '+str(current['precip_mm'])+'MM'+'\nPrecipitation Amount š§ : '+str(current['precip_in'])+' Inches'+'\nHumidityš§: '+str(current['humidity'])+'%'+'\nCloud Cover āļø : '+str(current['cloud'])+'%'+'\nVisibility š£ : '+str(current['vis_km'])+'KM'+'\nVisibility š£ : '+str(current['vis_miles'])+'MPH'+'\nUV āļøš¶ : '+str(current['uv']))                                                                                                                                                                
        except : 
            bot.reply_to(message,'š“š“ Make sure the city name you entered is correct š“š“')
   
    elif message.text == 'return to main page ā©ļø' : 
        chat_id = message.chat.id 
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row("š¤ Introducing The Robot š¤")
        markup.row('š click here to find out what each keyword does š')
        markup.row('š click here to open the list of keywords for you š')
        markup.row('š Changing the name of the city š')
        bot.send_message(chat_id,'Return to main page was successful ā', reply_markup=markup)
    
    elif message.text == 'return to the previous page š' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row("š¦ Click here to get current weather conditions š¦")
        markup.row("š click here to get the weather forecast š")
        markup.row("āļøš Click here to get the local time of your desired location āļøš")
        markup.row('š Changing the name of the city š')
        markup.row('Return to main page ā©ļø')
        bot.send_message(chat_id,'Return to the previous page was successfully ā', reply_markup=markup)


    elif message.text == 'āļøš click here to get the local time of your desired location āļøš' :  
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
        
                

            bot.reply_to(message,'Country Name š : '+location['country']+'\nRegion šŗ : '+location['region']+'\nCity Name š : '+location['name']+"\nLocal Time āļø : "+location['localtime'].split()[1]+'\nCalendar š : '+location['localtime'].split()[0]+"\nItās "+condition['text']+' Now'+sticker[condition['text']])
        except : 
            bot.reply_to(message,'š“š“ Make sure the city name you entered is correct š“š“')




    elif message.text == 'š click here to get the weather forecast š' :
        
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('ā³ Daily Forecast ā³')
        markup.row('š„ Hourly Daily Forecast š„')
        markup.row('š Day And Night Times š\nFor Example[ sunrise : 5:55 ]')
        markup.row('š Changing the name of the city š')
        markup.row('Return to main page ā©ļø','Return to the previous page š')
        bot.send_message(chat_id,'š Choose one of the options below š',reply_markup=markup)
    
    elif message.text == 'ā³ daily forecast ā³' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row("š® Today's weather forecast š®")
        markup.row("š® Tomorrow's weather forecast š®")
        markup.row("š® The weather forecast for the day after tomorrow š®")
        markup.row('Return to main page ā©ļø','Return to the forecast page š')
        bot.send_message(chat_id,'š Choose one of the options below š',reply_markup=markup)

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
                        

            bot.reply_to(message,'Country Name š : '+location['country']+'\nRegion šŗ : '+location['region']+'\nCity Name š : '+location['name']+"\n------------------------------------------------------"+'\nForecast Date š : '+str(date1['date'])+'\n'+condition['text']+' '+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' '+sticker[condition['text']]+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Maximum Temperature š” : "+str(forecast['maxtemp_c'])+'Ā°C'+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Minimum Temperature š” : "+str(forecast['mintemp_c'])+'Ā°C'+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Average Temperature š” : "+str(forecast['avgtemp_c'])+"Ā°C"+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Maximum Temperature š” : "+str(forecast['maxtemp_f'])+'Ā°F'+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Minimum Temperature š” : "+str(forecast['mintemp_f'])+'Ā°F'+"\n"+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+"'s Average Temperature š” : "+str(forecast['avgtemp_f'])+'Ā°F'+'\nMaximum Wind Speed š¬ : '+str(forecast['maxwind_kph'])+'KPH'+'\nMaximum Wind Speed š¬ : '+str(forecast['maxwind_mph'])+'MPH'+'\nAverage Visibility š£ : '+str(forecast['avgvis_km'])+'KM'+'\nAverage Visibility š£ : '+str(forecast['avgvis_miles'])+'MPH'+'\nAverage Humidity š§ : '+str(forecast['avghumidity'])+'%'+"\nWill It Rain "+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' š§ : '+yes_or_no[str(forecast["daily_will_it_rain"])]+'\nChance Of Rain '+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' š§ : '+str(forecast['daily_chance_of_rain'])+'%'+"\nWill It Snow "+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' šØ : '+yes_or_no[str(forecast["daily_will_it_snow"])]+'\nChance Of Snow '+the_name_of_each_day[answer_choose_the_day_of_the_daily_forecast]+' šØ : '+str(forecast['daily_chance_of_snow'])+'%'+'\nTotal Precipitation š§ : '+str(forecast['totalprecip_mm'])+'MM'+'\nTotal Precipitation š§ : '+str(forecast['totalprecip_in'])+'Inches')                                                        
        except : 
            bot.reply_to(message,'š“š“ Make sure the city name you entered is correct š“š“')
    
    elif message.text == 'return to the forecast page š' :
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('ā³ Daily Forecast ā³')
        markup.row('š„ Hourly Daily Forecast š„')
        markup.row('š Day And Night Times š\nFor Example[ sunrise : 5:55 ]')
        markup.row('š Changing the name of the city š')
        markup.row('Return to main page ā©ļø','Return to the previous page š')
        bot.send_message(chat_id,'Return to forecast page was successful ā',reply_markup=markup)

    elif message.text == 'return to the daily forecast list page š' : 
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row("š® Today's weather forecast š®")
        markup.row("š® Tomorrow's weather forecast š®")
        markup.row("š® The weather forecast for the day after tomorrow š®")
        markup.row('Return to main page ā©ļø','Return to the forecast page š')
        bot.send_message(chat_id,'Return to daily forecast list page was successful ā',reply_markup=markup)


    elif message.text == 'š„ hourly daily forecast š„' : 

        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('š„ Hourly Forecast Today š„')
        markup.row('š„ Hourly Forecast For Tomorrow š„')
        markup.row('š„ Hourly Forecast The Day After Tomorrow š„')
        markup.row('Return to main page ā©ļø','Return to the forecast page š')
        bot.send_message(chat_id,'š Choose one of the options below š',reply_markup=markup)
    
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
        markup.row('Return to main page ā©ļø','Return to the hourly daily forecast page š')
        bot.send_message(chat_id,'ā¼ļø Select one of the following hours and you will receive the weather forecast for that hour according to the selected time frame ā¼ļø',reply_markup=markup)
      
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

            bot.reply_to(message,'Country Name š : '+location['country']+'\nRegion šŗ : '+location['region']+'\nCity Name š : '+location['name']+"\n------------------------------------------------------"+'\nForecast Date š : '+str(date1['date'])+'\n'+condition['text']+' At '+hour2+' '+sticker[condition['text']]+"\nTemperature š” : "+str(forecast['temp_c'])+"Ā°C"+"\nFeels Like š» : "+str(forecast['feelslike_c'])+"Ā°C"+"\nThe Heat We Feel āØļø : "+str(forecast['heatindex_c'])+'Ā°C'+"\nTemperature š” : "+str(forecast['temp_f'])+"Ā°F"+"\nFeels Like š» : "+str(forecast['feelslike_f'])+"Ā°F"+"\nThe Heat We Feel āØļø : "+str(forecast['heatindex_f'])+'Ā°F'+"\nWind Speed At "+hour2+" š¬ : "+str(forecast['wind_kph'])+"KPH"+"\nWind Speed At "+hour2+" š¬ : "+str(forecast['wind_mph'])+"MPH"+"\nWind Temperature š” : "+str(forecast['windchill_c'])+'Ā°C'+"\nWind Temperature š”: "+str(forecast['windchill_f'])+'Ā°F'+"\nWind Direction š§­ : "+str(forecast["wind_dir"])+"\nPressure In Inches š« : "+str(forecast["pressure_in"])+"\nWill It Rain "+the_name_of_each_day_2[hour4]+' At '+hour2+' š§ : '+yes_or_no[str(forecast["will_it_rain"])]+'\nChance Of Rain '+the_name_of_each_day_2[hour4]+' At '+hour2+' š§ : '+str(forecast['chance_of_rain'])+'%'+"\nPrecipitation Amount š§ : "+str(forecast['precip_mm'])+"MM"+"\nPrecipitation Amount š§ : "+str(forecast['precip_in'])+"Inches"+"\nWill It Snow "+the_name_of_each_day_2[hour4]+" At "+hour2+' šØ : '+yes_or_no[str(forecast["will_it_snow"])]+'\nChance Of Snow '+the_name_of_each_day_2[hour4]+' At '+hour2+' šØ : '+str(forecast['chance_of_snow'])+'%')                                                                                                                                                                
        except : 
            bot.reply_to(message,'š“š“ Make sure the city name you entered is correct š“š“')

    elif message.text == 'return to the hourly daily forecast page š':
        chat_id = message.chat.id
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('š„ Hourly Forecast Today š„')
        markup.row('š„ Hourly Forecast For Tomorrow š„')
        markup.row('š„ Hourly Forecast The Day After Tomorrow š„')
        markup.row('Return to main page ā©ļø','Return to the forecast page š')
        bot.send_message(chat_id,'Return to hourly daily forecast page was successful ā',reply_markup=markup)

    elif message.text == "š day and night times š\nfor example[ sunrise : 5:55 ]" :
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




            bot.reply_to(message,'Country Name š : '+location['country']+'\nRegion šŗ : '+location['region']+'\nCity Name š : '+location['name']+"\n------------------------------------------------------"+'\nDate š : '+str(date1['date'])+"\nSunrise š : "+str(forecast['sunrise'])+"\nSunset š : "+str(forecast['sunset'])+"\nMoonrise š : "+str(forecast['moonrise'])+'\nMoonset š : '+str(forecast['moonset'])+'\nMoon phases : '+str(forecast['moon_phase'])+'\nMoon illumination : '+str(forecast['moon_illumination'])+"%"+"\n------------------------------------------------------"+'\nDate š : '+str(date11['date'])+"\nSunrise š : "+str(forecast1['sunrise'])+"\nSunset š : "+str(forecast1['sunset'])+"\nMoonrise š : "+str(forecast1['moonrise'])+'\nMoonset š : '+str(forecast1['moonset'])+'\nMoon phases : '+str(forecast1['moon_phase'])+'\nMoon illumination : '+str(forecast1['moon_illumination'])+"%"+"\n------------------------------------------------------"+'\nDate š : '+str(date12['date'])+"\nSunrise š : "+str(forecast2['sunrise'])+"\nSunset š : "+str(forecast2['sunset'])+"\nMoonrise š : "+str(forecast2['moonrise'])+'\nMoonset š : '+str(forecast2['moonset'])+'\nMoon phases : '+str(forecast2['moon_phase'])+'\nMoon illumination : '+str(forecast2['moon_illumination'])+"%")                                                                                                  
        except : 
            bot.reply_to(message,'š“š“ Make sure the city name you entered is correct š“š“')
    
    elif  message.text =='š changing the name of the city š': 
        chat_id = message.chat.id
        text = "`" +"The name of the new city : "+ "`"
        bot.reply_to(message,"š“š“ IMPORTANT š“š“\nTo change the name of the desired city,click on the text below and paste it and add the name of the desired city to the end of the text.")
        bot.send_message(chat_id,text,parse_mode='MarkdownV2')
        
    
    elif  'the name of the new city' in message.text :
            try:
                update_city_name = message.text.replace("the name of the new city","")
                update_city_name = update_city_name.replace(":","")
                city_name = update_city_name
                city_name_test_v2 = city_name.replace(" ","")
                city_name_test_v2 = city_name_test_v2[0] , city_name_test_v2[1]
                if city_name_test_v2[0]  not in Alphabet :
                    bot.reply_to(message,"Rename was failed ā")
            
                elif city_name_test_v2[1] not in Alphabet : 
                    bot.reply_to(message,"Rename was failed ā")

                elif city_name_test_v2[0] in Alphabet : 
                   
                    bot.reply_to(message,"Rename was successfully ā\nNew City Name : "+city_name.title())
            except: 
                bot.reply_to(message,"Rename was failed ā")
        
"----------------------------------------------------------------------------------------------------------"
bot.polling(none_stop=True)
