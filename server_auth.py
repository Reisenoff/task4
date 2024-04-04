import socket
import threading
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# База данных пользователей (для учебных целей)
user_database = {
    "user1": hash_password("123"),
    "user2": hash_password("1234")
}

def authenticate_user(username, password):
    hashed_password = user_database.get(username)
    if hashed_password and hashed_password == hash_password(password):
        return True
    return False

def start_authentication_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер аутентификации запущен. Ожидание подключений на {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключение клиента {client_address}")

        # Принятие данных от клиента
        username = client_socket.recv(1024).decode()
        password = client_socket.recv(1024).decode()

        if authenticate_user(username, password):
            client_socket.sendall(b"SUCCESS")
            print(f"Пользователь {username} успешно аутентифицирован.")
        else:
            client_socket.sendall(b"FAILURE")
            print(f"Неверные учетные данные для пользователя {username}.")

        client_socket.close()

# Запуск сервера аутентификации
if __name__ == "__main__":
    auth_host = input("Введите имя хоста для сервера аутентификации (пустая строка для использования localhost): ") or 'localhost'
    auth_port = int(input("Введите номер порта для сервера аутентификации: "))
    start_authentication_server(auth_host, auth_port)