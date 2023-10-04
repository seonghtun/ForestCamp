from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from bs4 import BeautifulSoup


from threading import Timer
from threading import Thread

math.factorial(100000)

class data_class:
    def __init__(self):
        self.datas = list()
    
    def put(self,data):
        self.datas.append(data)
    
    def get(self):
        return self.datas

def is_success(browser:object,action:str,web_object:object=None,URL:str=None): #index:int, ,seletor:str 
    '''
        action type:
        0 get
        1 click
        2 back
    '''
    flag=True
    crawling_success = False
    for i in range(5):
        print(f'==try count: [{i+1}]')
        try:
            if action == '0':
                browser.get(url=URL)
                
            elif action == '1':
                if flag: 
                    web_object.click()
                else:
                    browser.refresh()
            else:
                if flag:
                    browser.back()
                else:
                    browser.refresh()
            crawling_success = True
        except TimeoutException as ex:
            print(f'==try count: [{i+1}] => exception:\n{ex}')
            flag=False
        if crawling_success:
            break
    if crawling_success == False:
        print("retry gogo!")

def is_queue_func(driver:object):
    html = driver.page_source
    try:
        result = driver.switch_to.alert
        print("alert :",result.text)
        result.accept()
    except Exception as e:
        pass
    soup = BeautifulSoup(html, 'html.parser')
    is_queue = soup.find('progress', attrs={'id': 'progressbar'})
    if is_queue != None:
        print("대기열 떴습니다.")
        time.sleep(15)
    else:
        driver.implicitly_wait(10)

def count_page(url, chrome_options) -> int:
    print("count_page start~")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(5)
    
    is_success(driver,'0',URL=url)
    is_queue_func(driver)

    is_success(driver,'1',web_object=driver.find_element(By.CLASS_NAME, "next_last"))
    is_queue_func(driver)

    last_page_num = driver.find_elements(By.CSS_SELECTOR, "div.paging > ul > li")[-1].text
    print("last_page :",last_page_num)
    driver.close()
    print("count_page end~")
    return int(last_page_num)

def page_crawling(url, page_num, chrome_options, datas):
    counts = 0
    print(f"{page_num} page crawling start!")
    driver = webdriver.Chrome(options=chrome_options)
    is_success(driver,'0',URL=url)
    is_queue_func(driver)
     
    if page_num != 1:
        if (page_num - 1) / 5 >= 1.0 :
            for _ in range((page_num - 1) // 5):
                is_success(driver,'1',web_object=driver.find_element(By.CLASS_NAME, 'next'))
                is_queue_func(driver)
                 

    pages = driver.find_elements(By.CSS_SELECTOR, "div.paging > ul > li" )
    is_success(driver,'1',web_object=pages[(page_num % 5) - 1])
    is_queue_func(driver)

    menus = driver.find_elements(By.CSS_SELECTOR,'.img_board > li > a')

    for i in range(len(menus)):
        menus = driver.find_elements(By.CSS_SELECTOR,'.img_board > li > a')
        is_success(driver,'1',web_object=menus[i])
        is_queue_func(driver)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find("table", attrs={"class": "tbl_cal"})
        # print(table.find_all("a", attrs={"title":"예약불가"}))
        ables = table.find_all("a", attrs={"title":"예약가능"})
        
        print("able 개수:",len(ables),"page_num",page_num)
        counts += len(ables)
        for a in ables:
            remain, total = a.find('span', attrs={'class':'num'}).text.split('/')
            data = {
                "place": soup.find('span', attrs={'class':"tit"}).text,
                "date":a['data-ymd'],
                "remain_site":remain,
                "total_site": total,
                "img_url": base_url + soup.select_one(" div.left_box > div.img_box > img")['src']
            }
            datas.put(data)
            # datas.put(data)
        print("func : datas 개수", len(datas.get()))
        # print("Queue size :", datas.qsize())

        is_success(driver,'2')
        is_queue_func(driver)

    driver.close()
    print("counts:",counts,"page_num",page_num)
    return 

def selenium_multi_thread(num,url, chrome_options):
    datas = data_class()
    threads = []
    for i in range(1, num+1):
        t = Thread(target=page_crawling, args = (url, i, chrome_options,datas))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

    print("data size",len(datas.get()))
    return datas

def set_interval(func,sec,url,chrome_options):
    count,datas = func(url,chrome_options)
    insert_data(datas)
    
    t = Timer(sec, set_interval, args=(func,sec,url,chrome_options))
    t.start()
    
    print(count)
    return t

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-browser-side-navigation")
    chrome_options.add_argument("--start-maximized")

    base_url = 'https://yeyak.seoul.go.kr'
    myurl = 'https://yeyak.seoul.go.kr/web/search/selectPageListDetailSearchImg.do?code=T500&dCode=T502'
    
    start = time.time()

    cnt = count_page(myurl,chrome_options)
    result = selenium_multi_thread(int(cnt),myurl, chrome_options)

    end = time.time()
    print(f"{end - start:.5f} sec")

