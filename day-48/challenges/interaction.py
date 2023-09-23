from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')
driver.maximize_window()

# total_articles = driver.find_element(By.CSS_SELECTOR, value='#articlecount a:first-child')
# total_articles.click()
# all_portals = driver.find_element(By.LINK_TEXT, value='Create account')
# all_portals.click()

search = driver.find_element(By.ID, value='searchInput')
search.send_keys('Pokemon')
search.send_keys(Keys.ENTER)

# driver.quit()