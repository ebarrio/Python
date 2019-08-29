from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

import os
import time

secs_delay = 1


class Weather_Miner_Bot:
    def __init__ (self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.fecha = []
        self.metros = []
        self.viento = []
        time.sleep(secs_delay)
        self.driver.maximize_window()
        time.sleep(secs_delay)

    def refresh_data(self):
        self.driver.get('https://bancodatos.puertos.es/TablaAccesoSimplificado/?p=622028053&name=Valencia')
        time.sleep(secs_delay)
        raw_data = self.driver.find_elements_by_class_name('datacell')
        for i in range(0, len(raw_data) - 8 ,8):
            if(raw_data[i].text != ''):
                self.fecha.append(raw_data[i].text)
                self.viento.append(raw_data[i+2].text)
                self.metros.append(raw_data[i+4].text)

    def get_fechas(self):
        return self.fecha

    def get_metros(self):
        return self.metros

    def get_viento(self):
        return self.viento

    def clear(self):
        self.driver.close()

