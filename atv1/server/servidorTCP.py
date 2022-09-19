# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# 
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 30000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
serverIP=gethostbyname(gethostname())
print ('Servidor iniciado em %s:%d ...' % (serverIP,serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  sentence = sentence.decode('utf-8')
  print ('Cliente %s enviou: %s' % (addr, sentence))
  connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor