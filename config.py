import os

from dotenv import load_dotenv

load_dotenv()


BASE_URL = os.getenv('BASE_URL')
PERSONAL_ID = os.getenv('PERSONAL_ID')
BIRTH_DATE = os.getenv('BIRTH_DATE')
