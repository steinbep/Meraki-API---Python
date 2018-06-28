#!/usr/bin/python

import meraki, json, csv, creds

#
# Python Script Using Meraki API to find MAC or IP address in Dashboard
# Prints out the Network Name, Device Name, and IP or MAC
#

# Enter User's API Key
apikey = creds.apikey

# Enter Organization ID Here
organizationid = creds.orgid

my_dict_48 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48}
my_dict_24 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24}
#User Input of filename
# print('Enter a file name below,\nthe .csv will be appended to the name given')
# filename = input('Name: ')


#Network lookup
networks = meraki.getnetworklist(apikey, organizationid, suppressprint=True)
# print(format(str(networks)))

for row in networks:
    devices = meraki.getnetworkdevices(apikey, row['id'], suppressprint=True)
    #print (row['name'])

    for device in devices:
        if 'MS' not in device['model']:
            continue
        elif '24' in  device['model']:
                try:
                    for item in my_dict_24:
                        ports = meraki.getswitchportdetail(apikey, device['serial'], item , suppressprint=True)
                        try:
                            if ports['accessPolicyNumber'] == None:
                                print (row['name'], device['name'], device['model'], item)
                            else:
                                continue
                        except:
                            pass
                except:
                    pass
        else:
            try:
                for item in my_dict_48:
                    ports = meraki.getswitchportdetail(apikey, device['serial'], item , suppressprint=True)
                    try:
                        if ports['accessPolicyNumber'] == None:
                            print (row['name'], device['name'], device['model'], item)
                        else:
                            continue
                    except:
                        pass
            except:
                pass
