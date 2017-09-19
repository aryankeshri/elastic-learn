#!/usr/bin/env python3

import json
import pprint
import requests
from .create_index import index_create
from .get_index import index_get

pp = pprint.PrettyPrinter(indent=1)
HOST = 'http://localhost:9200'

data = {
    "first_name" : "aryan",
    "last_name" :  "Keshri",
    "age" :        259,
    "about" :      "I love to go rock climbing",
    "interests": [ "games", "music" ]
}

# headers={'Content-Type': 'application/json'}
# response = requests.get(HOST + "/megacorp/employee/_search", headers={'Content-Type': 'application/json'})
# pp.pprint(response.json())



create = index_create(host=HOST, index='megacorp', doc_type='employee', id=4, data=data)
pp.pprint(create.json())

get = get_index(host=HOST, index='megacorp', doc_type='employee', id=4)
pp.pprint(get.json())

curl -XGET 'localhost:9200/megacorp/employee/_search?pretty'
curl -XGET 'localhost:9200/megacorp/employee/_search?q=last_name:Smith&pretty'
curl -XGET 'localhost:9200/megacorp/employee/_search?pretty' -H 'Content-Type: application/json' -d '{"query": {"match" :{"last_name": "Smith"}}}'


def search(host, index, doc_type):
	pp = pprint.PrettyPrinter(indent=1)
	url = host + '/' + index + '/' + doc_type + '/_search?pretty'
	header = {'Content-Type': 'application/json'}
	response = requests.get(url, headers=header)
	if response.status_code == 200:
		return pp.pprint(response.json())
	else:
		raise ValueError('Some error!!')

def search_query(host, index, doc_type, key, value):
	pp = pprint.PrettyPrinter(indent=1)
	url = host + '/' + index + '/' + doc_type + '/_search?q=' + str(key) + ':' + str(value) + 'pretty'
	header = {'Content-Type': 'application/json'}
	response = requests.get(url, headers=header)
	if response.status_code == 200:
		return pp.pprint(response.json())
	else:
		return 'Not found'

def search_with_query(host, index, doc_type, query):
	pp = pprint.PrettyPrinter(indent=1)
	url = host + '/' + index + '/' + doc_type + '/_search?pretty'
	header = {'Content-Type': 'application/json'}
	response = requests.get(url, headers=header, data=query)
	if response.status_code == 200:
		return pp.pprint(response.json())
	else:
		return 'Not found'