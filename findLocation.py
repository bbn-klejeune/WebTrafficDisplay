import http.client
import string

#IP Geo Location API
conn = http.client.HTTPSConnection("ip-geo-location.p.rapidapi.com")

# API Request Header
headers = {
    'X-RapidAPI-Key': "fc951c16a0msha71f61569ee9a22p103a8ajsnf682365ff752",
    'X-RapidAPI-Host': "ip-geo-location.p.rapidapi.com"
    }

ipList = open('.\\log\\cleanIP.txt')
for ip in ipList:
    print(string.strip(ipList.readlines))
    # conn.request("GET", f"/ip/{ip}?format=json", headers=headers)
    # res = conn.getresponse()
    # data = res.read()
    # print(data.decode("utf-8"))

conn.close()