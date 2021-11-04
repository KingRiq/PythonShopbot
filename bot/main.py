# coding=utf-8
import time
import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Time, Timestamp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import sched
import time
import os
import config_file
from configparser import ConfigParser
import configparser

global driver
driver = webdriver.Chrome('./chromedriver')

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
        except Error:
            #I predict we have reached a captcha here and want to check if an error is thrown
            #if so then notify the user to do the captcha
            notify("Error", "Something went wrong press enter on terminal when finished")
            text = input("How? Sway")
            notify("Now we are back on track", "Let's finish where we left off!")
            driver.refresh()

#same procedure I just need to check if an element exists
def checkvalid2(string):
        try:
            signup = driver.find_element_by_id(string)
        except Error:
            #I predict we have reached a captcha here and want to check if an error is thrown
            #if so then notify the user to do the captcha
            notify("Error", "Something went wrong press enter on terminal when finished")
            text = input("How? Sway")
            notify("Now we are back on track", "Let's finish where we left off!")
            driver.refresh()

def login(username1, password1):
    #ensure current window is right
    mainwindow = driver.current_window_handle
    
    #now log in
    driver.get("https://shop.telfar.net/account/login")
    username = driver.find_element_by_id("CustomerEmail")
    username.send_keys(username1)
    password = driver.find_element_by_id("CustomerPassword")
    password.send_keys(password1)
    global signup
    signup = driver.find_element_by_class_name("btn")
    time.sleep(1)
    signup.click() 
    time.sleep(1)

    #validate tht e are in the right place
    name = driver.current_url
    name1 = "https://shop.telfar.net/account"

    if name == 'https://shop.telfar.net/account':
        notify("Login Successful", "Were in boiz")
    else:
        check_Captcha(name)
    schedule()

def check_Captcha(string) :
    if string == 'https://shop.telfar.net/challenge':
        notify("check for captcha", "I think a captcha is here press enter in terminal to continue")
        input('press enter to continue')
        notify("Now we are back on track", "Let's finish where we left off!")
    
#schedule for the allotted time.
def schedule():
    scheduler = sched.scheduler(time.time, 
    time.sleep)

    # Schedule when you want the action to occur
    t =time.strptime('Fri Nov 04 07:59:55 2021') #I will make this user friendly later!
    t= time.mktime(t)
    scheduler.enterabs(t, 0, main)

    #dont start until I say too!
    scheduler.run() 

def main():
    global buy 

    # navigate to the item in question
    driver.get("https://shop.telfar.net/collections/upcoming-drop/products/small-yellow-shopping-bag")
    print('adding to cart')
    atc = 'AddToCart'
    checkvalid(atc)
    time.sleep(1)

    # Ready to checkout
    print('ready for checkout')
    driver.get("https://shop.telfar.net/cart")
    
    
    
    buy = driver.find_element_by_name('checkout')
    buy.click()
    check_Captcha(driver.current_url)
    print('enter your information yourself until I improve the script')
    dropdown = 'checkout_shipping_address_id'
    checkvalid2(dropdown)
    buy = driver.find_element_by_id('continue_button')
    notify("Almost done", "if the code fails just continue yourself to save time!")
    buy.click()
    time.sleep(1)
    buy = driver.find_element_by_id('continue_button')
    buy.click()
    time.sleep(1)

    #this was used before we made a static account this was used to register
    '''
    buy.send_keys('///')
    buy = buy.send_keys(Keys.TAB)
    buy = driver.switch_to.active_element
    buy.send_keys('///')
    buy = buy.send_keys(Keys.TAB*2)
    buy = driver.switch_to.active_element
    buy.send_keys('///')
    buy.send_keys(Keys.TAB*2)
    buy = driver.switch_to.active_element
    buy.send_keys('Winnipeg')
    buy.send_keys(Keys.TAB)
    buy = driver.switch_to.active_element
    buy.send_keys(Keys.DOWN)
    drop = Select(buy)
    drop.select_by_visible_text('Canada')
    buy.send_keys(Keys.ENTER)
    buy.send_keys(Keys.TAB)
    buy = driver.switch_to.active_element
    buy.send_keys(Keys.DOWN)
    drop = Select(buy)
    drop.select_by_visible_text('Manitoba')
    buy.send_keys(Keys.ENTER)
    buy.send_keys(Keys.TAB)
    buy = driver.switch_to.active_element
    buy.send_keys('///')
    buy.send_keys(Keys.TAB)
    buy = driver.switch_to.active_element
    buy.send_keys('12043903822')
    buy.send_keys(Keys.TAB*3)
    buy = driver.switch_to.active_element
    buy.send_keys(Keys.ENTER)'''

'''
    firstname = driver.find_element_by_xpath('//*[@id="FieldWrapper-6"]')
    firstname.click()
    firstname.send_keys("Saira")
    lastname = driver.find_element_by_xpath('//*[@id="FieldWrapper-7"]')
    lastname.send_keys("Hampton")
    email = driver.find_element_by_xpath('//*[@id="FieldWrapper-8"]')
    email.send_keys("blank")

    phone = driver.find_element_by_xpath('//*[@id="FieldWrapper-10"]')
    phone.send_keys("4563453456")
    passwords = driver.find_element_by_xpath('//*[@id="FieldWrapper-11"]')
    passwords.send_keys("1111111111")
    signup = driver.find_element_by_xpath('//*[@id="sign-up-submit-button"]/div/span/div')
'''

#this is a function Ill never use for this purpose it was merely to check if I can make mass number of emails (protip I cant because of captcha v3 atm)
def email():
    #create email
    driver = webdriver.Chrome(executable_path='/Users/riq/PycharmProjects/DDAutomation/chromedriver')
    mainwindow = driver.current_window_handle
    driver.get("http://www.protonmail.com")
    signup1 = driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul/li[9]/a')
    signup1.click()
    driver.implicitly_wait(100)
    bar = driver.find_element_by_xpath('//*[@id="signup-plans"]/div[5]/div[1]/div[1]/div')
    bar.click()
    free = driver.find_element_by_xpath('//*[@id="freePlan"]')
    free.click()

    passuser = driver.find_element_by_xpath('//*[@id="password"]')
    passuser.send_keys("placeholder")
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
        (By.XPATH, "//div[@class='usernameWrap']//iframe[@title='Registration form']")))
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class='input' and @id='username']"))).send_keys("riqboy2323")
    driver.switch_to.default_content()
    passuser = driver.find_element_by_xpath('//*[@id="passwordc"]')
    passuser.send_keys("placeholder")
    passuser.send_keys(Keys.ENTER)
    create = passuser
    create.click()
    confirm = driver.find_element_by_xpath('//*[@id="confirmModalBtn"]')
    confirm.click()
    input("Press enter when you are done with captcha")
    #driver.switch_to_window(mainwindow)

    

notify("Hi", "Good morning!")
if not os.path.exists('../../config'):
    exit()

file = '../../config/config.ini'
config = ConfigParser()
config.read(file)
username = config.get('Account', 'username')
password = config.get('Account', 'password')

driver = login(username, password)
print('process complete!')
notify("Process Complete", "Complete")
#sql_connection()


#typically the website will generate a captcha at specific times although unpredictable I probably can figure out when one appears by checking if a captcha element is present.