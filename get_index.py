import pprint
import requests


def index_get(host, index, doc_type, id):
	pp = pprint.PrettyPrinter(indent=1)
	url = host + '/' + index + '/' + doc_type + '/' + str(id) + '?pretty'
	header = {'Content-Type': 'application/json'}
	response = requests.get(url, headers=header)
	if response.status_code == 200:
		return pp.pprint(response.json())
	else:
		raise ValueError('Some error!!')

index_get(host='http://localhost:9200', index='megacorp', doc_type='employee', id=3)
