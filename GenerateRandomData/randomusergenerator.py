import requests
import json

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
    
def WriteJsonToAFile(userArray):
    with open('userdata.txt', 'w') as outfile:
        json.dump(userArray, outfile)


if __name__ == "__main__":
    userArray = GenerateRandomUserData()    
    WriteJsonToAFile(userArray)    
    print('Done')
    