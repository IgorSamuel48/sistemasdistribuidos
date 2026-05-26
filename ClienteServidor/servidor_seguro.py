import socket

HOST = '0.0.0.0'
PORT = 5000
SENHA_CORRETA = "fatec123"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Servidor seguro aguardando conexões na porta 5000...")

conn, addr = server.accept()
print(f"Conexão recebida de {addr}")

dados = conn.recv(1024).decode()

partes = dados.split("|")

if len(partes) == 2:
    senha = partes[0]
    mensagem = partes[1]

    if senha == SENHA_CORRETA:
        print("Cliente autenticado.")
        print("Mensagem recebida:", mensagem)
        resposta = "Acesso autorizado. Mensagem recebida com sucesso."
    else:
        print("Tentativa de acesso negada.")
        resposta = "Acesso negado. Senha incorreta."
else:
    resposta = "Formato inválido."

conn.sendall(resposta.encode())

conn.close()
server.close()
