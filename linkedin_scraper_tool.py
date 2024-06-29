from linkedin_api import Linkedin
from dotenv import load_dotenv
import os 

load_dotenv()

parameter_1, parameter_2 = os.getenv('KEY1'), os.getenv('KEY2')


api = Linkedin(parameter_1, parameter_2)

profile = api.get_profile('tom-yeh')

print("Linked Profile : ",profile)
'''
def linkedin_scrape(url):
    parameter_1, parameter_2 = os.getenv('KEY1'), os.getenv('KEY2')
    api = Linkedin(parameter_1, parameter_2)
    profile = api.get_profile(url)
    return str(profile)

url = 'https://ae.linkedin.com/in/athwal'
splitter = url.split('/')[-1]
linkedin_base_url = 'https://www.linkedin.com/in/'
print("Splitter : ",splitter)
linkedin_url = linkedin_base_url + splitter
print("URL == ",linkedin_url)
print(linkedin_scrape(linkedin_url))
'''