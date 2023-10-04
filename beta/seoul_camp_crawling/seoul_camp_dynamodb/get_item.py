import boto3

def get_item(dbname:str='dynamodb', region:str='ap-northeast-2', table_name:str='seoul_camp',key:dict={"place": "강남",'site':'20'}):
    dynamodb = boto3.resource(dbname, region_name=region)
    table = dynamodb.Table(table_name)
    
    resp = table.get_item(Key=key)
    
    return resp['Item']

if __name__ == '__main__':
    print(get_item())
