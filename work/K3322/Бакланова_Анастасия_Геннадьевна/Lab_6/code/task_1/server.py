import socket

def run_server():
    # Создаем TCP/IP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Привязываем сокет к порту
    server_address = ('localhost', 8000)
    print(f"Starting server on {server_address[0]}:{server_address[1]}")
    server_socket.bind(server_address)
    # Слушаем входящие соединения
    server_socket.listen(1)

    while True:
        print("Waiting for a connection...")
        # Принимаем соединение
        client_socket, client_address = server_socket.accept()
        try:
            print(f"Connection from {client_address}")
            # Получаем данные от клиента
            data = client_socket.recv(1024)
            print(f"Received: {data.decode('utf-8')}")
            # Отправляем ответ
            response = "Hello, client"
            client_socket.sendall(response.encode('utf-8'))
            print(f"Sent: {response}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    run_server()