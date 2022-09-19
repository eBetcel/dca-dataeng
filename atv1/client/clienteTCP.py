# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
#
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#

# importacao das bibliotecas
from socket import *
import sys

# EXECUTAR: python cliente.py IP

# definicao das variaveis
serverName = str(sys.argv[1]) # ip do servidor
serverPort = 30000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

print ('Cliente em execucao...\nEnviando mensagem para o servidor')
sentence = 'O meu hostname e ' + gethostname()
clientSocket.send(sentence.encode('utf-8')) # envia o texto para o servidor
clientSocket.close() # encerramento o socket do cliente
