import requests
import json
import boto3

def GenerateRandomUserData():      
    array = []
    
    url = 'https://randomuser.me/api/'
    response = requests.get(url)
    json_data = json.loads(response.text)
        
    user =json.dumps( {
        "First": json_data["results"][0]['name']['first'],
        "Last": json_data["results"][0]['name']['last'],
        "Age": json_data["results"][0]['dob']['age'],
        "Gender": json_data["results"][0]['gender'],
        "Lattitude": json_data["results"][0]['location']['coordinates']['latitude'],
        "Longitude": json_data["results"][0]['location']['coordinates']['longitude']
    })    
    array.append(user)
    return array    
    

def ReadAws(array):    
    s3 = boto3.resource('s3')
    body = str(json.dumps(array).encode('UTF-8'))
    s3.Bucket('nathanrhoda-machinelearning').put_object(Key='userdata.json', Body=body)

if __name__ == "__main__":        
    userArray = GenerateRandomUserData()    
    ReadAws(userArray)    
    print('Done')
