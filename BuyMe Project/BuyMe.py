#import relevant packages and classes for testing use
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#save chrome selenium webdriver in variable, open chrome browser
driverChrome = webdriver.Chrome(executable_path='C:/DevOps/Class 2/chromedriver_win32/chromedriver.exe')
#define element waiting time rule
driverChrome.implicitly_wait(10)

#open txt file and read the content to variable and open BuyMe internet page
webSiteFile = open("C:/DevOps/First Project/URL_WebSite.txt", 'r', encoding='UTF-8')
URL = webSiteFile.read()
driverChrome.get(URL)
# maximize browser window
driverChrome.maximize_window()

#save class element in variable and click on it(כניסה|הרשמה)
enterRegistrationWindow = driverChrome.find_element_by_class_name("seperator-link")
enterRegistrationWindow.click()


#
# #save class element in variable and click on it (הרשמה)
# enterRegistration = driverChrome.find_element_by_class_name("text-btn")
# enterRegistration.click()
#
# #save element in variable and print the name on inputBox
# firstName = driverChrome.find_element_by_id("ember1019")
# firstName.send_keys("Bruce")
#
# #save element in variable and print the email on inputBox
# email = driverChrome.find_element_by_id("ember1021")
# email.send_keys("BruceSpringsteen1984@gmail.com")
#
# password = driverChrome.find_element_by_id("valPass")
# password.send_keys("Abcd1234!")
#
#
# rePassword = driverChrome.find_element_by_id("ember1025")
# rePassword.send_keys("Abcd1234!")
#
#
# # because checkbox not clickable by python selenium i used "execute_script" to click the checkbox
# driverChrome.execute_script("arguments[0].click();", driverChrome.find_element_by_id("ember1026-id"))
#
#
# pressSingButton = driverChrome.find_element_by_class_name("ui-btn")
# pressSingButton.click()
#

# for enters without registration each Python script running
# enter mail
mailEnter = driverChrome.find_element_by_id("ember1005")
mailEnter.send_keys("BruceSpringsteen1984@gmail.com")

#enter password
passwordEnter = driverChrome.find_element_by_id("ember1007")
passwordEnter.send_keys("Abcd1234!")

#press enter button
enterBuyMeButton = driverChrome.find_element_by_class_name("ui-btn")
enterBuyMeButton.click()
# wait to sec
time.sleep(2)

#open drop list of pickAmount
pickSum = driverChrome.find_element_by_xpath("//*[@id='ember664_chosen']/a")
pickSum.click()

#select amount of 99-199 NIS
SelectAmount = driverChrome.find_element_by_xpath("//*[@id='ember664_chosen']/div/ul/li[3]")
SelectAmount.click()


#open drop list of Area
pickArea = driverChrome.find_element_by_xpath("//*[@id='ember679_chosen']/a")
pickArea.click()

#select south Area
selectArea = driverChrome.find_element_by_xpath("//*[@id='ember679_chosen']/div/ul/li[5]")
selectArea.click()

#open drop list of Category
pickCategory = driverChrome.find_element_by_xpath("//*[@id='ember688_chosen']/a")
pickCategory.click()

#select category
selectCategory = driverChrome.find_element_by_xpath("//*[@id='ember688_chosen']/div/ul/li[5]")
selectCategory.click()

#Press search button
presssearchButton = driverChrome.find_element_by_id("ember723")
presssearchButton.click()

#select busines
pickBusiness = driverChrome.find_element_by_xpath("//*[@id='ember1165']/div")
pickBusiness.click()

#selectGiftAmount
selectGiftAmount = driverChrome.find_element_by_id("ember1215")
selectGiftAmount.send_keys("154")
time.sleep(2)
#Press choose Button
pressChoose = driverChrome.find_element_by_xpath("//*[@id='ember1214']/div[2]/div/button")
pressChoose.click()

#select to else
giftTo = driverChrome.find_element_by_xpath("//*[@id='ember1280']/label[1]")
giftTo.click()
time.sleep(2)
#Gift to
driverChrome.find_element_by_id("ember1308").clear()
EnterGiftreceiver = driverChrome.find_element_by_id("ember1308").send_keys("James")
driverChrome.find_element_by_id("ember1310").clear()
EnterSenderreceiver = driverChrome.find_element_by_id("ember1310").send_keys("Superman")
clearText = driverChrome.find_element_by_xpath("//*[@id='ember1327']/textarea").clear()
time.sleep(2)
EnterSender = driverChrome.find_element_by_xpath("//*[@id='ember1327']/textarea").send_keys("מזל טוב חבוב...עד 120")
Enterreceiver = driverChrome.find_element_by_xpath("//*[@id='ember1336']").send_keys("C:\DevOps\First Project\yomholedet.jpg")
time.sleep(2)
#select event
openEvents = driverChrome.find_element_by_xpath("//*[@id='ember1312_chosen']/a").click()
selectEvent = driverChrome.find_element_by_xpath("//*[@id='ember1312_chosen']/div/ul/li[5]").click()

#pay time
payTime = driverChrome.find_element_by_class_name("send-now").click()

#selectSMSMethod
selectSMS = driverChrome.find_element_by_xpath("//*[@id='ember1273']/div[4]/div/div[1]/div[1]/div/button").click()
senderPhone = driverChrome.find_element_by_xpath("//*[@id='resendReciver']").send_keys("0501234567")
driverChrome.find_element_by_xpath("//*[@id='resendReciver']").clear()
receiverPhone = driverChrome.find_element_by_xpath("//*[@id='resendReciver']").send_keys("0507654321")
time.sleep(2)
pressSavePhone = driverChrome.find_element_by_xpath("//*//*[@id='ember1273']/div[5]/button").click()
time.sleep(2)
#press payment
paymentSave = driverChrome.find_element_by_xpath("//*[@id='ember1817']/div[5]/button").click()

time.sleep(3)
driverChrome.close()

