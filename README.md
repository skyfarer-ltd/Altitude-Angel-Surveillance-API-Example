# Altitude Angel Surveillance API Example

Most of the flow was lifted from the Altitude Angel [Surveillance-API documentation](https://docs.altitudeangel.com/docs/surveillance-api) & the [Scout Firmware](https://github.com/AltitudeAngel/Scout). 

Ultimately the goal is to appear on [https://www.dronesafetymap.com/](https://www.dronesafetymap.com/)

## Quickstart

1. Update credentials in [src/secrets.py](src/secrets.py)
2. `pip3 install -r requirements.txt`
3. `python3 src/01_auth_token.py`
4. You'll get [src/token.json](src/token.json)
5. `python3 src/02_post_gps_data_example.py`


## Obtaining credentials


1. Create an account at [AltitudeAngel](https://www.altitudeangel.com/developer-portal/)
2. [Raise a ticket](https://customerportal.altitudeangel.com/submit_ticket) with Altitude Angel to:
    1. Register a sensor ID `my.uav.sensor.001`
    2. Obtain `clientId` and `clientSecret`




## Tested on:

|Device|Python version|
|-|-|
|Macbook Air M1, 2020 / v11.2.2 |Python 3.9.4|
|Raspberry PI 3b+ / Raspbian Buster| Python 3.7.3 |


## References

- [https://www.altitudeangel.com/developer-portal/](https://www.altitudeangel.com/developer-portal/)
- [https://docs.altitudeangel.com/docs/surveillance-api](https://docs.altitudeangel.com/docs/surveillance-api)
- [https://docs.altitudeangel.com/docs/oauth2-bearer-tokens](https://docs.altitudeangel.com/docs/oauth2-bearer-tokens)
