#!/user/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="user this option to choose the interface to change its MAC address")

parser.parse_args()

interface = raw_input("interface > ")
new_mac = raw_input("new MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])