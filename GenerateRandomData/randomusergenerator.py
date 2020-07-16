import requests
import json

def GenerateRandomUserData():    
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
    return user    
    


if __name__ == "__main__":
    user = GenerateRandomUserData()
    print(user)
    