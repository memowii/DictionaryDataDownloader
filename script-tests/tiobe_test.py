from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.tiobe.com/tiobe-index')
table = driver.find_element_by_tag_name('table')
rows = table.find_elements_by_tag_name('tr')
tds = rows[1].find_elements_by_tag_name('td')
#for row in rows
#print(len(tds))
for td in tds:
	print(td.text)
driver.close()