from collections import Counter


def exibir_relatorios(equipamentos):
    """Exibe um resumo dos equipamentos cadastrados."""
    total = len(equipamentos)
    peso_total = sum(float(item.get("peso", 0)) for item in equipamentos)
    status = Counter(item.get("status", "nao_informado") for item in equipamentos)
    destinacoes = Counter(
        item.get("destinacao", "nao_definida") for item in equipamentos
    )

    print("\n========== RELATÓRIOS ==========")
    print("Total de equipamentos:", total)
    print(f"Peso total cadastrado: {peso_total:.2f} kg")

    print("\nEquipamentos por status:")
    for nome, quantidade in sorted(status.items()):
        print(f"- {nome}: {quantidade}")

    print("\nEquipamentos por destinação:")
    for nome, quantidade in sorted(destinacoes.items()):
        print(f"- {nome}: {quantidade}")
