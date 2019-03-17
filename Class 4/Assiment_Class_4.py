from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driverChrome = webdriver.Chrome(executable_path='C:/DevOps/Class 2/chromedriver_win32/chromedriver.exe')
#driverFirefox = webdriver.Firefox(executable_path='C:/DevOps/Class 4/geckodriver-v0.24.0-win64/geckodriver.exe')
driverChrome.implicitly_wait(10)
#1
driverChrome.get("http://www.walla.co.il")
driverChrome.maximize_window()
#
# #driverFirefox.get("http://www.ynet.co.il")
# #2
# #a
# webSiteTitle = driverChrome.title
# print(webSiteTitle)
# #b
# driverChrome.refresh()
# #c
# if webSiteTitle == driverChrome.title:
#     print("Equal")
# else:
#     print("Not Equal")
#
# #3
# # Yes they are the same
#
# # #4
# driverChrome.get("https://translate.google.com")
# writeText = driverChrome.find_element_by_id("source")
# writeText.send_keys("איך אומרים שלום באנגלית")
#
# # #5
# driverChrome.get("https://www.youtube.com")
# songSearch = driverChrome.find_element_by_name("search_query")
# songSearch.send_keys("bruce springsteen born in the usa")
# sendSongSearch = driverChrome.find_element_by_id("search-icon-legacy")
# sendSongSearch.click()
#
# #6
# driverChrome.get("https://translate.google.com")
# a = driverChrome.find_element_by_id("sugg-item-en")
# b = driverChrome.find_element_by_class_name("goog-inline-block")
# c = driverChrome.find_elements_by_xpath("//*[@id="sugg-item-en"]")
# print(ש)
# #7
# driverChrome.get("https://www.facebook.com")
# enterUser = driverChrome.find_element_by_id("email")
# enterUser.send_keys("eladadi@gmail.com")
# enterPassword = driverChrome.find_element_by_id("pass")
# enterPassword.send_keys("jlkj4567")
# pressLogIn = driverChrome.find_element_by_id("u_0_2")
# pressLogIn.click()
#
# #8
# driverChrome.get("https://www.facebook.com")
# driverChrome.delete_all_cookies()
# cookiesListNames = driverChrome.get_cookies()
# print(cookiesListNames)
#
# #9
# driverChrome.get("https://github.com")
# gitSearch = driverChrome.find_element_by_class_name("form-control")
# gitSearch.send_keys("Selenium")
# gitSearch = driverChrome.find_element_by_class_name("form-control").send_keys(Keys.ENTER)
