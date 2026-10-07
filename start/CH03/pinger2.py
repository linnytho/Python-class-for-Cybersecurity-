#!/usr/bin/env python3
# Second example of pinging from Python
# By 

import os 

# assign prefix
ip_prefix = "192.168.0."

for final_octet in range(254):
    # set IP address
    address = ip_prefix + str(final_octet+ 1)

    # Build Ping CMD
    ping_cmd = f"ping -c 1 -w 1 {address} > /dev/null 2>&1"
    # RUn ping
    status_code = os.system(ping_cmd)
    #print status
    # #print(status_code)
    if status_code == 0:
        print (f"{address} ONLINE")
    else:
        print(address, "Offline")