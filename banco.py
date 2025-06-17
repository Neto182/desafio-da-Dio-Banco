#AmBank
# AmBank é um banco fictício para por minhas habilidades da primeira parte do curso de python aqui na DIO
# Am de Amazonas de onde sou e Bank de banco kkk


#começarei definindo as variáveis extrato e saldo
extrato = ""
saldo = 0

#com a ideia q de que todo caixa eletronico após uma operação ele tem...
# um menu pra onde retorna decidi fazer um loop com while 

while True:
    print("Menu")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Sair")

    # pergunto a opção aqui
    opcao = input("escolha sua opção: ")
    
    # se for 1 de deposito
    if opcao == "1":
        # Peço o valor que o usuário deseja depositar
        valor = float(input("Informe o valor do depósito: "))
        
        # Verifico se o valor é válido (positivo)
        if valor > 0:
            saldo += valor   # Adiciono o valor ao saldo
            extrato += f"Depósito: +R$ {valor:.2f}\n"  # Registro no extrato
            print("Depósito realizado com sucesso.")
        else:
            # Se o valor for inválido (negativo ou zero), informo ao usuário
            print("Valor inválido. Tente novamente.")

    # Se a opção for saque
    elif opcao == "2":
        # Peço o valor do saque
        valor = float(input("Informe o valor do saque: "))

        # Verifico se o valor é válido
        if valor <= 0:
            print("Valor inválido.")
        elif valor > saldo:
            # Se o valor for maior que o saldo, o saque não pode ser realizado
            print("Saldo insuficiente.")
        else:
            saldo -= valor    # Desconto o valor do saldo
            extrato += f"Saque: -R$ {valor:.2f}\n"  # Registro no extrato
            print("Saque realizado com sucesso.")

    # Se a opção for 3 de extrato
     
    elif opcao == "3":
        # Mostro o extrato com as movimentações realizadas e o saldo atual
        print("\n========== EXTRATO ==========")
        # Se não houver movimentações, aviso isso
        print("Nenhuma movimentação." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==============================")

    # Se a opção for 4 de sair
    elif opcao == "4":
        # Saio do loop e finalizo o programa
        print("Saindo... Obrigado por utilizar o AmBank")
        break

    # caso o usuario coloque algo diferente
    else:
        print("Opção inválida, tente novamente.")
