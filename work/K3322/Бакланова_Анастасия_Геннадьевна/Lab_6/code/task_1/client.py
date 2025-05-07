import socket

def run_client():
    # Создаем TCP/IP сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Подключаемся к серверу
    server_address = ('localhost', 8000)
    print(f"Connecting to {server_address[0]}:{server_address[1]}")
    client_socket.connect(server_address)
    try:
        # Отправляем данные
        message = "Hello, server"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")
        # Получаем ответ
        data = client_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_client()