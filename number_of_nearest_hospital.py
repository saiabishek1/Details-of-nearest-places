import os
import urllib
import xml.dom.minidom as mdom

latitude=#Enter Latitude
longtitude=#Enter Longtitude
base_url='https://maps.googleapis.com/maps/api/place/search/xml?location='+latitude+','+longtitude+'&rankby=distance&types=hospital&sensor=false&key=[ENTER API KEY]'
response=urllib.urlopen(base_url)
data=response.read()

response.close()
dom=mdom.parseString(data)
xmlTag=dom.getElementsByTagName('place_id')
for pid in xmlTag:
	pid=pid.toxml().replace('<place_id>','').replace('</place_id>','')
	details_url='https://maps.googleapis.com/maps/api/place/details/xml?placeid='+pid+'&key=[ENTER API KEY]'
	response=urllib.urlopen(details_url)
	data=response.read()
	response.close()
	dom=mdom.parseString(data)
	phone_number=dom.getElementsByTagName('formatted_phone_number')
	try:
		print phone_number[0].toxml().replace('<formatted_phone_number>','').replace('</formatted_phone_number>','')
		break
	except:
		pass
