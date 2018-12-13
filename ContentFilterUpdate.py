#!/usr/bin/python

import meraki, json, creds

#
# Python Script Using Meraki API to update all content filter settings in Dashboard
#

# Enter User's API Key
apikey = creds.apikey

# Enter Organization ID Here
organizationid = creds.orgid

contentFilterUpdate = {
    "urlCategoryListSize": "topSites",
    "blockedUrlCategories": [
							{'id': 'cf_011'	 'name': 'Adult and Pornography'},
							{'id': 'cf_018'	 'name': 'Dating'},
							{'id': 'cf_027'	 'name': 'Gambling'},
							],
    "blockedUrlPatterns": 	[
							'www.blockedsite.com',
							],
    "allowedUrlPatterns": 	[
							'www.allowedsite.com'
							]
	}

#Network lookup
networks = meraki.getnetworklist (apikey, organizationid, suppressprint=False)

for row in networks:
	updatefilter = meraki.updatecontentfilter(apikey, row['id'], contentFilterUpdate)
	# print(updatefilter)
