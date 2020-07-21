import redis

redis = redis.Redis(host='localhost',port=6379,db=0,decode_responses=True)

def redis_get(key):
    return redis.get(key)


def redis_set(key,value,timeout=60):
    return redis.set(key,value,timeout)


def redis_delete(key):
    return redis.delete(key)


if __name__ == '__main__':
    # redis_set('hhh','ggg')
    print(redis_get('hhh'))
