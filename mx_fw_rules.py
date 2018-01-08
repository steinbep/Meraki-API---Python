#!/usr/bin/python

import meraki
import json

#
# Python Script Using Meraki API to collect all MX L3 Firewall Rules in all Networks to CSV file.
# Returns Site, Comments, Source port and CIDR, Destination port and CIDR. 
#

# Enter User's API Key
apikey = 'xxxxxx'

# Enter Organization ID Here
organizationid = 'xxxxxxxxx'

#User Input of filename
print('Enter a file name below,\nthe .csv will be appended to the name given')
filename = input('Name: ')

#Network lookup
networks = meraki.getnetworklist(apikey, organizationid, suppressprint=True)
# print(format(str(networks)))

#Loop through Network
for row in networks:
    # Device Lookup
    rules = meraki.getmxl3fwrules(apikey, row['id'], suppressprint=True)

    # print(format(str(rules)))
    for rule in rules:
        # print (rule)
        try:
            with open(filename + '.csv', 'a', newline='') as wr:
                a = csv.writer(wr, delimiter=',' )
                data = [str(row['name']), str(rule['comment']), str(rule['policy']), str(rule['protocol']), str(rule['srcPort']), str(rule['srcCidr']), str(rule['destPort']), str(rule['destCidr'])]
                a.writerow(data)
        except:
            pass
