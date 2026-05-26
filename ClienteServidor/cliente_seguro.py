import socket

HOST = '68.211.177.238'
PORT = 5000

senha = input("Digite a senha de acesso: ")
mensagem = input("Digite a mensagem: ")

dados = senha + "|" + mensagem

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(dados.encode())

resposta = client.recv(1024)
print("Resposta do servidor:", resposta.decode())

client.close()
