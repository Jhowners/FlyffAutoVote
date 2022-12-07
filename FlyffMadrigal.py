from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import schedule
import time

usu = {'user': 'password'}

def autovote(usernameStr, passwordStr):
    website = 'http://flyffmadrigal.com.br/index.php'
    path = './chromedriver'
    driver = webdriver.Chrome(path)
    driver.get(website)
    time.sleep(1)

    username = driver.find_element(by='name', value='loginAccount')
    username.send_keys(usernameStr)
    password = driver.find_element(by='name', value='loginPassword')
    password.send_keys(passwordStr)
    loginbt = driver.find_element(by='name', value='loginSend')
    loginbt.click()

    websitevote = 'http://flyffmadrigal.com.br/index.php?site=vote'
    driver.get(websitevote)

    try:
        buttonvote = driver.find_element(by='id', value='voteFormOpener0')
        buttonvote.click()
        time.sleep(3)
        button = driver.find_element(by='name', value='submitVote0')
        button.click()
        print('User: ' + usernameStr + ' voted')
        logout = 'http://flyffmadrigal.com.br/index.php?site=vote&logout'
        driver.get(logout)
    except NoSuchElementException:
        logout = 'http://flyffmadrigal.com.br/index.php?site=vote&logout'
        driver.get(logout)
        print( usernameStr + ' Already voted')
        driver.close()
        
for x, v in usu.items():
    autovote(x, v)