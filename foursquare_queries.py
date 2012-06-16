#import pprint as pp
import json
import requests

meter_to_mile_convert =1609
categories_dict= {}
categories_dict['tennis'] = ['4e39a956bd410d7aed40cbc3',#Tennis Court
							'4e39a9cebd410d7aed40cbc4']#College Tennis Court

def grab_venues(sport,lat, lon):
	url = 'https://api.foursquare.com/v2/venues/search'
	queries=''
	for query in categories_dict[sport]:
		queries+=query+","
	radius_miles = 5*meter_to_mile_convert
	payload = {
			'oauth_token':'YPVB42OFP2ZMDB4GD5YVRJF4SA1UDTQJNOGA32QQVTPFMATP',# oauth_token
			'categoryId':queries,
			'll':lat+","+lon,
			'radius':radius_miles
}
	r = requests.get(url,params=payload)
	#print r.url
	#pp.pprint(json.loads(r.text))
	return r.text
"""
grab_venues(
	'tennis',#sport
	'40.7',#latitude
	'-74',#longitude
)
"""

#print grab_venues('tennis','40.7','-74')
