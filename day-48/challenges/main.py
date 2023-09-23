from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')
driver.maximize_window()
print(driver)

events_dict = {}

events = driver.find_elements(By.CSS_SELECTOR, value='.event-widget .shrubbery .menu li')
for index, event  in enumerate(events):
    event_name = event.find_element(By.TAG_NAME, value='a').text
    event_time = event.find_element(By.TAG_NAME, value='time').text
    events_dict[index] = {'time': event_time, "name": event_name}
    
print(events_dict)
driver.quit()