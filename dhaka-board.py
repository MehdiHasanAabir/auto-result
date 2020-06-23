from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


url = 'http://www.educationboardresults.gov.bd'

driver = webdriver.Chrome()
#driver.implicitly_wait(10)
driver.get(url)

#driver.find_element_by_name('value_s').send_keys('10')

#for drop down
Select(driver.find_element_by_name('exam')).select_by_value('ssc')
Select(driver.find_element_by_name('year')).select_by_value('2010')
Select(driver.find_element_by_name('board')).select_by_value('dhaka')


driver.find_element_by_name('roll').send_keys(103236)
driver.find_element_by_name('reg').send_keys(687057)


val = driver.find_elements_by_css_selector('td[valign]')[43].text
#print(val)
val = val.split(' ')
val = int(val[0]) + int(val[2])
driver.find_element_by_name('value_s').send_keys(val)


#print(driver.find_elements_by_tag_name('td')[43].text)
driver.find_element_by_css_selector('input[type="submit"]').click()
