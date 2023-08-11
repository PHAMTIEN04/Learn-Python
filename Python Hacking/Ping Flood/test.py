import subprocess
import time

def scan_wifi():
    result = subprocess.run(['netsh', 'wlan', 'show', 'network', 'mode=Bssid'], capture_output=True, text=True)
    return result.stdout

def deauth_bssid(bssid):
    subprocess.run(['netsh', 'wlan', 'disconnect', 'interface="Wi-Fi"'])
    time.sleep(2)
    subprocess.run(['netsh', 'wlan', 'connect', 'ssid="non_existent_ssid"', 'interface="Wi-Fi"'])
    time.sleep(2)
    subprocess.run(['netsh', 'wlan', 'disconnect', 'interface="Wi-Fi"'])
    time.sleep(2)
    subprocess.run(['netsh', 'wlan', 'connect', 'ssid="non_existent_ssid"', 'bssid=' + bssid, 'interface="Wi-Fi"'])

def main():
    while True:
        print("Scanning WiFi networks...")
        networks = scan_wifi()
        print(networks)  # Display the available networks
        bssid_to_deauth = input("Enter the BSSID of the network to deauthenticate (or 'exit' to quit): ")
        if bssid_to_deauth.lower() == 'exit':
            break
        deauth_bssid(bssid_to_deauth)

if __name__ == "__main__":
    main()
