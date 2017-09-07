import os


import pymongo
MONGO_URI = 'localhost'
def pymg(highest,collections,port=MONGO_URI):
    client = pymongo.MongoClient(port, 27017)
    zhihu = client[highest]
    collections = zhihu[collections]
    return collections

coll = pymg('only','t_shit')
# path = '/Users/user/Desktop/T恤未上传数据'
# with open(path,'r') as f:
#     for x in f.readlines():
#         coll.update({'asin': x},{'$set':{'asin': x.split('\t')[1]}})
#         print(x.split('\t')[1])

root_path = '/Users/user/Desktop/T恤未上传数据'
txt_list = os.listdir(root_path)

for it in txt_list:
    this_path = os.path.join(root_path,it)
    with open(this_path,'r') as f:
        for x in f.readlines():
            coll.insert({'dsa':'dasdfasf'})
            # coll.update({'asin': x.split('\t')[1]},{'$set':{'asin': x.split('\t')[1]}})
            # print(x.split('\t')[1])
    print(this_path)
