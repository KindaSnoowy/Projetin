import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6060))
s.listen()
print("Aguardando conexão!")


clientSocket, address = s.accept()
print(f"Conexão estabelecida no endereço: {address}")

while True:
    data = clientSocket.recv(2064)
    if not data:
        print("fechando conexão")
        clientSocket.close()
        break
    clientSocket.sendall(data)