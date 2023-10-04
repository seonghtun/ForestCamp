import boto3

def update_item(dbname:str='dynamodb', region:str='ap-northeast-2', table_name:str='seoul_camp',
                key:dict={"place": "강남",'site':'20'}):
    
    dynamodb = boto3.resource(dbname, region_name=region)
    table = dynamodb.Table(table_name)
    
    # The UpdateItem API allows you to update a particular item as identified by its key.
    resp = table.update_item(
        Key=key,
        # Expression attribute names specify placeholders for attribute names to use in your update expressions.
        ExpressionAttributeNames={
            "#formats": "Formats",
            "#audiobook": "Audiobook",
        },
        # Expression attribute values specify placeholders for attribute values to use in your update expressions.
        ExpressionAttributeValues={
            ":id": "8WE3KPTP",
        },
        # UpdateExpression declares the updates you want to perform on your item.
        # For more details about update expressions, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.UpdateExpressions.html
        UpdateExpression="SET #formats.#audiobook = :id",
    )
    
if __name__ == "__main__":
    update_item()
