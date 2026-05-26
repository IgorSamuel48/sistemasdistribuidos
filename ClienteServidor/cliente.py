import socket

HOST = '68.211.177.238'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

mensagem = "Ola servidor, esta e uma mensagem do cliente"
client.sendall(mensagem.encode())

data = client.recv(1024)
print("Resposta do servidor:", data.decode())

client.close()
