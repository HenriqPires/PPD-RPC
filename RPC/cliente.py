import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

def jogar_jogo():
    print("\tBEM-VINDO AO JOGO\n ----- Pedra, Papel e Tesoura -----")
    
    while True:
        escolha_cliente = input("Escolha Pedra, Papel ou Tesoura: ")
        
       
        if escolha_cliente not in ["Pedra", "Papel", "Tesoura"]:
            print("Escolha inválida. Por favor, escolha Pedra, Papel ou Tesoura.")
            continue  
       
        escolha_servidor = proxy.jogar()

        print(f"Você escolheu: {escolha_cliente}")
        print(f"Servidor escolheu: {escolha_servidor}")

        resultado = proxy.verificar_resultado(escolha_cliente, escolha_servidor)
        print(f"Resultado: {resultado}")
        
       
        jogar_novamente = input("Deseja jogar novamente? (Sim/Não): ")
        if jogar_novamente.lower() != "sim":
            break  

if __name__ == "__main__":
    jogar_jogo()
