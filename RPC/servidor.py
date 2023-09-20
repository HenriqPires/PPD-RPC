import random
from xmlrpc.server import SimpleXMLRPCServer


opcoes = ["Pedra", "Papel", "Tesoura"]

def jogar():
    escolha_servidor = random.choice(opcoes)
    return escolha_servidor

def verificar_resultado(escolha_cliente, escolha_servidor):
    if escolha_cliente == escolha_servidor:
        return "Empate"
    elif (
        (escolha_cliente == "Pedra" and escolha_servidor == "Tesoura")
        or (escolha_cliente == "Papel" and escolha_servidor == "Pedra")
        or (escolha_cliente == "Tesoura" and escolha_servidor == "Papel")
    ):
        return "Você venceu!"
    else:
        return "Servidor venceu!"

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(jogar, "jogar")
server.register_function(verificar_resultado, "verificar_resultado")

print("Servidor RPC iniciado. Aguardando conexões...")
server.serve_forever()
