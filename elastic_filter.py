import pprint
from elasticsearch import Elasticsearch


pp = pprint.PrettyPrinter(indent=1)
es = Elasticsearch()

# Filter the serarching results basic accourding to filter path(specific)
response_filter = es.search(index='test-index', filter_path=['hits.hits._id', 'hits.hits._type'])
pp.pprint(response_filter)

# matches any type of query(all) 
response_filter2 = es.search(index='test-index', filter_path=['hits.hits._*'])
pp.pprint(response_filter2)
