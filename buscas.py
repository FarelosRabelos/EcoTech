
import json

with open("dados/equipamentos.json", "r", encoding="utf-8") as arquivo:
    equipamentos = json.load(arquivo)

print("Total de equipamentos:", len(equipamentos))

def buscar_equipamento(equipamentos, codigo):
    for equipamento in equipamentos:
        if equipamento["codigo"] == codigo:
            return equipamento

    return None

if __name__ == "__main__":
    
    while True:
        entrada = input("\nDigite o código do equipamento ou 0 para sair: ")

        if entrada == "0":
            print("Encerrando pesquisa.")
            break

        try:
            codigo = int(entrada)
        except ValueError:
            print("Código inválido. Digite apenas números.")
            continue

        resultado = buscar_equipamento(equipamentos, codigo)

        if resultado is not None:
            print("\nEquipamento encontrado!")
            print("Código:", resultado["codigo"])
            print("Dispositivo:", resultado["equipamento"], "da marca:", resultado["marca"])
            print("A condição atual é", resultado["condicao"], "e, o destino atual é", resultado["destinacao"])
        else:
            print("Equipamento não encontrado.")
