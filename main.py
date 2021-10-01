# coding=utf-8
import time
import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Time, Timestamp
import d

"""def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/"""

import sqlite3
from sqlite3 import Error
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def sql_connection():

    try:

        con = sqlite3.connect("SairaUsernames.db")

        print("Connection is established: To saira's database")

    except Error:

        print(Error)

    finally:

        con.close()


def main():
    driver = webdriver.Chrome(executable_path='/Users/riq/PycharmProjects/DDAutomation/chromedriver')
    mainwindow = driver.current_window_handle
    driver.get("https://shop.telfar.net/collections/t-shirts/products/telephone-long-sleeve-t-off-black")
    signup = driver.find_element_by_id('AddToCart')
    signup.click()
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

driver = main()
sql_connection()