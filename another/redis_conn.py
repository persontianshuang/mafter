import redis

r = redis.Redis(host='localhost',port=6379)
r.set('ffffff','hhhhha')
print(r.get('ffffff'))
