from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/DevOps/Class 2/chromedriver_win32/chromedriver.exe')
# driver.get("http://www.facebook.com")
# print(driver.current_url)
# print(driver.title)
# if driver.title == 'Facebook - Log In or Sign Up':
#     print('yes')
# else:
#     print('no')

#a = driver.page_source
#print(a) # לכתוב את זה לקובץ
#print(driver.find_element_by_id('u_0_z'))


driver.get("https://translate.google.com")
a = driver.find_element_by_xpath("/html/body[@class='displaying-homepage']/div[@class='frame']/div[@class='page tlid-homepage homepage translate-text']/div[@class='homepage-content-wrap']/div[@class='tlid-source-target main-header']/div[@class='source-target-row']/div[@class='tlid-input input']/div[@class='source-wrap']/div[@class='input-full-height-wrapper tlid-input-full-height-wrapper']/div[@class='source-input']/div[@id='input-wrap']/textarea[@id='source']")
print(a)
driver.quit()