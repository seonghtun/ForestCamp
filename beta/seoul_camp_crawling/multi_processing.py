from selenium import webdriver
from selenium.webdriver.common.by import By
from multiprocessing import Process, Queue

import time
import math
from bs4 import BeautifulSoup

math.factorial(100000)

def is_queue_func(html):
    soup = BeautifulSoup(html, 'html.parser')
    is_queue = soup.find('progress', attrs={'id': 'progressbar'})
    if is_queue != None:
        print("대기열 떴습니다.")
        time.sleep(15)
    else:
        print("대기열 아닙니다.")
        time.sleep(0.3)
    return

def count_page(url, chrome_options) -> int:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url=url)
    is_queue_func(driver.page_source)

    driver.find_element(By.CLASS_NAME, "next_last").click()
    is_queue_func(driver.page_source)

    last_page_num = driver.find_elements(By.CSS_SELECTOR, "div.paging > ul > li")[-1].text
    print(last_page_num)
    driver.close()
    return int(last_page_num)

def page_crawling(url, page_num, chrome_options, datas):
    print(f"{page_num} page crawling start!")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url=url)
    is_queue_func(driver.page_source)
     
    if page_num != 1:
        if (page_num - 1) / 5 >= 1.0 :
            for _ in range((page_num - 1) // 5):
                driver.find_element(By.CLASS_NAME, 'next').click()
                is_queue_func(driver.page_source)
                 

    pages = driver.find_elements(By.CSS_SELECTOR, "div.paging > ul > li" )
    pages[(page_num % 5) - 1].click()
    is_queue_func(driver.page_source)

    menus = driver.find_elements(By.CSS_SELECTOR,'.img_board > li > a')

    for i in range(len(menus)):
        menus = driver.find_elements(By.CSS_SELECTOR,'.img_board > li > a')
        menus[i].click()
        is_queue_func(driver.page_source)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find("table", attrs={"class": "tbl_cal"})
        # print(table)
        # print(table.find_all("a", attrs={"title":"예약불가"}))
        ables = table.find_all("a", attrs={"title":"예약가능"})
        
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

        driver.back()
        is_queue_func(driver.page_source)
    
    driver.close()
    print(f"{page_num} page 예약 가능 개수 : {datas.qsize()}개 !")
    print(f"{page_num} page crawling end!")
    return 


def selenium_multi_processing(num,url, chrome_options):
    datas = Queue()
    procs = []
    for i in range(1, num+1):
        p = Process(target=page_crawling, args = (url, i, chrome_options, datas))
        procs.append(p)
        p.start()
    
    for proc in procs:
        proc.join()

    datas.put('STOP')
    print("-"*50)
    print("all crawling end!")
    print("Queue size",datas.qsize())
    return datas

def set_interval(func,sec,url,chrome_options):
    datas = func(url,chrome_options)
    # insert_data(datas)
    
    t = Timer(sec, set_interval, args=(func,sec,url,chrome_options))
    t.start()
    
    print(count)
    return t


# def set_interval(func, sec, url, chrome_options, bs4_parser):
#     def func_wrapper():
#         cnt = func(url, chrome_options, bs4_parser)
#         print(cnt)
#         set_interval(func, sec, url, chrome_options, bs4_parser)
#     t = Timer(sec, func_wrapper)
#     t.start()
#     return t
    
# insert_data(items=crawling_func(myurl, chrome_options, myparser))


if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-browser-side-navigation")
    
    myparser = 'html.parser'
    base_url = 'https://yeyak.seoul.go.kr'
    myurl = 'https://yeyak.seoul.go.kr/web/search/selectPageListDetailSearchImg.do?code=T500&dCode=T502'
    
    start = time.time()

    # cnt = count_page(myurl,chrome_options)
    # datas = selenium_multi_processing(int(cnt),myurl, chrome_options)
    datas = Queue()
    procs = []
    
    for i in range(1, 3):
        p = Process(target=page_crawling, args = (myurl, i, chrome_options, datas))
        procs.append(p)
        p.start()
    
    for proc in procs:
        proc.join()
    
    datas.put('STOP')
    print("-"*50)
    print("all crawling end!")
    print("Queue size",datas.qsize())


    end = time.time()
    print(f"{end - start:.5f} sec")