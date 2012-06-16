import pprint as pp
import json
import requests


fields_id =	'4bf58dd8d48988d15f941735'#Fields
parks_id =  '4bf58dd8d48988d163941735'#parks
meter_to_mile_convert =1609
categories_dict= {}
categories_dict['tennis'] = ['4e39a956bd410d7aed40cbc3',#Tennis Court
							'4e39a9cebd410d7aed40cbc4']#College Tennis Court
categories_dict['basketball'] = ['4bf58dd8d48988d1e1941735',#basketball court
								 '4bf58dd8d48988d1ba941735']#college basketball
categories_dict['frisbee'] = [fields_id,parks_id]
categories_dict['soccer'] = [fields_id,parks_id]
categories_dict['dodgeball'] = [fields_id,parks_id]
categories_dict['tag']= [fields_id,parks_id]

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

#grab_venues('soccer','40.7','-74')
