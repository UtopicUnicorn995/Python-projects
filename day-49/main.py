from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.ID, value='cookie')
buy_cursor = driver.find_element(By.ID, value='buyCursor')
buy_grandma = driver.find_element(By.ID, value='buyGrandma')
buy_mine = driver.find_element(By.ID, value='buyMine')
buy_shipment = driver.find_element(By.ID, value='buyShipment')
buy_alchemy = driver.find_element(By.ID, value='buyAlchemy lab')
buy_portal = driver.find_element(By.ID, value='buyPortal')
buy_time = driver.find_element(By.ID, value='buyTime machine')


upgrades = [buy_cursor, buy_grandma, buy_mine, buy_shipment, buy_alchemy, buy_portal, buy_time]

def checkUpgrade():
    money = int(driver.find_element(By.ID, value='money').text.replace(',', ''))
    print(money)
    for upgrade in upgrades:
        item = upgrade.find_element(By.TAG_NAME, value='b').text.split('- ')
        if money >= int(float(item[-1].replace(',', ''))):
            upgrade.click()
            break

while True:
    cookie.click()
    time.sleep(5)
    checkUpgrade()

    
