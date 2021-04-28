"""

Requests a token from the Altitude Angel token endpoint
https://auth.altitudeangel.com/oauth/v2/token

stores it into token.json

"""



import os, sys
import requests
import secrets
import logging
import datetime
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PATH_TOKEN = os.path.join( BASE_DIR, 'token.json')

now = datetime.datetime.utcnow()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

URL_TOKEN = 'https://auth.altitudeangel.com/oauth/v2/token'

payload = {
    "client_id":secrets.client_id,
    "client_secret":secrets.client_secret,
    "grant_type":"client_credentials",
    "scope":"surveillance_api",
    "token_format":"jwt",
    "device_id":secrets.sensor_id
}

session = requests.Session()

# setting "data" argument forces 'Content-Type': 'application/x-www-form-urlencoded'
request = requests.Request('POST', URL_TOKEN , data = payload).prepare()

logging.info('Making request..')
response = session.send( request )
logging.info(response)

if response.ok is False:
    raise RuntimeError("Response not OK!")


# Grab the JSON token
response_json = response.json()
response_json.update({"_timestamp": str(now.isoformat()) })
with open(PATH_TOKEN, 'w') as f:
    json.dump(response_json, f, indent=1)




logging.info(f'Wrote token to {PATH_TOKEN}')
    