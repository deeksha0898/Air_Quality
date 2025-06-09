import requests

headers = {"X-API-Key": "621b301f86a274ae03114faf9404d2d126637646811a760c949d39607af92296"}  # replace this
#params = {"country": "IN", "limit": 100}

#response = requests.get("https://api.openaq.org/v3/locations", params=params, headers=headers)

#print("Status code:", response.status_code)
#data = response.json()

#if "results" in data:
 #   for loc in data["results"]:
  #      city = loc.get("city", "N/A")
   #     name = loc.get("name", "N/A")
    #    print("City:", city, "| Location:", name)
#else:
 #   print("No results found:", data)

#import requests

url = "https://api.openaq.org/v3/parameters/2/latest?limit=1000"
#headers = {
   # "X-API-Key": "YOUR-OPENAQ-API-KEY"
#}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())