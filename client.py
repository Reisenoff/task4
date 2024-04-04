import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)
    client_socket.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер запущен. Ожидание подключений на {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключение клиента {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    host = input("Введите имя хоста (пустая строка для использования localhost): ") or 'localhost'
    port = int(input("Введите номер порта: ") or '12345')
    start_server(host, port)
