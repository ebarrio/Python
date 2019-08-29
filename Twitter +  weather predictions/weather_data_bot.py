from weather_miner_bot import Weather_Miner_Bot
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

import os
import time

secs_delay = 1

class Twitter_Bot:
    def __init__(self, acc, passw):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.minimize_window()
        self.acc = acc
        self.passw = passw
        self.Weather_bot = Weather_Miner_Bot()
        self.Weather_bot.refresh_data()
        self.fechas = self.Weather_bot.get_fechas()
        self.altura = self.Weather_bot.get_metros()
        self.viento = self.Weather_bot.get_viento()
        self.Weather_bot.clear()
        print(self.fechas)
    
    def print_all_data(self):
        print("\n ---------------- FECHAS ALMACENADAS ------------------- \n")
        print(self.fechas)
        print("\n ----------- ALTURAS DE LAS OLAS ALMACENADAS ----------- \n")
        print(self.altura)
        print("\n--------- VELOCIDAD DEL VIENTO ALMACENADAS ------------- \n")
        print(self.viento)

    def get_altura_maxima(self, pos_inicio, pos_final):
        max = self.altura[pos_inicio]
        pos = pos_inicio
        for i in range(pos_inicio,pos_final):
            if(max < self.altura[i]):
                max = self.altura[i]
                pos = i
        return pos
    def weather_to_post(self):
        post = []
        day1 = self.get_altura_maxima(1,24)
        day2 = self.get_altura_maxima(25,48)
        day3 = self.get_altura_maxima(48,72)
        print(day3)
        a = [self.fechas[day1], self.altura[day1], self.viento[day1]]
        post.append(a)
        b = [self.fechas[day2], self.altura[day2], self.viento[day2]]
        post.append(b)
        c = [self.fechas[day3], self.altura[day3], self.viento[day3]]
        post.append(c)
        return post
    def get_tweet_strings(self):
        tweets = []
        data = self.weather_to_post()

        tweet_1 = data[0][0][:10] + ": La mejor hora para surfear hoy es las " + data[0][0][11:16]
        tweet_1 += ". Habrá olas de " + data[0][1] + " metros con un viento de " + data[0][2] + " m/s."

        tweet_2 = data[1][0][:10] + ": Para mañana el pronostico de olas es "
        tweet_2 += "de " + data[1][1] + " metros con un viento de " + data[1][2] + " m/s "
        tweet_2 += "a las " + data[1][0][11:16] + " horas."

        tweet_3 = data[2][0][:10] + ": Pasado mañana la mejor hora para surfear según las predicciones meteorologicas serán las " + data[2][0][11:16]
        tweet_3 += ". Las olas tendran una altura de " + data[2][1] + " metros con un viento de " + data[2][2] + " m/s."

        print(tweet_1)
        print(tweet_2)
        print(tweet_3)

        tweets = [tweet_1, tweet_2, tweet_3]
        return(tweets)

    def post_tweets(self):
        tweets = self.get_tweet_strings()
        self.driver.maximize_window()
        self.driver.get('https://tweetdeck.twitter.com')
        time.sleep(secs_delay)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/section/div[1]/a').click()
        time.sleep(secs_delay)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div[2]/div/input').send_keys(self.acc)
        time.sleep(secs_delay)
        p = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div[2]/div/input')
        p.send_keys(self.passw)
        time.sleep(secs_delay)
        p.send_keys(Keys.ENTER)
        

        for i in range(len(tweets)):
            time.sleep(2*secs_delay)
            bt = self.driver.find_element_by_xpath('/html/body/div[3]/header/div/button/i')
            bt.click()
            time.sleep(secs_delay)
            tweet_box = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div/div/div/div[1]/div[7]/textarea')
            tweet_box.send_keys(tweets[i])
            time.sleep(secs_delay)
            self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div/div/div/div[1]/div[12]/div/div/button').click()

Tw_bot = Twitter_Bot('@PronosticosSurf' , '<-- Follow me')
Tw_bot.post_tweets()
