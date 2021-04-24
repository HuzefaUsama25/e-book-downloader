import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import webbrowser


options = webdriver.ChromeOptions()
options.add_argument('--headless')

browser = webdriver.Chrome(options=options)  

base_url = 'https://b-ok.asia/s/'
query = input("query: ")+'/?language=english&extension=pdf&order=bestmatch'
url = base_url + query 

browser.get(url) 
time.sleep(3) 
body = browser.find_element_by_tag_name('body')
for _ in range(1): 
    body.send_keys(Keys.PAGE_DOWN) 
    time.sleep(0.1) 
time.sleep(0.5)
books = browser.find_elements_by_tag_name('h3')
n = 0
for book in books:
    print(book.text)
    print()
    n = n + 1
    if n == 10:
        break
ntodown = int(input("Which one two Download: "))
todown = books[ntodown-1].text
print("Downloading: "+'''"'''+str(todown)+'''"''')

x = books[ntodown-1]
x
x.click()

body = browser.find_element_by_tag_name('body')

for _ in range(1): 
    body.send_keys(Keys.PAGE_DOWN) 
    time.sleep(0.1) 
time.sleep(0.5)

try:
    x = browser.find_element_by_css_selector('a.btn.btn-primary.dlButton.addDownloadedBook')
    x = str(x.get_attribute("href"))
    print(x)
    webbrowser.open(x)
    browser.quit()
    exit()
except Exception as e:
    print("Downloads unavailable Try another book :( "+str(e))
    input()

input()

