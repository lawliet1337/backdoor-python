import socket

HOST = "127.0.0.1"
PORTA = 1337
servidor = socket.socket()
servidor.bind((HOST,PORTA))
print("[+] servidor inicializado...")
print("[+] esperando por conexoes...")
servidor.listen(1)
cliente, end_client = servidor.accept()
print(f'[+]{end_client} Cliente conectado ao servidor')

while True:
    comando = input("Digite um comando: ")
    comando = comando.encode()
    cliente.send(comando)
    print("[+] comando enviado.")
    saida = cliente.recv(1024)
    saida = saida.decode()
    print(f"saida: {saida}")
