from fastapi import FastAPI, APIRouter
import pymongo
from pathlib import Path
from typing import Optional
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn.objects as so
import boto3
import matplotlib.pyplot as plt
from fastapi.responses import StreamingResponse
import io
import datetime
import re
from datetime import datetime, timedelta
import datetime
# pydantic.json.ENCODERS_BY_TßYPE[ObjectId] = str
app = FastAPI()
router = APIRouter()
s3 = boto3.client('s3')

myclient = pymongo.MongoClient("mongodb://15.164.18.245:27017/")
mydb = myclient["admin"]
mycol = mydb["forestcamps"]
# db.컬렉션.createIndex({필드 : 인덱스 이름})
# mycol.create_index({'titleName' : "text" , 'account' : "text"})
# mycol.create_index([('name', 'text')])

from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/Campingstore/imgPrint')
async def imgPrint(id):
    titleimg = mycol.find({"id" : id}, {'_id': 0}).sort('_id',-1).limit(1)
    _ = list(titleimg)[0]
    if len(_["price"]) == 0:
        _["price"] = "품절 입니다."
    else:
        _["price"] =  _["price"][0]
    # print(titleimg[0])
    # return titleimg
    # return {"ok" : 200, "Information" : { "id" : list(titleimg)[0]['id'], "title" : list(titleimg)[0]['titleName'], "titleImg" : list(titleimg)[0]['titleImg'], "price" : list(titleimg)[0]['price'] }}
    return  {"ok" : 200, "id" : _['id'], "titleImg" : _['titleImg']}
    # return {"ok" : 200, "id" : titleimg["id"] ,"titleImg" : titleimg["titleImg"], 'time': titleimg["time"]}

@app.get('/Campingstore/information')
async def imgPrint(id: str):
    informations = mycol.find({'id' : id}, {'_id': 0 ,'iconName': 1, 'iconImg' : 1 , 'price' : 1, 'deliveryPrc' : 1, 'sellpage' : 1, 'time': 1})
    information = list(informations)[-1]
    iconName_dic = []
    iconImg_dic = []
    price_dic = []
    deliveryPrc_dic = []
    sellPage_dic = []
    iconName_dic.append(information["iconName"])
    iconImg_dic.append(information["iconImg"])
    price_dic.append(information["price"])
    deliveryPrc_dic.append(information["deliveryPrc"])
    sellPage_dic.append(information["sellpage"])
    print(information["time"])
    return {"ok" : 200, "Information" : {"iconName": iconName_dic, "iconImg": iconImg_dic, "price": price_dic, "deliveryPcr": deliveryPrc_dic, "sellpage": sellPage_dic,} }

@app.get('/Campingstore/explanation')
async def imgPrint(id: str):
    
    account = mycol.find_one({'id' : id}, {'_id': 0, 'titleName' : 1,'account': 1})
    
    return {"ok" : 200, "Information" : { "account" : account["account"], "title" : account["titleName"] }}


# @app.get('/Campingstore/trends')
# async def imgPrint(id: str):
#     informations = mycol.find_one({'id' : id}, {'_id': 0 , 'price' : 1, 'time' : 1 })
#     price_list = []
#     for information in informations["price"]:
#         info = information.replace(',','').replace('원', '')
#         print(info)
#         price_list.append(int(info))

    sns.set_theme(style='darkgrid')
    snsimg = sns.lineplot(data=price_list, color='gray')
    
    figure = snsimg.get_figure()
    
    figure.gca().axes.xaxis.set_visible(False)
    img_stream = io.BytesIO()
    figure.savefig(img_stream, format="png")
    img_stream.seek(0)
    plt.clf()
    
# .set(ylim=(0, max(price_list) + 100000))
    # plt.savefig('filename.png', dpi = 300)
    return StreamingResponse(img_stream, media_type="image/png")
    

