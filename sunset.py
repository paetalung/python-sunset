# sunriseCheck.py
# https://paetalung.github.io/cv/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as soup


opt = webdriver.ChromeOptions()
opt.add_argument('headless') # hidden mode of chrome

driver = webdriver.Chrome(options=opt) # create driver

url = 'https://meteogram.org/sun/thailand/chumphon/'

driver.get(url) # open web
time.sleep(3)   # waiting 3 sec

page_html = driver.page_source
driver.close()

data = soup(page_html,'html.parser') # scan data

table = data.findAll('span',{'id':'sunset'})
out = str(table) # index on data

out = out.replace("[<span id=\"sunset\">","")
out = out.replace("</span>]","")

#print(out)

# Send line Section    
from songline import Sendline
token = '' # TEST TOKEN

sunrise = "SUNSET @ " + out

messenger = Sendline(token)
messenger.sendtext(sunrise)
