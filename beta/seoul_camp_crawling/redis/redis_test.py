import redis
r = redis.Redis(host='54.180.186.96', port=5000 ,decode_responses=True)

r.set('foo', 'bar')
print(r.get('foo'))