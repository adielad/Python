from selenium import webdriver

driverChrome = webdriver.Chrome(executable_path='C:/DevOps/Class 2/chromedriver_win32/chromedriver.exe')

URL = "http://192.168.99.100:5000"
driverChrome.get(URL)
