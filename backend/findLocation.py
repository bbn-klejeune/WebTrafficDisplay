import http.client
import time
import json

#IP Geo Location API
conn = http.client.HTTPSConnection("ip-geo-location.p.rapidapi.com")

# API Request Header
headers = {
    'X-RapidAPI-Key': "fc951c16a0msha71f61569ee9a22p103a8ajsnf682365ff752",
    'X-RapidAPI-Host': "ip-geo-location.p.rapidapi.com"
    }

ipList = open('.\\log\\cleanIP.txt')

for ip in ipList:
    ip = ip.strip()
    print(ip)
    requestString = f'/ip/{ip}?format=json'

    conn.request("GET", requestString, headers=headers)
    res = conn.getresponse()
    data = json.loads(res.read())
    latlng = data["location"]["latitude"] + data["location"]["longitude"]
    currentIp = data["ip"]
    print(currentIp, ':', latlng)
    time.sleep(1)

conn.close()