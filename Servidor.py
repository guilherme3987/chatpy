import socket
import datetime

red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m" 


def menu():
    print(red+"--- Menu --- \n\nEntrar no chat -- 1\nSair no chat -- 0")

menu()

def hora():
    hora_atual = datetime.datetime.now()
    hora_formatada = hora_atual.strftime(blue+"%H:%M:%S")
    return hora_formatada

def servidor():
    escolha = int(input(red+"->"))

    if escolha == 1 :

        # Definindo porta e ip para conexão
        ip = '127.0.0.1'
        porta = 3322

        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind((ip, porta))
        servidor.listen( )

        print(green,"Esperando conexão...")

        while True:
            # Aceita a conexão do cliente
            cliente, address = servidor.accept()
            print(green,"Conexão estabelecida com ",address,hora())

            while True:
                # Recebe a mensagem do cliente
                msg = cliente.recv(1024).decode()

                # Sair do chat
                if msg.strip() == '0':
                    print(red,address,"Desconectou.")
                    cliente.close()
                    break

                print(msg,address,"  (",hora(),")")

                # Responde ao cliente
                conversa = input("=: ")
                cliente.send(conversa.encode())


    else: print(red,"Fim")



servidor()




