import socket
import datetime

red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m" 


def hora():
    hora_atual = datetime.datetime.now()
    hora_formatada = hora_atual.strftime(blue+"%H:%M:%S")
    return hora_formatada

# Ip e porta do socket

ip = '127.0.0.1'
porta = 3322

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ip, porta))

while True:
    # Começar conversa
    conversa = input(red+"=: ")
    cliente.send(conversa.encode())

    # Verifica se o usuário deseja sair
    if conversa.strip() == '0':
        print(red+"Desconectado.")
        cliente.close()
        break

    # Recebe a resposta do servidor
    resposta_conversa = cliente.recv(1024).decode()
    print(blue,resposta_conversa,"  (",hora(),")")

