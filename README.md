**Redis — Полная документация**

---

## Описание Redis

**Redis (Remote Dictionary Server)** — это система управления базами данных, которая работает по принципу *ключ-значение*. Основной особенностью Redis является хранение данных в оперативной памяти (RAM), что обеспечивает высокую скорость доступа и обработки данных. Redis поддерживает множество структур данных, таких как строки, списки, множества, хэши и отсортированные множества.

### Преимущества Redis:
- **Высокая производительность** — Redis обрабатывает до миллионов запросов в секунду.
- **Множество типов данных** — поддержка различных структур данных позволяет использовать Redis для различных сценариев.
- **Постоянное хранилище** — несмотря на то, что данные хранятся в оперативной памяти, Redis поддерживает функции сохранения данных на диск.
- **Простота использования** — интерфейс Redis интуитивно понятен, и операции выполняются с минимальной задержкой.

## Установка Redis

### 1. Установка на Linux (Ubuntu):
```bash
sudo apt update
sudo apt install redis-server
```

### 2. Установка на MacOS с помощью Homebrew:
```bash
brew install redis
```

### 3. Запуск Redis:
После установки можно запустить Redis командой:
```bash
redis-server
```
Для подключения к Redis-клиенту:
```bash
redis-cli
```

## Основные команды Redis

### Строки (Strings)
Redis строки — это самый простой тип данных, который используется для хранения текста или чисел.

- **SET** — установить значение для ключа:
  ```bash
  SET mykey "hello"
  ```
- **GET** — получить значение по ключу:
  ```bash
  GET mykey
  ```
- **INCR** — увеличить числовое значение ключа:
  ```bash
  SET counter 10
  INCR counter  # Значение станет 11
  ```

### Списки (Lists)
Списки — это упорядоченные коллекции строк.

- **LPUSH** — добавить элемент в начало списка:
  ```bash
  LPUSH mylist "world"
  LPUSH mylist "hello"
  ```
- **LRANGE** — получить элементы из списка:
  ```bash
  LRANGE mylist 0 -1  # Выведет: ["hello", "world"]
  ```

### Множества (Sets)
Множества — это неупорядоченные коллекции уникальных строк.

- **SADD** — добавить элемент в множество:
  ```bash
  SADD myset "apple"
  SADD myset "banana"
  ```
- **SMEMBERS** — получить все элементы множества:
  ```bash
  SMEMBERS myset  # Выведет: ["apple", "banana"]
  ```

### Хэши (Hashes)
Хэши — это коллекции пар *поле-значение*.

- **HSET** — установить значение для поля в хэше:
  ```bash
  HSET user:1000 name "Akrom"
  HSET user:1000 age 18
  ```
- **HGET** — получить значение поля:
  ```bash
  HGET user:1000 name  # Выведет: "Akrom"
  ```

### Отсортированные множества (Sorted Sets)
Отсортированные множества — это множества, где каждому элементу присвоен числовой рейтинг, и элементы отсортированы по этому рейтингу.

- **ZADD** — добавить элемент с рейтингом:
  ```bash
  ZADD scores 100 "Akrom"
  ZADD scores 200 "Rustamov"
  ```
- **ZRANGE** — получить элементы в диапазоне по их индексу:
  ```bash
  ZRANGE scores 0 -1  # Выведет: ["Akrom", "Rustamov"]
  ```

## Настройка конфигурации Redis

Конфигурационный файл Redis находится по пути `/etc/redis/redis.conf`. Вот некоторые важные параметры:

- **bind** — указывает IP-адрес, на котором Redis будет принимать соединения (по умолчанию 127.0.0.1).
  ```bash
  bind 127.0.0.1
  ```
- **port** — порт, который использует Redis (по умолчанию 6379).
  ```bash
  port 6379
  ```
- **maxmemory** — задает максимальный объем памяти, который может использовать Redis:
  ```bash
  maxmemory 256mb
  ```

## Устойчивость данных в Redis

Несмотря на то, что Redis хранит данные в оперативной памяти, он поддерживает несколько механизмов для сохранения данных на диск:

1. **RDB (Redis Database Backup)** — снимок базы данных через определенные интервалы времени. Настраивается в `redis.conf`:
   ```bash
   save 900 1   # Сохранить если одна операция выполнена за 900 секунд
   save 300 10  # Сохранить если 10 операций выполнено за 300 секунд
   save 60 10000  # Сохранить если 10000 операций выполнено за 60 секунд
   ```

2. **AOF (Append Only File)** — метод, при котором все команды, изменяющие данные, записываются в файл:
   ```bash
   appendonly yes
   ```

## Использование Redis в Python

### Установка библиотеки `redis-py`:
Для работы с Redis в Python используется библиотека `redis-py`. Установить её можно так:
```bash
pip install redis
```

### Пример использования:
```python
import redis

# Подключение к Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Установка значения
r.set('username', 'Akrom')

# Получение значения
username = r.get('username')
print(username.decode())  # Выведет: Akrom
```

### Работа с другими типами данных:
```python
# Работа с хэшами
r.hset('user:1', 'name', 'Akrom')
r.hset('user:1', 'age', 18)

# Получение хэша
name = r.hget('user:1', 'name')
print(name.decode())  # Выведет: Akrom
```

## Pub/Sub в Redis

Redis поддерживает механизм **Pub/Sub (Publish/Subscribe)**, который позволяет создавать системы обмена сообщениями в реальном времени.

### Пример:
```python
import redis

r = redis.StrictRedis()

# Подписка на канал
pubsub = r.pubsub()
pubsub.subscribe('mychannel')

# Отправка сообщения в канал
r.publish('mychannel', 'Hello, Redis!')
```

Подписчик будет получать сообщения из канала в реальном времени.

## Заключение

Redis — это мощный инструмент для высокоскоростной работы с данными. Его использование позволяет значительно ускорить приложения, которые требуют быстрого доступа к данным, таких как веб-сайты с высокой нагрузкой, системы реального времени и кэширование.

Redis гибок, поддерживает множество типов данных и сценариев использования, что делает его популярным выбором для разработчиков.
