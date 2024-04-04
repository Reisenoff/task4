import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            break

def send_messages(client_socket):
    while True:
        try:
            message = input()
            client_socket.sendall(message.encode())
        except:
            break

def start_chat_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Соединение с сервером успешно установлено.")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

if __name__ == "__main__":
    auth_host = 'localhost'
    auth_port = 9000
    chat_host = 'localhost'
    chat_port = 9001
    start_chat_client(auth_host, auth_port)