@app.get('/Campingstore/card')
async def imgPrint(id: str):
    # titleimg = mycol.find({"id" : id}, {'_id': 0, 'id': 1 ,'titleName' : 1,'titleImg': 1, 'price' : 1}).sort({'_id':-1}).limit(1)
    # titleimg = mycol.find({"id" : id}, {'_id': 0, 'id': 1 ,'titleName' : 1,'titleImg': 1, 'price' : 1, 'time' : 1}).sort({'_id':-1}).limit(1)
    titleimg = mycol.find({"id" : id}, {'_id': 0}).sort('_id',-1).limit(1)
    _ = list(titleimg)[0]
    if len(_["price"]) == 0:
        _["price"] = "품절 입니다."
    else:
        _["price"] =  _["price"][0]
    # print(titleimg[0])
    # return titleimg
    # return {"ok" : 200, "Information" : { "id" : list(titleimg)[0]['id'], "title" : list(titleimg)[0]['titleName'], "titleImg" : list(titleimg)[0]['titleImg'], "price" : list(titleimg)[0]['price'] }}
    return  {"ok" : 200, "Information" : {"id" : _['id'], "title" : _['titleName'], "titleImg" : _['titleImg'], "price" : _['price']}}
    # return {"ok":200}


@app.get('/Campingstore/fluctuation')
async def imgPrint(id: str):
    informations = mycol.find({'id' : id}, {'_id':  0, 'time' : 1,'id' : 1,'price' : 1, })

    prc_list = []
    for information in list(informations):
        print(information['time'])
        print(information['price'])
        
        
  
        prc_list.append(information['price'][0])

    recentPrc = prc_list[-1]
    evePrc = prc_list[-2]
    fluctuation = (int(recentPrc.replace(',','').replace('원', '')) - int(evePrc.replace(',','').replace('원', ''))) / int(evePrc.replace(',','').replace('원', '')) * 100
    
        

    return  {"ok" : 200, "Information" : { "recentPrc" : '0', "fluctuation" : '0'}}

# @app.get('/Campingstore/trend2')
# async def imgPrint(id: str):
#     informations = mycol.find({'id' : id}, {'_id':  0, 'time' : 1,'price' : 1, })

#     prc_list = []
#     time_lsit = []
#     for information in list(informations):
#         prc_list.append(information['price'][0].replace(',','').replace('원', ''))
#         recent_prc = list(reversed(prc_list))[0:7]
#         time_lsit.append(information['time'])
        
    
#     recent_time = list(reversed(time_lsit))[0:7]
#     line=[]
#     for i in range(1, len(recent_prc)+1):
#         line.append({"recentPrc": int(recent_prc[-i]), "recentTime":recent_time[-i]})
        
#         return {"ok" : 200, "Information" : line}

@app.get('/Campingstore/trend2')
async def imgPrint(id: str):
    informations = mycol.find({'id' : id}, {'_id':  0, 'time' : 1,'price' : 1, })
    time = []
    price = []
    for to in list(informations):
        time.append(to["time"])
        pcr = to["price"]
        pr = []
        for i in pcr:
            pr.append(int(i.replace(',','').replace('원', '')))
        
        if len(pr) == 0:
             price.append(int(0))
        else:
            price.append(min(pr))
    print(len(time))
            
    cnt = 0  
    set_cnt = 0
    price_list_sample = []
    return_list = [] 
    set_time = ""
    for _ in range(0, len(time)):
        times = time[cnt].split("-") 
        day = datetime.date(int(times[0]), int(times[1]), int(times[2]))
        weekdat = day.weekday()
        
        if set_time == time[cnt]:
            pass
        
        elif set_cnt > weekdat and weekdat != 0:
            set_cnt = weekdat 
            return_list.append({"recentPrc":min(price_list_sample) , "recentTime":time[cnt]})
            price_list_sample = []
            price_list_sample.append(price[cnt])
        
        elif weekdat == 0:
            price_list_sample.append(price[cnt])
            return_list.append({"recentPrc":min(price_list_sample) , "recentTime":time[cnt]})
            price_list_sample = []
            set_cnt = 0
        
        elif cnt == 0:
            set_cnt = weekdat
            price_list_sample.append(price[cnt])
            
        else:
            set_cnt = weekdat
            price_list_sample.append(price[cnt])
        cnt += 1
        set_time = time[_]
                     
    return {"ok" : 200, "Information" : return_list}

@app.get('/Campingstore/serchcard')
async def imgPrint(a: str):
    titleimg = mycol.find( {'account':{'$regex':f'{a}'}}).limit(10)
    # .findOne().sort({ dateCreated: 1 })
    print(list(titleimg))
    return {"ok" : 200}

