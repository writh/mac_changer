#!/user/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Use this option to choose the interface to change its MAC address.")
    parser.add_option("-m", "--mac", dest="new_mac", help="Use this option to choose the desired new MAC address.")
    return parser.parse_args()
    if not options.interface:
        parser.error("[-] you forgot the interface, dummy")
    elif not options.new_mac:
        parser.error("[-] you forgot the mac, dummy")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw","ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)