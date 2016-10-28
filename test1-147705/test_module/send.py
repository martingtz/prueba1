import urllib2
import json
import sys 

def send_json_request(server_url, json_dict):
      	"""send a json object by post request to a url and expects a json response"""
      	req = urllib2.Request(server_url)
       	req.add_header('Content-Type','application/json')
      	response = urllib2.urlopen(req, json.dumps(json_dict))
      	out=response.read()+ " Code: "+ str(response.code)
        return out

#url ="http://localhost:9080"
url = "http://localhost:9080/"


if len(sys.argv) >= 2: #Checks if at least 2 params)
	dict = {"Tipo":"temperatura","Valor":float(sys.argv[1]),"ubicacion":1}
	print('sending please wait...')
	print(dict)
	r=send_json_request(url,dict)
	print (r)
else:
	print ('faltan parametros...')