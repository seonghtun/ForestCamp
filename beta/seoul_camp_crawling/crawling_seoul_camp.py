from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from threading import Timer
import redis
import time
import math
import json
from pymongo import mongo_client
from bson.objectid import ObjectId
from bs4 import BeautifulSoup
from mongodb import mongo_insert_one,mongo_query,mongo_delete

# import sys
# sys.path.append('/forestCamp/seoul_camp_crawling/seoul_camp_dynamodb')

# from insert_items import insert_data
#from pyvirtualdisplay import Display


#dispay = Display(visible=0, size = (1024,768))
#dispay.start()

math.factorial(100000)


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
                print("browser open")
            elif action == '1':
                if flag: 
                    web_object.click()
                    print("web object click")
                else:
                    browser.refresh()
            else:
                if flag:
                    browser.back()
                    print("browser back")
                else:
                    browser.refresh()
            crawling_success = True
        except TimeoutException as ex:
            print(f'==try count: [{i+1}] => exception:\nMessage: timeout')
            flag=False
        if crawling_success:
            break
    if crawling_success == False:
        print("retry gogo!")

def is_queue_func(driver:object):
    is_alert(driver)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    is_queue = soup.find('progress', attrs={'id': 'progressbar'})
    if is_queue != None:
        print("대기열 상태가 되었습니다.")
        time.sleep(15)
    else:
        time.sleep(0.3)

def is_alert(driver:object):
    try:
        result = driver.switch_to.alert
        print("alert :",result.text)
        result.dismiss()
        result.accept()
        driver.send_keys('\n')
    except NoAlertPresentException as e:
        pass
    except Exception as e :
        print(e)
        pass


def detail_search(driver:object) -> str:
    driver.execute_script("document.getElementById('sch_svc_sttus_R403').click();")
    driver.implicitly_wait(10)

    driver.execute_script("document.getElementById('dl_focus').click();")
    driver.implicitly_wait(10)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'text_red')))
    # print("WebDriveWait",element.text)
    # num = driver.find_element(By.CLASS_NAME,'text_red').text
    print(f"접수중인 서울 캠핑장 갯수 : {element.text}")
    # return num

def extract_data(driver:object) -> dict:
    base_url = 'https://yeyak.seoul.go.kr'

    is_alert(driver)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    info = soup.select("ul.dt_top_list > li")
    soup.select("#aform > div.dt_con_each > div.tab_con_box > div.tab_con.active > div:nth-child(3) > div > p:nth-child(2) > span:nth-child(2)")
    tents = ['텐트 지급', "텐트 제공"]
    is_tent = True
    for tent in tents:
            if tent in soup.find("span",attrs={"class":"tit"}).text:
                is_tent = False

    is_alert(driver)
    name = soup.select("#aform > div.dt_con_each > div.tab_con_box > div.tab_con.active > div:nth-child(3) > div > p:nth-child(2) > span:nth-child(2)")
    part_plan_src = soup.select("#aform > div.dt_con_each > div.tab_con_box > div.tab_con.active > div:nth-child(3) > div > div > img")
    print(part_plan_src)
    data = {
        # "name": info[1].contents[1],
        # "name": soup.select("#aform > div.dt_con_each > div.tab_con_box > div.tab_con.active > div:nth-child(3) > div > p:nth-child(2) > span:nth-child(2)"),
        "able_date":[],
        "reservation_state":[],
        "img_url": base_url + soup.select_one(" div.left_box > div.img_box > img")['src'],
        "information_use": str(soup.find("div",class_="tab_con active")),
        "use_term":info[2].contents[1].split("~"),
        "receipt_term": info[3].contents[2].split("~"),
        "phone": info[10].a.text,
        "tent": is_tent,
        "camp_url": driver.current_url
    }
    if name:
        print("찾음",name[0].text)
        data["name"] = name[0].text
    else:
        print("빈리스트",name)
        data["name"] = info[1].contents[1]
    
    if part_plan_src:
        data["part_plan"] = base_url + part_plan_src[0]['src']

    table = soup.find("table", class_="tbl_cal")
    if (table == None):
        table = soup.find("table", class_="tbl_cal")    
    ables = table.find_all("a", attrs={"title":"예약가능"})
    for a in ables:
        data['able_date'].append(a['data-ymd'])
        data['reservation_state'].append(a.find('span', attrs={'class':'num'}).text.split('/'))

    return data
    


