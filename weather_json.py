import json
import pprint

with open("weather.json", "r") as f:
    #data = f.read()
    #print(type(data))
    data = json.load(f)
    print(type(data))
    print(data)
    pprint.pprint(data)

    print("===== Weather Information ======")
    print(f"Location: {data["name"]}")
    print(f"Temperature: {data["main"]["temp"]}")
    print(f"Temperature: {data["weather"][0]["description"]}")