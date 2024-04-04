import socket
import threading

def broadcast_message(message, sender_socket, clients):
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message)
            except:
                clients.remove(client)

def handle_client(client_socket, clients):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast_message(message, client_socket, clients)
        except:
            break
    client_socket.close()

def start_chat_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер чата запущен. Ожидание подключений на {host}:{port}")

    clients = []

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключение клиента {client_address}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, clients))
        client_thread.start()

# Запуск сервера чата
if __name__ == "__main__":
    chat_host = 'localhost'
    chat_port = 9001
    start_chat_server(chat_host, chat_port)