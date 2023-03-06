from flask import Flask
from flask_cors import CORS

import flask
import http.client
import json
import time

appName = "WebTraffic"
bbnApp = Flask(appName)
CORS(bbnApp)

@bbnApp.route("/iphandler", methods=["GET"])
def refreshIPs():
    print("Extracting IP from Log")
    def GetIP(line, start_index):
        index = start_index
        ip    = ""

        while not line[index] == ' ':
            ip += line[index]
            index += 1
        ip += '\n'
        return ip

    # Open the server log that contains web traffic information
    input = open('.\\log\\access.log', 'r')
    ipList = []

    #For each instance in the log
    for instance in input:
        #Initialize the character index of the new instance
        index      = 0
        ip_index   = 0
        
        #Skips all instances that begin with a colon
        if instance[index] == ':':
            continue

        #Add IP Address from current line into IP List
        ipList.append(GetIP(instance, ip_index))

    # Get rid of duplicate IP Addresses
    ipList = list(set(ipList))

    # Create the output file and write IP Addresses
    output = open('.\\log\\cleanIP.txt', 'w')
    output.writelines(ipList)

    # Close files to finish reading and writings
    input.close()
    output.close()
def feedIP():
    print("IP Feeder Reached")

    #IP Geo Location API
    conn = http.client.HTTPSConnection("ip-geo-location.p.rapidapi.com")

    # API Request Header
    headers = {
        'X-RapidAPI-Key': "fc951c16a0msha71f61569ee9a22p103a8ajsnf682365ff752",
        'X-RapidAPI-Host': "ip-geo-location.p.rapidapi.com"
        }

    ipList = open('.\\log\\cleanIP.txt')
    dictCoordinates = {}

    for ip in ipList:
        ip = ip.strip()
        requestString = f'/ip/{ip}?format=json'

        conn.request("GET", requestString, headers=headers)
        res = conn.getresponse()
        data = json.loads(res.read())
        dictCoordinates[f'{data["ip"]}'] = format(f'{data["location"]["latitude"]},{data["location"]["longitude"]}')

    conn.close() 
    return json.dumps(dictCoordinates)

@bbnApp.route("/users", methods=["GET"])
def users():
    print("users endpoint reached. . .")
    with open("users.json", "r") as f:
        data = json.load(f)
        data.append({
            "username": "user4",
            "pets": ["hamster"]
        })

    return flask.jsonify(data)


@bbnApp.route("/")
def hello():
    return "Hello, BBN!"

if __name__ == "__main__":
    bbnApp.run("localhost", 7070)