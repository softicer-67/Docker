import redis

if __name__ == '__main__':

    with redis.Redis(host='redis', port=6379) as client:
        while True:
            task = input("Введите пример: ")
            if task == 'stop':
                print('Вы завершили программу.')
                break
            client.lpush('tasks', task)