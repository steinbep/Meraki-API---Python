#!/usr/bin/python

import meraki
import json

#
# Python Script Using Meraki API to find MAC or IP address in Dashboard
# Prints out the Network Name, Device Name, and IP or MAC
#

# Enter User's API Key
apikey = 'xxxxxx'

# Enter Organization ID Here
organizationid = 'xxxxxxxxx'

#User input to determine IP or MAC Search
answer = input('Do you have the MAC address? (y or n): ')

#IF Statement to start looping through for MAC lookup.
if answer == ('yes') or answer == ('Yes') or answer == ('YES') or answer == ('Y') or answer == ('y') :

    #User input of MAC Address
    mac = input('MAC: ')

    #Network lookup
    networks = meraki.getnetworklist(apikey, organizationid, suppressprint=True)

    #Loop through Network
    for row in networks:

        #Device Lookup
        devices = meraki.getnetworkdevices(apikey, row['id'], suppressprint=True)
        #print(format(str(row['id'])))

        #Loop through each device in network
        for device in devices:

            #Client Lookup
            clients = meraki.getclients(apikey, device['serial'], suppressprint=True)
            #print(format(str(device['serial'] + '\n')) + (str(device['mac'])))

            #Loop to find client
            for client in clients:
                #print(format(str(client['mac'] + '\n')))

                #Condition match statement
                if mac == (client['mac']):
                    print(format('Network Name: ') + (str(row['name'] + '\n')) + ('Device Name: ') + (str(client['description'] + '\n')) + ('Device IP: ') + (str(client['ip'] + '\n')))
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break

    #Print Statement for not found in loop
    else:
        print ('MAC Not Found')


#Else Statement to start IP lookup
else:
    
    #User input of MAC Address
    ip = input('IP: ')


    #Network lookup - API
    networks = meraki.getnetworklist(apikey, organizationid, suppressprint=True)


    #Loop through Network
    for row in networks:

        #Device Lookup
        devices = meraki.getnetworkdevices(apikey, row['id'], suppressprint=True)
            #print(format(str(row['id'])))

        #Loop through each device in networ
        for device in devices:

            #Client Lookup
            clients = meraki.getclients(apikey, device['serial'], suppressprint=True)
            #print(format(str(device['serial'] + '\n')) + (str(device['mac'])))

            #Loop to find client
            for client in clients:
                #print(format(str(client['mac'] + '\n')))

                #Condition match statement
                if ip == (client['ip']):
                    print(format('Network Name: ') + (str(row['name'] + '\n')) + ('Device Name: ') + (str(client['description'] + '\n')) + ('Device MAC: ') + (str(client['mac'] + '\n')))
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print ('IP Not Found')  
                                   
