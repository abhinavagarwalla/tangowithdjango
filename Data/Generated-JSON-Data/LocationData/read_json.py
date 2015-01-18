import json
import os

for fn in os.listdir('.'):
	if os.path.isfile(fn):
		with open(fn) as json_file:
			data = json.load(json_file)
			if(data['status'] != 'ZERO_RESULTS'):
				print ("new google.maps.LatLng(%f ,%f)," % (data['results'][0]['geometry']['location']['lat'],data['results'][0]['geometry']['location']['lng']))