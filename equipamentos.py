
import json
import buscas
from datetime import date
from pathlib import Path

CAMINHO_JSON = Path(__file__).resolve().parent / "dados" / "equipamentos.json"


def carregar_equipamentos():
    with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_equipamentos(equipamentos):
    with open(CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(equipamentos, arquivo, ensure_ascii=False, indent=4)


def gerar_codigo(equipamentos):
    if not equipamentos:
        return 1001

    maior_codigo = max(
        equipamento["codigo"] for equipamento in equipamentos
    )
    return maior_codigo + 1


def criar_equipamento(equipamentos):
    novo_codigo = gerar_codigo(equipamentos)

    print("\n========== CADASTRAR EQUIPAMENTO ==========")

    nome = input("Nome do novo equipamento: ").strip()
    marca = input("Marca do novo equipamento: ").strip()
    condicao = input("Condição do equipamento: ").strip()

    if not nome or not marca or not condicao:
        print("Cadastro cancelado. Preencha todos os campos.")
        return None

    while True:
        try:
            peso = float(
                input("Peso do equipamento (em kg): ").replace(",", ".")
            )

            if peso <= 0:
                print("O peso precisa ser maior que zero.")
                continue

            break

        except ValueError:
            print("Peso inválido. Digite um número.")

    equipamento = {
        "codigo": novo_codigo,
        "equipamento": nome,
        "marca": marca,
        "condicao": condicao,
        "peso": peso,
        "data_entrada": date.today().isoformat(),
        "status": "aguardando_avaliacao",
        "destinacao": "nao_definida"
    }

    print("\n========== CONFIRMAR CADASTRO ==========")
    print("Código:", equipamento["codigo"])
    print("Equipamento:", equipamento["equipamento"])
    print("Marca:", equipamento["marca"])
    print("Condição:", equipamento["condicao"])
    print("Peso:", equipamento["peso"], "kg")
    print("Data:", equipamento["data_entrada"])
    print("Status:", equipamento["status"])
    print("Destinação:", equipamento["destinacao"])

    confirmar = input("\nConfirmar cadastro? (S/N): ").strip().lower()

    if confirmar != "s":
        print("Cadastro cancelado.")
        return None

    equipamentos.append(equipamento)

    try:
        salvar_equipamentos(equipamentos)

    except OSError as erro:
        equipamentos.pop()
        print("Erro ao salvar equipamento:", erro)
        return None

    print("\nEquipamento cadastrado com sucesso!")
    print("Código gerado:", novo_codigo)

    return equipamento


if __name__ == "__main__":
    equipamentos = carregar_equipamentos()

    print("Total de equipamentos:", len(equipamentos))
    print("Próximo código disponível:", gerar_codigo(equipamentos))

    criar_equipamento(equipamentos)

def atualizar_equipamento(equipamentos, codigo):
    equipamento = buscas.buscar_equipamento(equipamentos, codigo)

    if equipamento is None:
        print("Equipamento não encontrado.")
        return

    print("\n========== ATUALIZAR EQUIPAMENTO ==========")
    print("Código:", equipamento["codigo"])
    print("Equipamento:", equipamento["equipamento"])
    print("Marca:", equipamento["marca"])
    print("Condição:", equipamento["condicao"])
    print("Peso:", equipamento["peso"], "kg")
    print("Data de entrada:", equipamento["data_entrada"])
    print("Status:", equipamento["status"])
    print("Destinação:", equipamento["destinacao"])

    nome = input("\nNovo nome (Enter para manter): ").strip()
    marca = input("Nova marca (Enter para manter): ").strip()
    condicao = input("Nova condição (Enter para manter): ").strip()
    peso_original = equipamento["peso"]

    # Validação do peso
    while True:
        peso_input = input("Novo peso em kg (Enter para manter): ").strip()

        if not peso_input:
            break

        try:
            peso = float(peso_input.replace(",", "."))

            if peso <= 0:
                print("O peso deve ser maior que zero.")
                continue

            equipamento["peso"] = peso
            break

        except ValueError:
            print("Peso inválido. Digite um número.")

    confirmar = input("Confirmar atualização cadastral? (S/N): ").strip().lower()
    if confirmar != "s":
        equipamento["peso"] = peso_original
        print("Alteração cancelada.")
        return

    if nome:
        equipamento["equipamento"] = nome
    if marca:
        equipamento["marca"] = marca
    if condicao:
        equipamento["condicao"] = condicao

    salvar_equipamentos(equipamentos)

    print("\nDados cadastrais atualizados com sucesso!")
    

def atualizar_status(equipamentos, codigo):
    equipamento = buscas.buscar_equipamento(equipamentos, codigo)

    if equipamento is None:
        print("Equipamento não encontrado.")
        return

    print("\n========== ATUALIZAR STATUS ==========")
    print("Código:", equipamento["codigo"])
    print("Status atual:", equipamento["status"])
    print("Destinação:", equipamento["destinacao"])

    print("\n1 - Aguardando avaliação")
    print("2 - Em avaliação")
    print("3 - Aguardando destinação")
    print("4 - Finalizado")
    print("5 - Outro (especificar)")
    print("0 - Manter status atual")

    opcao = input("\nEscolha o novo status: ").strip()

    if opcao == "1":
        novo_status = "aguardando_avaliacao"

    elif opcao == "2":
        novo_status = "em_avaliacao"

    elif opcao == "3":
        novo_status = "aguardando_destinacao"

    elif opcao == "4":
        novo_status = "finalizado"

    elif opcao == "5":
        novo_status = input("Especifique o status: ").strip()

        if not novo_status:
            print("O status não pode ficar vazio.")
            return

    elif opcao == "0":
        print("Status mantido.")
        return

    else:
        print("Opção inválida.")
        return

    if novo_status == "finalizado" and equipamento["destinacao"] == "nao_definida":
        print("Não é possível finalizar sem uma destinação definida.")
        return

    confirmar = input(
        f"Confirmar status '{novo_status}'? (S/N): "
    ).strip().lower()
    if confirmar != "s":
        print("Alteração cancelada.")
        return

    equipamento["status"] = novo_status
    salvar_equipamentos(equipamentos)
    print("Status atualizado para:", novo_status)


def atualizar_destinacao(equipamentos, codigo):
    equipamento = buscas.buscar_equipamento(equipamentos, codigo)

    if equipamento is None:
        print("Equipamento não encontrado.")
        return

    print("\n========== REGISTRAR DESTINAÇÃO ==========")
    print("Código:", equipamento["codigo"])
    print("Destinação atual:", equipamento["destinacao"])
    print("\n1 - Reciclagem")
    print("2 - Reutilização")
    print("3 - Tratamento especializado")
    print("4 - Outro (especificar)")
    print("0 - Manter destinação atual")

    opcao = input("\nEscolha a destinação: ").strip()
    destinos = {
        "1": "reciclagem",
        "2": "reutilizacao",
        "3": "tratamento_especializado",
    }

    if opcao == "0":
        print("Destinação mantida.")
        return
    if opcao == "4":
        nova_destinacao = input("Especifique a destinação: ").strip()
        if not nova_destinacao:
            print("A destinação não pode ficar vazia.")
            return
    elif opcao in destinos:
        nova_destinacao = destinos[opcao]
    else:
        print("Opção inválida.")
        return

    confirmar = input(
        f"Confirmar destinação '{nova_destinacao}'? (S/N): "
    ).strip().lower()
    if confirmar != "s":
        print("Alteração cancelada.")
        return

    equipamento["destinacao"] = nova_destinacao
    salvar_equipamentos(equipamentos)
    print("Destinação registrada com sucesso!")
