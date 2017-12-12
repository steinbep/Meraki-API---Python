#!/usr/bin/python

import meraki
import json
import csv

#
# Python Script Using Meraki API to Inventory devices by vendor MAC (First 3 octets)
# Writes the data to CSV
# Network Name, Device Name, and IP Address
#

# Enter User's API Key
apikey = 'XXXXXXXXX'

# Enter Organization ID Here
organizationid = 'XXXXXXX'

#Network lookup
networks = meraki.getnetworklist(apikey, organizationid, suppressprint=True)

#Loop through Network
for row in networks:
    #print(row)
    
    #Device Lookup
    devices = meraki.getnetworkdevices(apikey, row['id'], suppressprint=True)
    #print(devices)

    #Loop through each device in network
    for device in devices:
        print (device['serial'])

        #UPlink Call
        uplink = meraki.getdeviceuplink(apikey, device['networkId'], device['serial'], suppressprint=True)
        #print (uplink)

        #loop to find active uplink and and append the Network Name and PublicIP to a csv
        for link in uplink:
            if link['status'] == 'Active':
                with open('Public_IP.csv', 'a', newline='') as wr:
                    a = csv.writer(wr, delimiter=',' )
                    data = [str(row['name']), str(link['publicIp'])]
                    a.writerow(data)
                #print (((str(row['name'] + ', ')) + (str(link['publicIp']))))
                
