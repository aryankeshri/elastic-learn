from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

# use for insert data in elastic search index
res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
print(res, type(res))

# Query for get any value according to query
res = es.get(index="test-index", doc_type='tweet', id=1)
print(res['_source']['text'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got {} Hits:" .format(res['hits']['total']))
for hit in res['hits']['hits']:
	pass
    # print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
