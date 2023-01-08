import redis

with redis.Redis(host='redis', port=6379) as client:
    while True:
        task = client.brpop('tasks')[1].decode('utf-8')
        print(eval(task))
