import json
import pprint
import requests

pp = pprint.PrettyPrinter(indent=1)
HOST = 'http://localhost:9200'


# response = requests.get(HOST + "test-index/_search")
# pp.pprint(response.json())

# pp.pprint(response.headers)
# curl -XPUT 'localhost:9200/megacorp/employee/1?pretty' -H 'Content-Type: application/json' -d'
data = {
    "first_name" : "aryan",
    "last_name" :  "Keshri",
    "age" :        259,
    "about" :      "I love to go rock climbing",
    "interests": [ "games", "music" ]
}
# request = requests.put(HOST + "megacorp/employee/1?pretty",
headers={'Content-Type': 'application/json'}
response = requests.get(HOST + "/megacorp/employee/_search", headers={'Content-Type': 'application/json'})
pp.pprint(response.json())



index_create(host=HOST, index='megacorp', doc_type='employee', id=4, data=data)

