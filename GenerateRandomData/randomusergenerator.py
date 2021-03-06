import requests
import json
import boto3
import uuid
import time
import random

def GenerateRandomUserData():      
    url = 'https://randomuser.me/api/'
    response = requests.get(url)
    json_data = json.loads(response.text)    
    
    return json_data
    

def WriteToS3(array):    
    s3 = boto3.resource('s3')
    body = str(json.dumps(array).encode('UTF-8'))
    s3.Bucket('nathanrhoda-machinelearning').put_object(Key='userdata.json', Body=body)

def StreamToKinesis():
    client = boto3.client('kinesis', 'us-east-1')
    partitin_key = str(uuid.uuid4())

    while True:
        try:
            data = GenerateRandomUserData()        
            client.put_record(
                StreamName='nr-stream',
                Data=json.dumps(data),
                PartitionKey=partitin_key
            )
        except Exception as e:
            print(e)

        #time.sleep(random.uniform(0,1))

if __name__ == "__main__":            
    StreamToKinesis()    
    print('Done')
