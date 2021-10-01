# coding=utf-8
import time
import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Time, Timestamp



import sqlite3
from sqlite3 import Error
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def sql_init():

    try:

        con = sqlite3.connect("SairaUsernames.db")

        print("Connection is established: To saira's database")

    except Error:

        print(Error)

    finally:

        con.close()


def main():
    global driver
    driver = webdriver.Chrome(executable_path='/Users/riq/PycharmProjects/DDAutomation/chromedriver')
    mainwindow = driver.current_window_handle
    driver.get("https://shop.telfar.net/collections/upcoming-drop/products/small-bubblegum-pink-shopping-bag?variant=32457570418787")
    p = True
    timeout = 0
    while p is True and timeout < 5:
        try:
            signup = driver.find_element_by_id('AddToCart')
            if signup.is_enabled():
                signup.click()
                break
            else:
                from sys import exit
                timeout +=1
                if timeout >= 5:
                    print("The item is definitely sold out")
                    exit()
                driver.refresh()
        except Error:
            driver.refresh()
            timeout+= 1
        

    
    time.sleep(1)
    driver.get("https://shop.telfar.net/cart")
    driver.refresh()
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

    return driver

def init_sql_table():
    
    #id = is the temp key
    #name = the name of the poster
    #message = the message
    connection.execute ("""
        Create table if not exists log(
        day integer PRIMARY KEY,
	    name text NOT NULL,
        password text NOT NULL
        );
    """)

def exe_sql(day, name, password):
    # add the new entry
    connection.execute("insert into log(day,name,password) values (?,?,?)", (day,name, password))
    connection.commit()


import sched
import time
  
from datetime import datetime
# Creating an instance of the
# scheduler class
scheduler = sched.scheduler(time.time, 
                            time.sleep)
import datetime
def hello():
    print('hi')
# Schedule when you want the action to occur
#s = str(datetime.datetime.now())
s = time.time()
s1 = datetime.datetime.now()
print(s)
print(s1)
t =time.strptime('Tue Sep 28 22:41:00 2021')
t= time.mktime(t)
print(t)
scheduler.enterabs(t, 0, main)
scheduler.run()


'''
def print_event(name):
    print('EVENT:', time.time(), name)

now = time.time()
print('START:', now)

scheduler.enterabs(now+2, 2, print_event, ('first',))
scheduler.enterabs(now+5, 1, print_event, ('second',))

scheduler.run()'''

'''connection = sqlite3.connect("365email.db")
init_sql_table()
password = 'sairaa1!'
default_username = "realemailday" 
for i in range(1, 366): 
    username = default_username + str(i)
    print(username)
    exe_sql(i,username,password)
connection.close


from datetime import *

day_of_year = (datetime.now().timetuple().tm_yday)
N_DAYS_AGO = day_of_year -1
today = datetime.now()    
n_days_ago = today - timedelta(days=N_DAYS_AGO)

cursor =connection.cursor().execute("SELECT * FROM log WHERE day=?", (day_of_year,))
print(cursor.fetchone())'''
'''
driver = webdriver.Chrome(executable_path='/Users/riq/PycharmProjects/DDAutomation/chromedriver')
mainwindow = driver.current_window_handle
driver.get("http://www.starbucks.com/create")'''
#sql_connection()