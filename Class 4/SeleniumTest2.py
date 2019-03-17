from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:/DevOps/Class 2/chromedriver_win32/chromedriver.exe')

driver.get("https://translate.google.com")
newTask = driver.find_element_by_id("source")
newTask.click()
newTask.clear()
newTask.send_keys("Problem")
driver.find_element_by_class_name("tl-more tlid-open-target-language-list")
#driver.find_element_by_class_name("language_list_item")
#driver.find_element_by_id("123").send_keys(Keys.ENTER)
#newTask.f
#newTask.clear()


# driver.get("https://translate.google.com")
# newTask = driver.find_element_by_id("source")
# newTask.click()
# newTask.clear()
# newTask.send_keys("Problem")
# print(newTask.is_displayed())

