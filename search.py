#!/usr/bin/env python3

import pprint
import requests


def search(host, index, doc_type):
	pp = pprint.PrettyPrinter(indent=1)
	url = host + '/' + index + '/' + doc_type + '/_search?pretty'
	header = {'Content-Type': 'application/json'}
	response = requests.get(url, headers=header)
	if response.status_code == 200:
		return pp.pprint(response.json())
	else:
		raise 'Not Found!!'

def search_query(host, index, doc_type, key, value):
	pp = pprint.PrettyPrinter(indent=1)
	url = host + '/' + index + '/' + doc_type + '/_search?q=' + str(key) + ':' + str(value) + '&pretty'
	header = {'Content-Type': 'application/json'}
	response = requests.get(url, headers=header)
	if response.status_code == 200:
		return pp.pprint(response.json())
	else:
		return 'Not found'

def search_with_query(host, index, doc_type, query):
	pp = pprint.PrettyPrinter(indent=1)
	url = host + '/' + index + '/' + doc_type + '/_search?pretty'
	print(url)
	header = {'Content-Type': 'application/json'}
	response = requests.get(url, headers=header, json=query)
	print(response)
	if response.status_code == 200:
		return pp.pprint(response.json())
	else:
		return 'Not found'



search(host='http://localhost:9200', index='megacorp', doc_type='employee')
search_query(host='http://localhost:9200', index='megacorp', doc_type='employee', key='_id', value='4')

query = {
    "query" : {
        "match" : {
            "last_name" : "Smith"
        }
    }
}

search_with_query(host='http://localhost:9200', index='megacorp', doc_type='employee', query=query)
