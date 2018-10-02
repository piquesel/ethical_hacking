#!/usr/bin/env python3

import subprocess

interface = input("interface > ")
new_mac = input("new MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# More secure version
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

