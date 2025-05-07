import socket

def get_user_input():
    while True:
        try:
            base = float(input("Введите длину основания параллелограмма: "))
            height = float(input("Введите высоту параллелограмма: "))
            return base, height
        except ValueError:
            print("Ошибка: введите числовые значения")

def start_client():
    host = 'localhost'
    port = 8001

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Подключено к серверу {host}:{port}")

        base, height = get_user_input()
        data = f"{base},{height}"
        s.sendall(data.encode())

        response = s.recv(1024).decode()
        print(f"Площадь параллелограмма: {response}")

if __name__ == "__main__":
    start_client()



