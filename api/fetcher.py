import requests

# ROOT_URL = "https://opensky-network.org/api"


def states_accessor():
    # Go through Doc API examples
    url = f"https://opensky-network.org/api/states/all"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    # print(r.json())


def tracks_accessor():
    # From reading documentation, running this through is implied first!
    # flights_accessor()
    url = f"https://opensky-network.org/api/tracks/all?icao24=a808c5&time=1641142800"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    # print(r.json())
    # BUT this is de-activated :(

def flights_accessor():
    url = f"https://opensky-network.org/api/flights/all?begin=1641142800&end=1641148800"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    return r.json()