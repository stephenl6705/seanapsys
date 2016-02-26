from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://innovation.seanapsys.com')

assert 'Django' in browser.title