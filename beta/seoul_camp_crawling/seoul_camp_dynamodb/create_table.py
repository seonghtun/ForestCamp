import boto3

# boto3 is the AWS SDK library for Python.
# We can use the low-level client to make API calls to DynamoDB.

def create_table(
            key_schema:list[dict],
            AttributeDefinitions:list[dict],  
            ProvisionedThroughput:dict,
            dbname : str = 'dynamodb', region : str = "ap-northeast-2",
            table_name:str = "seoul_camp"):

    client = boto3.client(dbname, region_name=region)

    try:
        resp = client.create_table(
            TableName=table_name,
            # Declare your Primary Key in the KeySchema argument
            KeySchema=key_schema,
            # Any attributes used in KeySchema or Indexes must be declared in AttributeDefinitions
            AttributeDefinitions=AttributeDefinitions,
            # ProvisionedThroughput controls the amount of data you can read or write to DynamoDB per second.
            # You can control read and write capacity independently.
            ProvisionedThroughput=ProvisionedThroughput
        )
        print("Table created successfully!")
    except Exception as e:
        print("Error creating table:")
        print(e)

if __name__ == '__main__':
    
    key_schema = [
            {
                "AttributeName": "place",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "date",
                "KeyType": "RANGE"
            }
        ]
        
    AttributeDefinitions = [
                {
                    "AttributeName": "place",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "date",
                    "AttributeType": "S"
                }
            ]
            
    ProvisionedThroughput = {
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            }
            
    create_table(key_schema = key_schema,
                AttributeDefinitions=AttributeDefinitions,
                ProvisionedThroughput=ProvisionedThroughput)