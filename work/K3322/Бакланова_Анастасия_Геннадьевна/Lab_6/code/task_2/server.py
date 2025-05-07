import socket

def calculate_parallelogram_area(base, height):
    return base * height

def start_server():
    host = 'localhost'
    port = 8001

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"Сервер запущен на {host}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Подключен клиент: {addr}")
                try:
                    data = conn.recv(1024).decode()
                    if not data:
                        continue

                    print(f"Получены данные: {data}")
                    base, height = map(float, data.split(','))
                    area = calculate_parallelogram_area(base, height)
                    conn.sendall(str(area).encode())
                except ValueError:
                    conn.sendall("Ошибка: неверные параметры")
                except Exception as e:
                    conn.sendall(f"Ошибка: {str(e)}".encode())

if __name__ == "__main__":
    start_server()

