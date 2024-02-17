import socket

HOST = 'localhost'
PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()
print('Aguardando conexão com cliente')
conn, ender = sock.accept()
print('Conectando em', ender)
while True:
    data = conn.recv(1024)
    if not data:
        print('Fechar conexão, sem dados')
        conn.closed()
        break
    conn.sendall(data)