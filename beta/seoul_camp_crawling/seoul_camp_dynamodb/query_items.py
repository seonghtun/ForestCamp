import boto3
from boto3.dynamodb.conditions import Key

def query_items(dbname:str='dynamodb',table_name:str='seoul_camp',
                region:str='ap-northeast-2',key:str='place',value:str='25'):
# boto3 is the AWS SDK library for Python.
    dynamodb = boto3.resource(dbname, region_name=region)
    table = dynamodb.Table(table_name)
    
    # When making a Query API call, we use the KeyConditionExpression parameter to specify the hash key on which we want to query.
    # We're using the Key object from the Boto3 library to specify that we want the attribute name ("Author")
    # to equal "John Grisham" by using the ".eq()" method.
    # resp = table.query(KeyConditionExpression=Key(key).eq(value))
    # resp = table.query(KeyConditionExpression=Key(key))
    resp = table.scan()
    
    return resp['Items']

if __name__ == '__main__':
    print("The query returned the following items:")
    print(query_items())
    # for item in query_items():
        # print(item)