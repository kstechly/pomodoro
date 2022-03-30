from threading import Timer
import time
from math import floor
import time
import winsound
import json
from os import path

if path.isfile('log.json') is False:
    with open('log.json','w') as f:
        f.write("[]")
        print("Created blank log file.")

def pomo_beep():
    for x in range(0,3):
        winsound.Beep(440, 600)

def pomo_end():
    pomo_beep()
    print("\nDone!")
    print("Category?")
    cat = input()
    print("Project?")
    proj = input()
    numprev = 0
    timestamp = time.time()
    with open("log.json") as f:
        data = json.load(f)
    data.append({"Timestamp": str(timestamp), "Project": proj, "Category": cat})
    numprev = len([x for x in data if x["Category"]==cat])
    with open("log.json",'w') as f:
        json.dump(data, f)
    print("Logged. You've now completed "+str(numprev)+" pomodoros in this category.")

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


    