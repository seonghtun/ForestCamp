import boto3

def delete_table(dbname : str = 'dynamodb', region : str = "ap-northeast-2",table_name:str = "seoul_camp"):
    client = boto3.client(dbname, region_name=region)

    try:
        resp = client.delete_table(
            TableName=table_name,
        )
        print(f"{table_name} Table deleted successfully!")
        return resp
    except Exception as e:
        print("Error deleting table:")
        print(e)
    

if __name__ == "__main__":
    region = 'ap-northeast-2'
    table = 'seoul_camp'
    delete_table(region=region,table_name=table)