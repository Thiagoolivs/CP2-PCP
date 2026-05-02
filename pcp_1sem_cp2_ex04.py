def calcular_horas_extras(salario_base, horas):
    """
    Calcula o valor das horas extras.
    Taxa: 1.5% do salário base por hora extra
    """
    valor_hora = salario_base * 0.015
    return valor_hora * horas


def calcular_descontos_faltas(salario_base, faltas):
    """
    Calcula o desconto por faltas.
    Taxa: 2% do salário base por falta
    """
    desconto_por_falta = salario_base * 0.02
    return desconto_por_falta * faltas


def calcular_bonus(cargo, recebeu_bonus):
    """
    Calcula o bônus por desempenho baseado no cargo.
    Gerente (1): R$ 1000
    Analista (2): R$ 500
    Assistente (3): R$ 300
    Estagiário (4): R$ 100
    """
    if not recebeu_bonus.lower() == 's':
        return 0

    bonus_valores = {
        1: 1000,
        2: 500,
        3: 300,
        4: 100
    }

    return bonus_valores.get(cargo, 0)


def main():
    print("=" * 50)
    print("SISTEMA DE RH - CÁLCULO DE SALÁRIO")
    print("=" * 50)

    # Entrada de dados
    nome_funcionario = input("\nNome do funcionário: ")

    print("\nCargo:")
    print("1 - Gerente")
    print("2 - Analista")
    print("3 - Assistente")
    print("4 - Estagiário")
    cargo = int(input("Digite o código do cargo: "))

    salario_base = float(input("Salário base (R$): "))
    horas_extras = float(input("Total de horas extras trabalhadas: "))
    faltas = int(input("Total de faltas no mês: "))

    print("\nRecebeu bônus por desempenho?")
    recebeu_bonus = input("Digite 's' para sim ou 'n' para não: ")

    # Cálculos
    valor_horas_extras = calcular_horas_extras(salario_base, horas_extras)
    desconto_faltas = calcular_descontos_faltas(salario_base, faltas)
    valor_bonus = calcular_bonus(cargo, recebeu_bonus)

    # Salário final
    salario_bruto = salario_base
    total_acrescimos = valor_horas_extras + valor_bonus
    total_descontos = desconto_faltas
    salario_final = salario_bruto + total_acrescimos - total_descontos

    # Exibição dos resultados
    print("\n" + "=" * 50)
    print("RESULTADO DO CÁLCULO DE SALÁRIO")
    print("=" * 50)
    print(f"\nNome do funcionário: {nome_funcionario}")
    print(f"Salário bruto: R$ {salario_bruto:.2f}")
    print(f"Horas extras: R$ {valor_horas_extras:.2f}")
    print(f"Bônus: R$ {valor_bonus:.2f}")
    print(f"Total de acréscimos: R$ {total_acrescimos:.2f}")
    print(f"Desconto por faltas: R$ {total_descontos:.2f}")
    print(f"Total de descontos: R$ {total_descontos:.2f}")
    print(f"\nSalário final: R$ {salario_final:.2f}")
    print("=" * 50)


if __name__ == "__main__":
    main()





