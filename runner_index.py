import ConfigParser
import pickle

from Indexer.index import Index
from Indexer.index import DocSpace
from Crawler import crawl


Config = ConfigParser.ConfigParser()
Config.read("util/indexer.cfg")
url = Config.get("crawler","url")
doc_path = Config.get("parser","doc_path")
index = Index()
docSpace = DocSpace()
docMap = {}
termMap = {}
crawl.crawl(url, index, docSpace, docMap, termMap, doc_path=doc_path)

data = {}
data['index'] = index
data['docSpace'] = docSpace
data['docMap'] = docMap
data['termMap'] = termMap
pickle.dump(data,open('util/index_data.p','w'))
