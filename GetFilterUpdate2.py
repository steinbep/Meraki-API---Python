#!/usr/bin/python

import meraki, json, creds, pprint

#
# Python Script Using Meraki API to return all content filter settings
#

# Enter User's API Key
apikey = creds.apikey

# Enter Organization ID Here
organizationid = creds.orgid
 	
#Network lookup
networks = meraki.getnetworklist (apikey, organizationid, suppressprint=True)

for row in networks:
	updatefilter = meraki.getcontentfilter(apikey, row['id'], suppressprint=True)
	print(row['name'])
	try:
		pprint.pprint(updatefilter)
	except:
		pprint.pprint('Skipped')


