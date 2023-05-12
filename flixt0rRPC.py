from lib import page_info, rpc
import time
import os
import art
import sys
from datetime import datetime
from datetime import timedelta
import json

def startRPC(infos):


    clear()
    art.tprint("flixt0rRPC")
    print("")
    print("[INFORMATIONS]")
    print("")
    print("Movie : " + infos[0] + " | Film duration : " + infos[1] + " minutes")
    print("")
    print("[RPC STARTED]")
    print("[Close to stop]")

    #start_time = time.mktime(time.localtime() + int(infos[1])*60)
    time_sec = int(infos[1])*60
    time_sec = timedelta(seconds=time_sec)
    #td = time.mktime(start_time + (datetime.min + time_sec).time())
    t2 = datetime.now() + timedelta(minutes=int(infos[1])*60)
    t2 = json.dumps(t2, indent=4, sort_keys=True, default=str)

    test = True
    while test:

        try:
            rpc_obj = rpc.DiscordIpcClient.for_platform("1106247042281504940")
            activity = {
                    "timestamps": {
                        "start": time.mktime(time.localtime()),
                        "end": time.mktime(time.localtime())+ int(infos[1])*60,
                    },
                    "details": infos[0],  
                    "assets": {
                        "large_text": infos[0],
                        "large_image": infos[2],
                        "small_image": "https://s1.bunnycdn.ru/assets/sites/flixtor/logo.png",
                        "small_text": "Flixtor"
                    },
            }

            rpc_obj.set_activity(activity)

        except KeyboardInterrupt:
            test = False

        time.sleep(1)


def clear():

    if os.name == 'nt':
        os.system("cls")
        os.system("color 2")
    else:
        os.system("clear")

def term():

    art.tprint("flixt0rRPC")
    print("\n\n")
    print("    +[1] Start Flixtor RPC")
    print("    +[2] Exit")
    print("\n")

clear()
term()

terminal = True

while terminal:

    choice = input("flixt0rRPC > ")
    try:
        if choice == "1":

            clear()
            term()
            link = input("\nEnter movie link > ")
            try:
                infos = page_info.get_informations(link)
                startRPC(infos)

                clear()
                print("RPC started.")

            except Exception as e:

                print("Link error. Please try again with a valid Flixtor link.")
                print(e)
        
        elif choice == "2":

            print("See you next time :)")
            terminal = False

        elif int(choice) < 1 or int(choice) > 2:

            print("Please enter a correct value.")

    except ValueError:
        print("Please enter a correct value.")