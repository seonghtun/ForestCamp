import time
from selenium import webdriver

# Chrome WebDriver를 이용해 Chrome을 실행합니다.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-browser-side-navigation")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options = chrome_options)
driver.execute_script("alert('자바스크립트 코드 적용!!');")

# pop.html 파일을 실행합니다.
time.sleep(1)

# 첫 번째 alert 버튼을 클릭합니다.
# inputElement = driver.find_element_by_id('simpleAlert')
# inputElement.click()
# time.sleep(2)

# alert 창의 '확인'을 클릭합니다.
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)

# 다시 첫 번째 alert 버튼을 클릭합니다.
# inputElement = driver.find_element_by_id('simpleAlert')
# inputElement.click()
# time.sleep(2)

# # alert 창의 메시지를 확인하고 싶습니다.
# alert = driver.switch_to.alert
# message = alert.text
# print("Alert shows following message: "+ message )
# time.sleep(2)

# # 메시지를 확인했으니 창을 닫습니다.
# alert = driver.switch_to.alert
# alert.accept()
# time.sleep(2)



# # 두 번째 alert 버튼을 클릭합니다.
# inputElement = driver.find_element_by_id('confirmAlert')
# inputElement.click()
# time.sleep(2)

# # alert 창의 '취소'을 클릭합니다.
# alert = driver.switch_to.alert
# alert.dismiss()
# time.sleep(2)

# # 다시 두 번째 alert 버튼을 클릭합니다.
# inputElement = driver.find_element_by_id('confirmAlert')
# inputElement.click()
# time.sleep(2)

# # alert 창의 '확인'을 클릭합니다.
# alert = driver.switch_to.alert
# alert.accept()
# time.sleep(2)



# # 세 번째 alert 버튼을 클릭합니다.
# inputElement = driver.find_element_by_id('promptAlert')
# inputElement.click()
# time.sleep(2)

# # alert 창의 '취소'을 클릭합니다.
# alert = driver.switch_to.alert
# alert.dismiss()
# time.sleep(2)

# # 다시 세 번째 alert 버튼을 클릭합니다.
# inputElement = driver.find_element_by_id('promptAlert')
# inputElement.click()
# time.sleep(2)

# # prompt창에 이름을 씁니다.
# alert = driver.switch_to.alert
# alert.send_keys('tongchun')
# time.sleep(2)

# # alert 창의 '확인'을 클릭합니다.
# alert = driver.switch_to.alert
# alert.accept()
# time.sleep(2)


# # 실행한 브라우저를 닫습니다.
time.sleep(5)
driver.quit()