@app.get('/Campingstore/search')
async def imgPrint(id: str):
    day = datetime.datetime.now().strftime('%Y-%m-%d')
    day2 = datetime.datetime.now() - datetime.timedelta(days=1)
    # titleimg = mycol.find({'$and':[{'$or':[{'account':{'$regex': a}},{'account':{'$regex': a}}]}, {'time':day}] }).limit(1)
    # titleimg = mycol.find({'$or':[{'account':{'$regex': a}},{'titleName':{'$regex': a}}] }).limit(1)
    titleimg = mycol.find({'account':{'$regex': id}, 'titleName':{'$regex': id}, 'time': day}, {'_id': 0, 'id': 1 ,'titleName' : 1,'titleImg': 1, 'price' : 1, 'time' : 1})

    _ = list(titleimg)
    id = []
    data = {}
    for i in range(0, len(_)):
        v = _[i]
        print(v)
        if len(v["price"]) == 0:
            data["price"] = "품절 입니다."
        else:
            data["price"] =  v["price"][0]
        data["id"] =  v["id"]
        data["title"] = v["titleName"]
        data["titleImg"] =  v["titleImg"]
        data["time"] =  v["time"]
        id.append(data)
        data = {}
    print(id)
    print(len(id))
    return {"data" : id}

@app.get('/Campingstore/category')
async def imgPrint(a: str):
    print(a)
    # if a.isdigit() == False or len(a) > 3:
    #     return "오류입니다."
    b =[]
    if "," in a:
        b = a.split(",")
    elif a == "":
        print(1)
        b.append("101")
    else:
        b.append(a)   
        
    day3 = datetime.datetime.now().strftime('%Y-%m-%d')
    day2 = datetime.datetime.now() - datetime.timedelta(days=2)
    day = day2.strftime('%Y-%m-%d')
    print(day)
    cnt = 0
    test_list = []   
    cnt1 = 0 
    for _ in b:
        while True:
            print(cnt1)
            try:
                text = int(_ +"0001") + cnt
                text = str(text)
                sortation = mycol.find({'time' : day, 'id': text}, {'_id':0, 'smallcategory': 1}).limit(1)
                test = list(sortation)[0]["smallcategory"]
                test_list.append(test)
                if len(test) > 0:
                    print(len(test))
                    break
            except:
                cnt += 1
                pass
        
            cnt1 += 1
            if cnt1 == 10:
                return "오류 입니다."
    id = []
    data = {}
    for v in test_list:
        sortation = mycol.find({ 'time': day, 'smallcategory': v}, {'_id': 0, 'id': 1 ,'titleName' : 1,'titleImg': 1, 'price' : 1, 'time' : 1})
        _ = list(sortation)
        for i in range(0, len(_)):
            v = _[i]
            if len(v["price"]) == 0:
                data["price"] = "품절 입니다."
            else:
                data["price"] =  v["price"][0]
            data["id"] =  v["id"]
            data["title"] = v["titleName"]
            data["titleImg"] =  v["titleImg"]
            data["time"] =  v["time"]
            id.append(data)
            data = {}
    return {"data" : id}
        
    # print(len(list(titleimg)))
    # return  {"ok" : 200, "Information" : {"id" : _['id'], "title" : _['titleName'], "titleImg" : _['titleImg'], "price" : _['price'][0]}}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
    print("server 3000 PORT OPEN")
    

    

# @app.get('/Campingstore/')
# @app.get("/get_image/{image_key}")
# async def get_image(image_key: str):
#     try:
#         response = s3.get_object(Bucket='lee-0286', Key=image_key)
#         image_data = response['Body'].read()
#         return image_data
#     except Exception as e:
#         return {"error": str(e)}


    # if cnt == 0:
    #     print("여기로 들갔습니다.")
    #     titleimg = mycol.find({'$and':[{'$or':[{'account':{'$regex': a}},{'account':{'$regex': a}}] }, {'time':day2.strftime('%Y-%m-%d')}]}, {})
    # print(len(list(titleimg)[0]))
    # print(len(list(titleimg)))
    # print(len(list(titleimg)))
    # # cnt = len(list(titleimg))