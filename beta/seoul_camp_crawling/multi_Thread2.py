# def get_campingjang_urls(url, chrome_options):
#     urls = []
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.set_page_load_timeout(10)
#     is_success(driver,'1',URL=url)
#     driver.implicitly_wait(10)
#     # is_alert()
#     is_queue_func(driver)
    
#     page_num = 0
#     while True:
#         pages = driver.find_elements(By.CSS_SELECTOR, "div.paging > ul > li" )
        
#         print("crawling start!")
#         for i in range(len(pages)):
#             page_num +=1
#             print(f"{page_num} page -> crawling start!!")
#             pages = driver.find_elements(By.CSS_SELECTOR, "div.paging > ul > li" )
#             pages[i].click()
#             driver.implicitly_wait(10)
#             # is_alert()

#             print(f"{page_num} page -> click")
#             is_queue_func(driver)

#             menus = driver.find_elements(By.CSS_SELECTOR,'.img_board > li > a')
#             for i in range(len(menus)):
#                 menus = driver.find_elements(By.CSS_SELECTOR,'.img_board > li > a')
#                 menus[i].click()
#                 driver.implicitly_wait(10)
#                 # is_alert()
#                 is_queue_func(driver)
                
#                 urls.append(driver.current_url)
#                 print("urls 개수 :",len(urls))
#                 driver.back()
                 
#                 driver.implicitly_wait(10)
#                 # is_alert()
#                 is_queue_func(driver)
#             print(f"{page_num} page -> crawling end!!")

#         soup = BeautifulSoup(driver.page_source, 'html.parser')
#         next_btn = soup.find('a', attrs={'class': 'next'})
        
#         if next_btn == None:
#             print("last url :",driver.current_url)
#             break
#         else:
#             driver.find_element(By.CLASS_NAME, 'next').click()
#             driver.implicitly_wait(10)
#             # is_alert()
#             print("next click")
#             is_queue_func(driver)

#     driver.close()
#     print(len(urls))
#     print(urls)
#     return urls

# def campingjang_crawling(url, chrome_options, bs4_parser,datas):
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(url=url)
    
#     is_queue_func(driver.page_source)
#     soup = BeautifulSoup(driver.page_source, bs4_parser)
#     table = soup.find("table", attrs={"class": "tbl_cal"})
#     ables = table.find_all("a", attrs={"title":"예약가능"})
#     for a in ables:
#         remain, total = a.find('span', attrs={'class':'num'}).text.split('/')
#         data = {
#             "place": soup.find('span', attrs={'class':"tit"}).text,
#             "date":a['data-ymd'],
#             "remain_site":remain,
#             "total_site": total,
#             "img_url": base_url + soup.select_one(" div.left_box > div.img_box > img")['src']
#         }
#         datas.put(data)

#     print("func : datas 개수", len(datas.get()))
    
#     driver.close()
#     return 