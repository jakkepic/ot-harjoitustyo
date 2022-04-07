import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
    pass
except FileNotFoundError:
    pass

COSTCENTRE_FILENAME = os.getenv('COSTCENTRE_FILENAME') or 'costcentre.sqlite'
COSTCENTRE_FILE_PATH = os.path.join(dirname, '..', 'data', COSTCENTRE_FILENAME)

DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.sqlite'
DATABASE_FILE_PATH = os.path.join(dirname, '..', 'data', DATABASE_FILENAME)