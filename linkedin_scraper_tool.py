from linkedin_api import Linkedin
from dotenv import load_dotenv
import os 

load_dotenv()

parameter_1, parameter_2 = os.getenv('KEY1'), os.getenv('KEY2')


api = Linkedin(parameter_1, parameter_2)

profile = api.get_profile('tom-yeh')

print("Linked Profile : ",profile)
