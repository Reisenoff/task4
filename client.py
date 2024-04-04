import socket

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Соединение с сервером {host}:{port}")

    while True:
        message = input("Введите сообщение (для выхода введите 'exit'): ")
        if message == 'exit':
            break

        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print("Получено от сервера:", data.decode())

    print("Разрыв соединения с сервером")
    client_socket.close()

if __name__ == "__main__":
    host = input("Введите имя хоста (пустая строка для использования localhost): ") or 'localhost'
    port = int(input("Введите номер порта: "))
    start_client(host, port)