#title: Automate Testing For BITS
#Author: Tandin Wangchuk
#Discription : BITS Admin
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
# driver.get("http://10.11.1.13/bits/")
driver.get("https://bits.drc.gov.bt/bits/")