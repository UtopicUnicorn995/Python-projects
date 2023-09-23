from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from amazoncaptcha import AmazonCaptcha


ROBOT_RESPONSE = "Sorry, we just need to make sure you're not a robot. For best results, please make sure your browser is accepting cookies."
robot_check = True

ua = UserAgent()
user_agent = ua.random

# chrome_option = Options()
# chrome_option.add_argument(f'--user-agent={user_agent}')
#keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument(f'--user-agent={user_agent}')

# Webdriver will be driving the browser
while robot_check == True:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.amazon.com/Cuckoo-CRP-P0609S-Cooker-10-10-11-60/dp/B01JRTZVVM/ref=sr_1_4?qid=1611738512&sr=8-4')
    page_text = driver.find_element(By.CLASS_NAME, value='a-last').text
    captcha = AmazonCaptcha.fromdriver(driver)
    solution = captcha.solve()
    driver.quit()
    if page_text != ROBOT_RESPONSE:
        robot_check = False
  
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.amazon.com/Cuckoo-CRP-P0609S-Cooker-10-10-11-60/dp/B01JRTZVVM/ref=sr_1_4?qid=1611738512&sr=8-4')
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
 
# print(f"The price is {price_dollar}.{price_cents}")

# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar)
# button = driver.find_element(By.ID, value='submit')
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link)
# XPath
xPath = driver.find_element(By.XPATH, value='//*[@id="a-autoid-10"]')
print(xPath)
# # driver.close() will close the tab
# driver.close()
# # driver.close() will close the browser
driver.quit()