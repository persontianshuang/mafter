import pymongo


_MongoengineConnect = 'mynihongo2'

_MongoUrl = 'localhost'

_Client = pymongo.MongoClient(_MongoUrl,27017)
_Db = _Client[_MongoengineConnect]
