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

#User Input of filename
print('Enter a file name below,\nthe .csv will be appended to the name given')
filename = input('Name: ')

#User input of MAC Address
mac = input('Input first 3 octets of the MAC: ')

#Network lookup
networks = meraki.getnetworklist(apikey, organizationid, suppressprint=True)

#Loop through Network
for row in networks:

    #Device Lookup
    devices = meraki.getnetworkdevices(apikey, row['id'], suppressprint=True)
    #print(format(str(row)))
    
    #Loop through each device in network
    for device in devices:

        #Client Lookup
        clients = meraki.getclients(apikey, device['serial'], suppressprint=True)
        #print(format(str(device['serial'] + '\n')) + (str(device['mac'])))

        #Loop to find client
        for client in clients:
            #print(format(str(client)))

            if mac in (client['mac']):
                with open(filename + '.csv', 'a', newline='') as wr:
                    #fieldnames = ['Network Name', 'Device Name', 'Device IP']
                    a = csv.writer(wr, delimiter=',' )
                    data = [str(row['name']), str(client['description']), str(client['ip'])]
                    a.writerow(data)
                #print(format('Network Name: ') + (str(row['name'] + '\n')) + ('Device Name: ') + (str(client['description'] + '\n')) + ('Device IP: ') + (str(client['ip'] + '\n')))
                
