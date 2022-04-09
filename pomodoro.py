from threading import Timer
import time
from math import floor
import time
import winsound
import json
from os import path
import requests

full_data = []
config = {}
api_url = ""


if path.isfile('config.json') is False:
    with open('config.json','w') as f:
        f.write("{'api_url':''}")
        print("Created empty config file.")
        print("Please edit config file to include server url. Logging disabled.")

with open('config.json','r') as f:
    config = json.load(f)
    api_url = config['api_url']
    if api_url == "":
        print("Please edit config file to include server url. Logging disabled.")

def pomo_beep():
    for x in range(0,3):
        winsound.Beep(440, 600)

def pomo_end():
    pomo_beep()
    print("\nDone!")
    print("Category?")
    timestamp = time.time()
    cat = input()
    print("Project?")
    proj = input()
    numprev = 0
    full_data = get_data()
    response = add_data(timestamp,proj,cat)
    numprev = len([x for x in full_data if x["Category"]==cat])
    if response.status_code == 200:
        print("Logged. You've now completed "+str(numprev+1)+" pomodoros in this category.")
    else:
        print(response.status_code)

def get_data():
    #with open("log.json") as f:
    #    return json.load(f)
    return requests.get(api_url+"/get").json()

def add_data(timestamp,proj,cat):
    #data.append({"Timestamp": str(timestamp), "Project": proj, "Category": cat})
    #with open("log.json",'w') as f:p
    #    json.dump(data, f)
    new_data = {'Timestamp':timestamp, 'Project':proj,'Category':cat}
    response = requests.post(api_url+"/post", data=new_data)
    return response

def start_countdown(minutes):
    minute_ctd(minutes*60)
    t = Timer(minutes*60,pomo_end)
    t.start() 

def minute_ctd(remaining):
    if remaining > 0:
        print(str(floor(remaining/60))+":"+str('{:02d}'.format(remaining%60))+" remains   ",end="\r")
        remaining-=1
        time.sleep(1)
        minute_ctd(remaining)


    
