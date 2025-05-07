import socket
import threading

HOST = '127.0.0.1'  # Локальный адрес
PORT = 55555        # Порт для подключения клиентов

# Список подключенных клиентов и их ников
clients = []
nicknames = []

# Создаем сокет сервера
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Сервер запущен на {HOST}:{PORT}")

# Функция для трансляции сообщений всем клиентам
def broadcast(message, sender=None):
    for client in clients:
        if client != sender:  # Не отправляем сообщение отправителю
            try:
                client.send(message)
            except:
                # Если отправка не удалась, удаляем клиента
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f'{nickname} покинул чат!'.encode('utf-8'))
                nicknames.remove(nickname)

# Обработка подключений клиентов
def handle_client(client):
    while True:
        try:
            # Получаем сообщение от клиента
            message = client.recv(1024)
            if message:
                broadcast(message, sender=client)
            else:
                # Если сообщение пустое, клиент отключился
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f'{nickname} покинул чат!'.encode('utf-8'))
                nicknames.remove(nickname)
                break
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} покинул чат!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# Основная функция для принятия подключений
def receive():
    while True:
        # Принимаем новое подключение
        client, address = server.accept()
        print(f"Подключен клиент с адресом {str(address)}")

        # Запрашиваем и сохраняем ник клиента
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        # Уведомляем чат о новом участнике
        print(f"Ник клиента: {nickname}")
        broadcast(f"{nickname} присоединился к чату!".encode('utf-8'))
        client.send('Подключение к серверу успешно!'.encode('utf-8'))

        # Запускаем поток для обработки сообщений клиента
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == '__main__':
    receive()