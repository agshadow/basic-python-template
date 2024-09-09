#uses python-dotenv module

from dotenv import load_dotenv


import os 

load_dotenv()
print(os.environ.get('emailUsername'))
print(os.environ.get('emailPassword'))
