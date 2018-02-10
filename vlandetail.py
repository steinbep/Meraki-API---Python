#!/usr/bin/python

import meraki, json, csv

#
# Python Script Using Meraki API to find subnet for deignated vlan
#

# Enter User's API Key
apikey = '***************'

# Enter Organization ID Here
organizationid = '*******'
vlan = 1

#Network lookup
networks = meraki.getnetworklist(apikey, organizationid, suppressprint=True)

#Loop through Network
for row in networks:
    vlantag = meraki.getvlandetail(apikey, row['id'], vlan, suppressprint=True)
    try:
        with open('VLANDETAIL.csv', 'a', newline='') as wr:
            a = csv.writer(wr, delimiter=',' )
            data = [str(row['name']), str(vlantag['name']), str(vlantag['subnet'])]
            a.writerow(data)
    except:
        continue
