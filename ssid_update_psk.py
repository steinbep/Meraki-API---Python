#!/usr/bin/python

import meraki
import json

#
# Python Script Using Meraki API to update PSK for a single SSID in all networks. 
#

# Enter User's API Key
apikey = 'xxxxxx'

# Enter Organization ID Here
organizationid = 'xxxxxxxxx'

#User Inputs for SSID and  new/old PSK
netname = input('INPUT SSID: ')
oldpsk = input('OLD PSK YOU ARE CHANGING: ')
newpsk = input('NEW PSK: ')

#Network lookup
networks = meraki.getnetworklist(apikey, organizationid, suppressprint = True)

#Loop through Network
for row in networks:

    #print (row['id'])
    
    #Device Lookup
    data = meraki.getssids(apikey, row['id'], suppressprint = True)
    
    #if NoneType returned continue script;
    if data == None:
        continue
        
    for line in data:
        if netname in line['name']:
            psk = line['psk']
                        
            if psk == oldpsk:
                updatepsk = meraki.updatessid(apikey, row['id'], line['number'], line['name'] , enabled = 'true', authmode = 'psk', encryptionmode = 'wpa',psk = newpsk, suppressprint=True)
                print ('Completed Change for ' + (str(row['name'])))
                
