import time
from bs4 import BeautifulSoup
import math
from urllib.request import urlopen

url = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S230703101244535490&code=T500&dCode=T502&sch_order=1&sch_choose_list=&sch_type=&sch_text=&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='
myparser = 'html.parser'

response = urlopen(url)
soup = BeautifulSoup(response, myparser)

# print(soup)
# print(soup.find("div", attrs={"class":'cal_box noselect'}))
print(soup.find("ul", attrs={"class" : "dt_top_list"}))