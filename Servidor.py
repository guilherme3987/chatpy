import socket
import threading
import datetime

#Definição de cores para a formatação do texto:

red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m"

#Função menu
def menu():
    print(red + "--- Menu --- \n\nEntrar no chat -- 1\nSair no chat -- 0")

menu()

#Função que retorna hora
def hora():
    hora_atual = datetime.datetime.now()
    hora_formatada = hora_atual.strftime(blue + "%H:%M:%S")
    return hora_formatada

# Função para lidar com a conexão com o cliente
def lidando_cliente(cliente, address):
    while True:
        try:
            # Recebe a mensagem do cliente
            msg = cliente.recv(1024).decode()

            # Sair do chat
            if msg.strip() == '0':
                print(red, address, "Desconectou.")
                cliente.close()
                break

            print(msg, address, "  (", hora(), ")")

            # Responde ao cliente
            conversa = input("=: ")
            cliente.send(conversa.encode())
        except ConnectionResetError:
            print(red, address, "Desconectou.")
            cliente.close()
            break

# Configuração do servidor
def servidor():
    escolha = int(input(red + "->"))

    if escolha == 1:
        # Definindo porta,ip e socket
        ip = '127.0.0.1'
        porta = 3322

        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind((ip, porta))
        servidor.listen()

        print(green, "Esperando conexão...")

        # Aceita a conexão do cliente
        while True:
            
            cliente, address = servidor.accept()
            print(green, "Conexão estabelecida com ", address, hora())

            #Lidar com várias conexões
            threading.Thread(target=lidando_cliente, args=(cliente, address)).start()
    else:
        print(red, "Fim")

servidor()
