import boto3

# default 값으로 쓰려면 함수보다 위에 위치해야된다는구나.그렇구나 알겠구나 성형니구나
def insert_data(items: list[dict], dbname:str= 'dynamodb', region:str = 'ap-northeast-2', table_name : str = 'seoul_camp'):
    dynamodb = boto3.resource(dbname, region_name=region)
    table = dynamodb.Table(table_name)
    
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)
    # print(f"{items} inserted dynamodb")
        
if __name__ == "__main__":
    items =[{"place": "seocho", "site": "24",
            "Category": "camping"},
        {"place": "guro", "site": "22",
            "Category": "camping"},
        {"place": "seoul", "site": "21",
            "Category": "camping"},
        {"place": "seocho", "site": "20",
            "Category": "camping"}]
    insert_data(items=items)