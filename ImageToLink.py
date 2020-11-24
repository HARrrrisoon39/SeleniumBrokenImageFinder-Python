import requests
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:\utility\chromedriver.exe')
# driver.get('https://pexels.com/')
driver.get('https://cbdbene.com/')
# images = driver.find_elements_by_tag_name('img')
# for image in images:
#     print(image.get_attribute('src'))

images = driver.find_elements_by_tag_name('img')
for image in images:
    if image.get_attribute('naturalWidth') == "0":
        print(image.get_attribute('src'))

    


# links = driver.find_elements_by_tag_name('a')
# for link in links:
#     r = requests.head(link.get_attribute('href'))
#     print(link.get_attribute('href'), r.status_code)

