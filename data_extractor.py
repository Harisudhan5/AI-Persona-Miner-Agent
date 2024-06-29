# s = 777ZpjVNYRd8kyyU
import requests
from googlesearch import search
from linkedin_api import Linkedin
from dotenv import load_dotenv
import os 

load_dotenv()

# Data Extractor 
'''
url = "https://verchoolfoz.vercel.app/next/api/user/detail/LB2giDDub4OpoWLG2ZPGT8eD56i1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()['data']
    print("Input Data : ",data)
else:
    print(f"Failed to retrieve data: {response.status_code}")'''

def linkedin_scrape(url):
    parameter_1, parameter_2 = os.getenv('KEY1'), os.getenv('KEY2')
    api = Linkedin(parameter_1, parameter_2)
    profile = api.get_profile(url)
    return str(profile)

def search_web(query):
    url_array = []
    result = search(query, num_results=1, safe = None, lang="en")
    for url in result:
        url_array.append(url)
    return url_array

def web_crawl(web_url):
    base_url = 'https://r.jina.ai/'
    input_url = web_url
    url = base_url + input_url
    response = requests.get(url)
    if response.status_code == 200:
        return str(response.content)  
    else:
        return ""


'''print("User Name : ",data['name'])
print("User Company : ",data['company'])
print("User Position : ",data['position'])

name = data['name']
company = data['company']
position = data['position']'''

# For custom testing 
name = "Dev Patel"
company = "Verchool"
position = "Head of Technology"

linkedin_search = search_web(name + company + position + "LinkedIn")

linkedin_username = linkedin_search[0].split('/')[-1]
print("Linkedin Username of "+name+" : "+linkedin_username)

company_search = search_web(company)

company_url = company_search[0]
print(company+" URL : "+company_url)

linkedin_data = linkedin_scrape(linkedin_username)

if "linkedin" in company_url:
    company_url = company_url.split('/')[-1]
    company_data = linkedin_scrape(company_url)
else:
    company_data = web_crawl(company_url)

print(linkedin_data)
print("=======================")
print(company_data)






