import pprint
import requests

pp = pprint.PrettyPrinter(indent=1)
HOST = 'http://localhost:9200/'


response = requests.get(HOST + "test-index/_search")
pp.pprint(response.json())


