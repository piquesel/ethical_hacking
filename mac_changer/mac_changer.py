#!/usr/bin/env python3

import subprocess
import optparse
import re

# Create a parse object (OptionParser is the class)
def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac",
                      help="New MAC address")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more \
                     info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    #mac_address_search_result = re.search(r"(\w{2}:){5}\w{2}", ifconfig_result)
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", \
                                          ifconfig_result.decode('utf-8'))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print('[-] Could not read MAC address.')

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

#change_mac(options.interface, options.new_mac)


