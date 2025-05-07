import socket

def load_html_file(filename):
    """Загружает содержимое HTML-файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "<h1>Error: File not found</h1>"


def create_http_response(html_content):
    """Формирует полный HTTP-ответ"""
    response = f"HTTP/1.1 200 OK\r\n"
    response += f"Content-Type: text/html; charset=utf-8\r\n"
    response += f"Content-Length: {len(html_content)}\r\n"
    response += "\r\n"  # Пустая строка - разделитель заголовков и тела
    response += html_content
    return response.encode('utf-8')


def run_server(host='localhost', port=8080):
    """Запускает HTTP-сервер"""
    html_content = load_html_file('index.html')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server running on http://{host}:{port}")

        while True:
            client_conn, client_addr = server_socket.accept()
            print(f"Connection from {client_addr}")

            try:
                request = client_conn.recv(1024).decode('utf-8')
                print(f"Received request:\n{request}")

                # Отправляем HTTP-ответ с HTML-страницей
                http_response = create_http_response(html_content)
                client_conn.sendall(http_response)
            finally:
                client_conn.close()


if __name__ == "__main__":
    run_server()