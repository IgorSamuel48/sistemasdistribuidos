import socket

HOST = '0.0.0.0'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Servidor aguardando conexao na porta 5000...")

conn, addr = server.accept()
print(f"Conexao recebida de {addr}")

data = conn.recv(1024)

if data:
    mensagem = data.decode()
    print("Mensagem recebida:", mensagem)
    resposta = "Mensagem recebida com sucesso pelo servidor"
    conn.sendall(resposta.encode())

conn.close()
server.close()
