import redis

r = redis.Redis('redis-service', port=6379)

r.set('key', 'value')
print(r.get('key'))
