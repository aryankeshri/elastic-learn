import pprint
import requests


def index_create(host, index, doc_type, id, data):
	pp = pprint.PrettyPrinter(indent=1)
	url = host + '/' + index + '/' + doc_type + '/' + str(id) + '?pretty'
	header = {'Content-Type': 'application/json'}
	request = requests.put(url, headers=header, json=data)
	if request.status_code == 201:
		return pp.pprint(request.json())
	else:
		raise ValueError('Some error!!')
