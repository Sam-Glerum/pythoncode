from selenium import webdriver

url = 'https://google.com'

browser = webdriver.Firefox()
browser.close()
browser.get(url)
browser.maximize_window()