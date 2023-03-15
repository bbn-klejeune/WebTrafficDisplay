import http.client
import time
import json
import pymongo

def formatDBEntry(entry):

    ipDict = {"ip_address": entry["ip"],
              "latitude": entry["location"]["latitude"],
              "longitude": entry["location"]["longitude"],
              "flag": entry["country"]["flag"]["file"],
              "country": entry["country"]["code"],
              "state": entry["area"]["name"],
              "city": entry["city"]["name"],
              "timezone": entry["time"]["timezone"]}

    return ipDict

#IP Geo Location API
conn     = http.client.HTTPSConnection("ip-geo-location.p.rapidapi.com")
bbnAppDB = pymongo.MongoClient("mongodb://localhost:27017/")["bbnApp"]
locations = bbnAppDB["locations"]

# API Request Header
headers = {
    'X-RapidAPI-Key': "fc951c16a0msha71f61569ee9a22p103a8ajsnf682365ff752",
    'X-RapidAPI-Host': "ip-geo-location.p.rapidapi.com"
    }

ipList = open('.\\log\\cleanIP.txt')

for ip in ipList:
    requestString = f'/ip/{ip.strip()}?format=json'

    # print(ip, end="\n\n") #Debugging 
    conn.request("GET", requestString, headers=headers)
    res = conn.getresponse()
    data = json.loads(res.read())
    # print(data, end="\n\n") #Debugging
    record = formatDBEntry(data)
    # print(record, end="\n\n\n\n\n\n") #Debugging
    locations.insert_one(record)
    print("Loading. . .")
    print(record, end="\n\n\n\n\n\n\n\n")
    time.sleep(3)

conn.close()