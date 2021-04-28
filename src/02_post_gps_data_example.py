import os, sys
import requests
import secrets
import logging
import datetime
import json
from uuid import uuid4
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

BASE_DIR = Path(__file__).resolve().parent
PATH_TOKEN = BASE_DIR.joinpath('token.json')

URL_SURVEILLANCE = 'https://surveillance-api.altitudeangel.com'
URL_REPORT = "{0}/v1/position-reports".format( URL_SURVEILLANCE )

LAT, LON = 52.06824956187701, -0.6290870698926041 # Cranfield ;)

session = requests.session()
now = datetime.datetime.utcnow()

with open( PATH_TOKEN ) as f:
    token = json.load( f )

access_token = token['access_token']

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {0}'.format( access_token )
}

# https://docs.altitudeangel.com/docs/surveillance-api#sending-position-reports
payload = {
    "positions":[{
        "id": str(uuid4()), 
        "sourceTimeStamp": str(now.isoformat()),
        "position": {
            "lat": LAT,
            "lon": LON
        }
    }]
}

# prep the request
request = requests.Request('POST', URL_REPORT , headers=headers, json=payload).prepare()
logging.debug(json.dumps( request.__dict__, indent=1, default=str))

# make the request
logging.info("Sending to AA")
response = session.send( request )

logging.info(response)

if response.ok is False:
    logging.error("Response not OK!")