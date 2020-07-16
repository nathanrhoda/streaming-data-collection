import requests

def GenerateRandomUserData():    
    url = 'https://randomuser.me/api/'
    response = requests.get(url)
    print(response.json())


if __name__ == "__main__":
    GenerateRandomUserData()
    