import requests
import json

def get_location(api, ip):
        url = 'https://api.ipgeolocation.io/ipgeo?apiKey=' + api + '&ip=' + ip + '&city,country_name&output=json'

        x = requests.get(url)

        y = x.text

        z = json.loads(y)

        ip = z["ip"]
        city = z["city"]
        country = z["country_name"]
        get_location.response = 'Ip:' + ip + ' Country:' + country + ' City:' + city
