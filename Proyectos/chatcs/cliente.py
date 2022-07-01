import socket
host = "LocalHost"
port = 5656
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("se inicia cliente")

while True:
    enviar = input("Cliente: ")
    s.send(enviar.encode(encoding="ascii", errors="ignore"))
    recibido = s.recv(1024)
    print ("servidor", recibido.decode(encoding="ascii", errors="ignore"))
s.close()
