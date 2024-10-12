import redis

# Подключение к Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Установка значения
r.set('username', 'akrom')

# Получение значения
username = r.get('username')
print(username.decode())  # Вывод: akrom
