# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import sched
import time
import os
import config_file
from configparser import ConfigParser
import configparser
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

global driver
driver = webdriver.Chrome()

#notify user of error becuase who knows what will happen
def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

#sometimes mistakes happen and it can happen either during login or during checkout or something
def checkvalid(string):
    signup = driver.find_element_by_id(string)
    p = True
    timeout = 0

    # try at maximum 61 times
    while p is True and timeout < 60:
        try:
            signup = driver.find_element_by_id(string)
            if signup.is_enabled():
                signup.click()
                break
            else:
                from sys import exit
                timeout +=1
                if timeout >= 10:
                    print("The item is definitely sold out")
                    exit()
                driver.refresh()
        except os.error:
            #I predict we have reached a captcha here and want to check if an error is thrown
            #if so then notify the user to do the captcha
            notify("Error", "Something went wrong press enter on terminal when finished")
            text = input("How? Sway")
            notify("Now we are back on track", "Let's finish where we left off!")
            driver.refresh()

def login(username, password):

    #ensure current window is right
    mainwindow = driver.current_window_handle
    
    #now log in
    driver.get("https://shop.telfar.net/account/login")
    username_field = driver.find_element_by_id("CustomerEmail")
    username_field.send_keys(username)
    password_field = driver.find_element_by_id("CustomerPassword")
    password_field.send_keys(password)
    signup = driver.find_element_by_class_name("btn")
    time.sleep(1)
    signup.click() 
    time.sleep(1)

    #validate tht e are in the right place
    name = driver.current_url

    if name == 'https://shop.telfar.net/account':
        notify("Login Successful", "Were in boiz")
    else:
        check_Captcha(name)

    # start purchase at the specified time (hardcoded)
    schedule()

# checks if at challenge webpge with captcha on it
def check_Captcha(string):

    if string == 'https://shop.telfar.net/challenge':
        
        notify("check for captcha", "I think a captcha is here press enter in terminal to continue")
        input('press enter to continue')
        notify("Now we are back on track", "Let's finish where we left off!")
    
#schedule for the allotted time.
def schedule():
    scheduler = sched.scheduler(time.time, 
    time.sleep)

    # Schedule when you want the action to occur (hardcoded for now)
    t=time.strptime('Fri Nov 04 07:59:55 2021')
    t= time.mktime(t)
    scheduler.enterabs(t, 0, purchase)

    # don't start until until its time!
    scheduler.run() 

def purchase():
    global buy # so selenium doesn't close when finished

    # navigate to the item in question
    time.sleep(1)
    driver.get(link)
    print('Adding to Cart')
    atc = 'AddToCart'
    checkvalid(atc)
    time.sleep(1)

    # Ready to checkout
    print('ready for checkout')
    driver.get("https://shop.telfar.net/cart")
    buy = driver.find_element_by_name('checkout')
    buy.click()
    check_Captcha(driver.current_url)
    buy = driver.find_element_by_id('continue_button')

    #navigate to payment
    notify("Almost done", "if the code fails just continue yourself to save time!")
    buy.click()
    time.sleep(1)
    buy = driver.find_element_by_id('continue_button')
    buy.click()
    time.sleep(1) 

def main():

    global link
    notify("Hi", "Good morning!")

    # make sure config exists
    if not os.path.exists('../../config'):
        exit() #quit silently for now


    # Access config file
    file = '../../config/config.ini'
    config = ConfigParser()
    config.read(file)
    username = config.get('Account', 'username')
    password = config.get('Account', 'password')

    # collect link from user (this is a design choice I rather have hardcoded)
    print("Post the link to the item you wish to purchase below!")
    link = input()

    # init
    login(username, password)

    # Terminate
    print('Process Complete!')
    notify("Process Complete", "Complete")

    

if __name__ == '__main__':
    main()
#typically the website will generate a captcha at specific times although unpredictable I probably can figure out when one appears by checking if a captcha element is present.