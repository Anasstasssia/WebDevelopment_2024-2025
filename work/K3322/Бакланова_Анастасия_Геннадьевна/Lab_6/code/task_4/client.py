import socket
import threading

HOST = '127.0.0.1'  # Адрес сервера
PORT = 55555        # Порт сервера

# Создаем сокет клиента
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
client.connect((HOST, PORT))

# Функция для получения никнейма
def get_nickname():
    nickname = input("Введите ваш никнейм: ")
    client.send(nickname.encode('utf-8'))
    return nickname

# Функция для приема сообщений от сервера
def receive():
    while True:
        try:
            # Получаем сообщение от сервера
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Произошла ошибка!")
            client.close()
            break

# Функция для отправки сообщений на сервер
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

# Получаем никнейм
nickname = get_nickname()

# Запускаем потоки для приема и отправки сообщений
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()