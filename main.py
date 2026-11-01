import buscas
import equipamentos
import relatorios
from equipamentos import carregar_equipamentos

opcao = ""

while opcao != "0":

    print("\n===================================================")
    print("                    ECOTECH")
    print(" Sistema de Gerenciamento de Resíduos Eletrônicos")
    print("===================================================")

    print("\nPor favor, selecione uma das opções abaixo:")
    print("1 - Cadastrar Equipamento")
    print("2 - Listar Equipamentos cadastrados")
    print("3 - Pesquisar Equipamentos cadastrados")
    print("4 - Atualizar Equipamentos cadastrados")
    print("5 - Atualizar Status")
    print("6 - Registrar Destinação")
    print("7 - Visualizar Relatórios")
    print("0 - Sair do sistema")

    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == "1":
        print("Você selecionou a opção de cadastrar equipamento.")
        
        while True:
            cadastrar = input("Deseja cadastrar um novo equipamento? (s/n): ").lower()

            if cadastrar == "s":
                from equipamentos import criar_equipamento
                criar_equipamento(buscas.equipamentos)

            elif cadastrar == "n":
                print("Voltando ao menu principal...")
                break

            else:
                print("Opção inválida. Digite 's' para sim ou 'n' para não.")

    elif opcao == "2":
        print("Você selecionou a opção de listar equipamentos cadastrados.")
        
        lista = carregar_equipamentos()
        for equipamento in lista:
            print("----------------------------------------")
            print("Código:", equipamento["codigo"])
            print("Equipamento:", equipamento["equipamento"])
            print("Marca:", equipamento["marca"])
            print("Condição:", equipamento["condicao"])
            print("Peso:", equipamento["peso"], "kg")
            print("Data de entrada:", equipamento["data_entrada"])
            print("Status:", equipamento["status"])
            print("Destinação:", equipamento["destinacao"])

        print("----------------------------------------")
        print("Total de equipamentos:", len(lista))
        
    elif opcao == "3":
        print("\n========== PESQUISAR EQUIPAMENTOS ==========")

        while True:
            entrada = input("\nDigite o código do equipamento ou 0 para voltar: ")

            if entrada == "0":
                print("\nVoltando ao menu principal...")
                break

            try:
                codigo = int(entrada)
            except ValueError:
                print("Código inválido. Digite apenas números.")
                continue

            resultado = buscas.buscar_equipamento(buscas.equipamentos, codigo)

            if resultado is not None:
                print("\n========== EQUIPAMENTO ENCONTRADO ==========")
                print("Código:", resultado["codigo"])
                print("Dispositivo:", resultado["equipamento"], "da marca:", resultado["marca"])
                print("A condição atual é", resultado["condicao"], "e, o destino atual é", resultado["destinacao"])
                print("===========================================")
            else:
                print("Equipamento não encontrado.")


    elif opcao == "4":
        print("Você selecionou a opção de atualizar equipamentos cadastrados.")

        while True:
            entrada = input("\nDigite o código do equipamento que deseja atualizar ou 0 para voltar: ")

            if entrada == "0":
                print("\nVoltando ao menu principal...")
                break

            try:
                codigo = int(entrada)
            except ValueError:
                print("Código inválido. Digite apenas números.")
                continue

            equipamentos.atualizar_equipamento(buscas.equipamentos, codigo)
            
    elif opcao == "5":
        print("Você selecionou a opção de atualizar status.")

        while True:
            entrada = input(
                "\nDigite o código do equipamento ou 0 para voltar: "
            ).strip()
            if entrada == "0":
                break
            try:
                codigo = int(entrada)
            except ValueError:
                print("Código inválido. Digite apenas números.")
                continue
            equipamentos.atualizar_status(buscas.equipamentos, codigo)

    elif opcao == "6":
        print("Você selecionou a opção de registrar destinação.")

        while True:
            entrada = input(
                "\nDigite o código do equipamento ou 0 para voltar: "
            ).strip()
            if entrada == "0":
                break
            try:
                codigo = int(entrada)
            except ValueError:
                print("Código inválido. Digite apenas números.")
                continue
            equipamentos.atualizar_destinacao(buscas.equipamentos, codigo)

    elif opcao == "7":
        print("Você selecionou a opção de visualizar relatórios.")
        relatorios.exibir_relatorios(carregar_equipamentos())

    elif opcao == "0":
        print("Saindo do sistema. Até logo!")

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