def crawling_func(url, chrome_options):
    print("crawling start!")
    not_campings = ["바비큐존","파이어"]
    r = redis.Redis(host='localhost', port=5000, decode_responses=True)
    
    # client = mongo_client.MongoClient(f'mongodb://localhost:27017/')
    client = mongo_client.MongoClient(f'mongodb://localhost:29017/')
    print('Conneted to Mongodb....')
    mydb = client['test']
    mycol = mydb['campingjang']

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(5)

    is_success(driver,'0',URL=url)
    is_queue_func(driver)
    detail_search(driver)
    
    count = 1
    page_num = 0
    while True:
        pages = driver.find_elements(By.CSS_SELECTOR, "div.paging > ul > li" )

        for i in range(len(pages)):
            page_num+=1
            print(f"{page_num} page -> crawling start!!")
            pages = driver.find_elements(By.CSS_SELECTOR, "div.paging > ul > li" )
            is_success(driver,'1',web_object=pages[i])
            print(f"{page_num} page -> click")

            is_queue_func(driver)

            menus = driver.find_elements(By.CSS_SELECTOR,'.img_board > li > a')
            for i in range(len(menus)):
                menus = driver.find_elements(By.CSS_SELECTOR,'.img_board > li > a')
                is_bbq = False
                element_soup = BeautifulSoup(menus[i].get_attribute('innerHTML'),'html.parser')
                
                for not_camp in not_campings:
                    if not_camp in element_soup.h4.text:
                        print(f"여기는 캠핑장 site 예약이아닌 {not_camp} 예약입니다.")
                        is_bbq = True
                        break
                
                if is_bbq:
                    continue
                is_success(driver,'1',web_object=menus[i])
                is_queue_func(driver)
                data = extract_data(driver)
                data['row'] = count
                print(data['row'])
                row = json.dumps(data, ensure_ascii=False).encode('utf-8')
                r.set(count,row)
                print(f"insert to redis one data ")
                is_success(driver,'2')
                is_queue_func(driver)
                count += 1
            print(f"{page_num} page -> crawling end!!")
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        next_btn = soup.find('a', attrs={'class': 'next'})
        
        if next_btn == None:
            break
        else:
            is_success(driver,'1',web_object=driver.find_element(By.CLASS_NAME, 'next'))
            is_queue_func(driver)
    
    driver.close()
    keys = r.keys('*')
    mongo_delete(mycol)
    for key in keys:
        row = r.get(key)
        mongo_insert_one(mycol,dict(json.loads(row)))
    r.delete(*keys) 
    r.close()
    client.close()
    print("crawling end!")
    print("총 data count :",count)
    return 

def set_interval(func,sec,url,chrome_options):
    datas = func(url,chrome_options)
    # insert_data(datas)
    
    t = Timer(sec, set_interval, args=(func,sec,url,chrome_options))
    t.start()
    
    return t



if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-browser-side-navigation")
    chrome_options.add_argument("--start-maximized")
    
    myparser = 'html.parser'
    myurl = 'https://yeyak.seoul.go.kr/web/search/selectPageListDetailSearchImg.do?code=T500&dCode=T502'
    
    start = time.time() 

    #set_interval(crawling_func,5,myurl,chrome_options)
    crawling_func(myurl, chrome_options)
    

    end = time.time()
    print(f"{end - start:.5f} sec")

# 종료
