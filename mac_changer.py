#!/usr/bin/env python

import subprocess
import optparse
import re

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help = "New Mac Address")
    (options, argument) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify interace, use -- help for more options")
    elif not options.new_mac:
        parser.error("Pleases specify new mac, use --help for more options")
    return options

def change_mac(interface, new_mac):
    print("changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("could not read mac address")

options = get_argument()
current_mac = get_current_mac(options.interface)
print("current mac =" + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("mac address was successfully changed to " + options.new_mac)
else:
    print("could not change mac address.")
