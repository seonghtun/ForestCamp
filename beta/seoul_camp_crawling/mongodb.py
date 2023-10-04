# BASE_DIR = os.path.dirname(os.path.relpath("./"))
# secret_file = os.path.join(BASE_DIR, 'secret.json')

# with open(secret_file) as f:
#     secrets= json.loads(f.read())

# def get_secret(setting, secrets=secrets):
#     try:
#         return secrets[setting]
#     except KeyError:
#         errorMsg = "Set the {} environment variable.".format(setting)
#         return errorMsg

# HOST = get_secret('Mongo_Host')
# USERNAME = get_secret('Mongo_User')
# PASSWORD = get_secret('Mongo_Pass')

# client = mongo_client.MongoClient(f'mongodb+srv://{USERNAME}:{PASSWORD}@{HOST}')

# client.close()
def mongo_insert_one(collection:object, row:dict) -> None:
    collection.insert_one(row)
    result = collection.find_one({"name":row['name']})
    return result

def mongo_insert_many(collection:object, rows:list[dict]):
    collection.insert_many(rows)
    print("insert rows")
    return

def mongo_query(collection:object, search:str):
    return collection.find({"name":{"$regex":search,"$options":"i"}}, {"_id":0})

def mongo_find_one(collection:object, name:str):
    return collection.find_one({"name":name},{"_id":0})

def mongo_delete(collection):
    d = collection.delete_many({})
    print(d.deleted_count," documents deleted !!")
    return d.deleted_count

if __name__ == "__main__" :
    from pymongo import mongo_client
    from bson.objectid import ObjectId
    import json
    import os

    # insert_many(mycol, users)
    # print(next(find(mycol)))

    client = mongo_client.MongoClient(f'mongodb://localhost:27017/')
    print('Conneted to Mongodb....')

    mydb = client['test']
    mycol = mydb['campingjang']
    user = dict(id="ab", name="bc")
    users = [dict(id="ab", name="bc"),dict(id="ab", name="bc")]
    print(mongo_delete(mycol))

# @app.get('/userupdate')
# async def userupdate(id=None, name=None):
#     if (id and name) is None:
#         return "id와 name을 입력하세요."
#     else:
#         result = mycol.find_one({"id":id})
#         if result is None:
#             return '데이터가 존재하지 않습니다'
        
#         new_values = {"$set" : {"name": name}}
#         reuslt = mycol.update_one({"id":id} , new_values)
#         print(result)
#         return result
