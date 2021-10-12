import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!")
        print(f'Erro: {e}')
        sys.exit()
    print("Socket criado com sucesso!")

    host_alvo = input('Digite o host ou IP a ser conectado: ')
    porta_alvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((host_alvo, int(porta_alvo)))
        print(f'Cliente TCP conectado com sucesso no host: {host_alvo} e na porta: {porta_alvo}')
        s.shutdown(2)
    except socket.error as e:
        print(f'A conexão falhou, erro: {e}')
        sys.exit()


if __name__ == "__main__":
    main()
