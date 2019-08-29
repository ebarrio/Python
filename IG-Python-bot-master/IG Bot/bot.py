from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import os
import time


class InstagramBot:
    
    def __init__(self, username, password, niche):
        """
        __init__ :
        Initializes an instance of the InstagramBot and login
        Args:
            username:str: the instagram username
            password:str: the instagram password for a user

        """
        self.username = username
        self.password = password
        self.total_likes = 0
        self.total_errors = 0
        self.niche = niche
        self.driver = webdriver.Chrome('chromedriver.exe')
        
        self.login()


    def login(self):

        """
        login:
        """
        # Get to instagram with webdriver
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(1)
        self.driver.fullscreen_window()
        time.sleep(1)
        # Set user y and password
        self.driver.find_element_by_name('username').send_keys(self.username)
        time.sleep(1)
        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        #Click: "Iniciar sesion" (Log in)
        self.driver.find_element_by_xpath("//div[contains(text(),'Iniciar ses')]").click() 
        time.sleep(5)
        #Click boton: No notification message
        #self.driver.find_element_by_class_name('a001WC').click()
        #time.sleep(1)


    def likes_tag(self,tag,num_likes):
        """
        likes_tag:
            Args:
            tag:string: Hastag to search
        """
        #Get to hashtag page
        self.driver.get('https://www.instagram.com/explore/tags/' + tag)
        time.sleep(2)

        #Open - like - close photo loop:
        for num in range(0,num_likes) :
            try:
                #Click photo
                self.driver.find_elements_by_class_name('eLAPa')[num].click()
                time.sleep(1)

                #Try to like
            
                self.driver.find_element_by_class_name('dCJp8').click()
                time.sleep(1)
                

                #Close photo
                self.driver.find_element_by_class_name('ckWGn').click()
                time.sleep(1)

                self.total_likes += 1

            except (NoSuchElementException, IndexError, ElementClickInterceptedException):
                self.total_errors += 1
                break
        
        self.print_stats


    def close_bot(self):
        ## Close Chrome Explorer:
        self.driver.quit()


    def get_tags(self,txt_file, num_likes):

        #Read .txt file, search hashtags and like num_likes times:
        text_file = open(txt_file, "r")
        raw = text_file.readlines()
        raw_len = len(raw)

        #Search hashtags in all the .txt file
        for i in range(raw_len):
            ## Filter hastags and qwerty chars (? == asian char):
            if raw[i][0] == '#' :
                #print(raw[i][1:])
                if raw[i][1] != '?' :
                    self.likes_tag(raw[i][1:],num_likes)

        text_file.close()
    

    def like_all_tags(self,num_likes):
        self.get_tags('tags_surf_0.txt',num_likes)
        self.get_tags('tags_raw_0.txt',num_likes)
        self.get_tags('tags_raw_1.txt',num_likes)
        self.get_tags('tags_raw_2.txt',num_likes)
        self.get_tags('tags_raw_3.txt',num_likes)
        self.get_tags('tags_raw_4.txt',num_likes)
        self.get_tags('tags_raw_5.txt',num_likes)
        self.get_tags('tags_raw_6.txt',num_likes)
        self.get_tags('tags_raw_7.txt',num_likes)
        self.get_tags('tags_raw_8.txt',num_likes)
        self.get_tags('tags_raw_9.txt',num_likes)
    
    def like_surf_niche(self,num_likes):
        self.get_tags('tags_surf_0.txt',num_likes)

    def print_stats(self):
        print('Likes in ' + self.username + ': ' + str(self.total_likes) + ' with ' + str(self.total_errors) + ' errors')


    def follow_users(self, num_follows, user_to_search):
        try:
            self.driver.get("https://www.instagram.com/" + user_to_search + "/")
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
            time.sleep(1)
            for i in range(1,num_follows):
                self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/div/li[" + str(i) + "]/div/div[2]/button").click()
                time.sleep(5)
        except (NoSuchElementException, IndexError, ElementClickInterceptedException):
            print("Error following in user to serach: " +  user_to_search)


    def follow_user_surf_niche(self, num_follows) :
        self.follow_users(num_follows, "billabong")
        self.follow_users(num_follows, "elementskateboards")

    def unfollow_users(self,num_unfollows):
        try:
            self.driver.get("https://www.instagram.com/" + self.username + "/")
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
            time.sleep(1)
            #/html/body/div[3]/div/div[2]/ul/div/li[2]/div/div[2]/button
            #/html/body/div[3]/div/div[2]/ul/div/li[1]/div/div[3]/button
            if (num_unfollows > 0):
                for i in range(1, num_unfollows):

                    self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li['+ str(i) +']/div/div[3]/button').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
                    time.sleep(1)

        except (NoSuchElementException, IndexError, ElementClickInterceptedException):
            print('Error in unfollow number:' + str(i))


    def instagram_rutine(self, num_likes, num_follow_page, num_unfollows):
        self.follow_user_surf_niche(num_follow_page)
        self.like_surf_niche(num_likes)


if __name__ == '__main__':

    num_follows_page = 20
    num_likes_tag = 2
    num_unfollows = 0

    #Declare bot:
    ig_bot = InstagramBot('user', 'pass','niche')

    # Execute rutine:
    ig_bot.instagram_rutine(num_likes_tag, num_follows_page, num_unfollows)

    #UnfolloW users:
    ig_bot.unfollow_users(num_unfollows)

    # Print bot stats
    ig_bot.print_stats()

    #Close Chrome Explorer
    ig_bot.close_bot()