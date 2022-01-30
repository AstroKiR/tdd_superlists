from selenium import webdriver
from selenium.webdriver.firefox.service import Service


service = Service('/home/akir/Projects/superlists/drivers/geckodriver')
browser = webdriver.Firefox(service=service)
browser.get('http://127.0.0.1:8000')

assert 'successfully' in browser.title

browser.quit()
