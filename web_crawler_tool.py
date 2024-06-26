import requests

base_url = 'https://r.jina.ai/'

input_url = input("Enter a URL other than social media : ")

url = base_url + input_url

response = requests.get(url)

if response.status_code == 200:
    print("Success!")
    print(response.content)  
else:
    print(f"Failed with status code: {response.status_code}")
