import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6060))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(f"Conexão estabelecida no endereço: {address}")
    clientSocket.send(bytes("Welcome to the Server!!!", "utf-8"))
    clientSocket.close()