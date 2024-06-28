import requests
from googlesearch import search


url = "https://verchoolfoz.vercel.app/next/api/user/detail/LB2giDDub4OpoWLG2ZPGT8eD56i1"

response = requests.get(url)

if response.status_code == 200:
    # Parse the JSON data
    data = response.json()['data']
    print("Input Data : ",data)
else:
    print(f"Failed to retrieve data: {response.status_code}")

def search_web(query):
    url_array = []
    result = search(query, num_results=1, safe = None, lang="en")
    for url in result:
        url_array.append(url)
    return url_array

print("User Name : ",data['name'])
print("User Company : ",data['company'])
print("User Position : ",data['position'])

name = data['name']
company = data['company']
position = data['position']

#name = data['name']
#company = data['company']
#position = data['position']

linkedin_search = search_web(name + company + position + "LinkedIn")

linkedin_url = linkedin_search[0]

print("Linkedin URL of "+name+" : "+linkedin_url)

company_search = search_web(company)

company_url = company_search[0]

print(company+" URL : "+company_url)






