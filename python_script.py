import requests 

url = 'https://api.zoopla.co.uk/api/v1/property_listings.json?county=Derbyshire'

response = requests.get(url)

place_ids = [place['place_id'] for place in response.json()['listing']]

print(place_ids)
