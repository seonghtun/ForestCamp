import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
# from apscheduler.schedulers.background import BlockingScheduler

import time
from bs4 import BeautifulSoup
import math
# import schedule

math.factorial(100000)

# def startTimer():
#     print(1234)
#     timer = Timer(5, startTimer)
#     timer.start()


    
# startTimer()

def hello(bs4_parser,chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url=url)

    campings = driver.find_elements(By.CSS_SELECTOR,'.img_board > li > a')
    for i in range(len(campings)):
        campings[i].click()
        time.sleep(0.5)
        soup = BeautifulSoup(driver.page_source, bs4_parser)
        table = soup.find("table", attrs={"class": "tbl_cal"})
        print(table)
        print(table.select('tbody tr td'))
        driver.back()
    
    driver.close()

url = 'https://yeyak.seoul.go.kr/web/search/selectPageListDetailSearchImg.do?code=T500&dCode=T502'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
myparser = 'html.parser'

@app.get()
def sidowjoe(df):
    for 
t = threading.Thread(target=hello, args=(myparser,chrome_options))
t.start
## apscheduler
# def main():
#     sched = BlockingScheduler()
#     sched.add_job(hello, 'interval', seconds=5, id='test', args=[myparser,chrome_options])
#     sched.start()

## 바보 아냐 ? 이걸 while 문으로 해도 중간에 값을 어떻게주냐 interrupt 그걸모르겠다고 으잉

## Threading Timer
# timer = Timer(15, hello, args=(myparser,))
# timer.start()
        
# menus = driver.find_elements(By.CSS_SELECTOR,'.img_board > li > a')

## schedule
# schedule.every(10).seconds.do(hello,myparser)

# while True:
#     schedule.run_pending()
#     time.sleep(1)



if __name__ == "__main__" :
    start = time.time()
    main()
    end = time.time()
    print(f"{end - start:.5f} sec")