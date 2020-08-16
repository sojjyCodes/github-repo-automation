import os
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://github.com/login')

print ("Opening Github")
time.sleep(1)
print('Opened Github')

usr = input('Enter Email/Username Id: ')
username_box = browser.find_element_by_id('login_field')
username_box.send_keys(usr)
print("Email Id entered")

pwd = input('Enter your password: ')
password_box = browser.find_element_by_id('password')
password_box.send_keys(pwd)
print("Passwored entered")

login_box = browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
login_box.click()
time.sleep(1)

'''
verify = webdriver.Chrome() 
verify.get('https://gmail.com')
print("Login to get your verification code")

ver_code = input("Enter your verification code: ")    
code = browser.find_element_by_id('otp')
code.send_keys(ver_code)

button = browser.find_element_by_xpath('//*[@id="login"]/div[3]/form/button')
button.click()
'''
# Note - You might need to uncomment the above if github prompt you to verify.

new_repo = browser.get('https://github.com/new')

repo_name = input("Enter the name of the repository: ")
print("Repo initialization is in progress 😴️😴️ ")

repo = browser.find_element_by_id('repository_name')
repo.send_keys(repo_name)
time.sleep(1)

print("Repository has been initialized sucessfully😎️🤑️ ")
create_repo = browser.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
create_repo.click()
browser.quit()