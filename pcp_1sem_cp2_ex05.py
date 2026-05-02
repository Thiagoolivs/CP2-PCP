def pode_aprovar(idade, renda, valor):
    """
    Verifica se o cliente pode ser aprovado para o financiamento.
    Critérios:
    - Ter mais de 18 anos
    - Valor do financiamento <= 20 vezes a renda mensal
    """
    if idade <= 18:
        return False

    if valor > (renda * 20):
        return False

    return True


def definir_taxa(parcelas):
    """
    Define a taxa de juros baseada no número de parcelas.
    até 6 parcelas → 5% ao mês
    de 7 até 12 parcelas → 8% ao mês
    de 13 até 24 parcelas → 10% ao mês
    """
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:  # 13 até 24
        return 0.10


def calcular_parcela(valor, taxa, parcelas):
    """
    Calcula o valor da parcela usando a fórmula de Tabela Price.
    PMT = PV * (i(1+i)^n) / ((1+i)^n - 1)
    onde:
    PMT = valor da parcela
    PV = valor financiado
    i = taxa de juros (em decimal)
    n = número de parcelas
    """
    # Cálculo do numerador: i(1+i)^n
    numerador = taxa * ((1 + taxa) ** parcelas)

    # Cálculo do denominador: (1+i)^n - 1
    denominador = ((1 + taxa) ** parcelas) - 1

    # Fórmula da parcela
    pmt = valor * (numerador / denominador)

    return pmt


def calcular_total(parcela, parcelas):
    """
    Calcula o valor total pago.
    total = PMT * n
    """
    return parcela * parcelas


def calcular_juros(total, valor):
    """
    Calcula o total de juros pagos.
    juros = total - PV
    """
    return total - valor


def main():
    print("=" * 60)
    print("SISTEMA DE FINANCIAMENTO BANCÁRIO")
    print("=" * 60)

    # Entrada de dados
    nome_cliente = input("\nNome do cliente: ")
    idade = int(input("Idade: "))
    renda_mensal = float(input("Renda mensal (R$): "))
    valor_emprestimo = float(input("Valor desejado do empréstimo (R$): "))

    print("\nNúmero de parcelas (mínimo 3, máximo 24):")
    num_parcelas = int(input("Digite o número de parcelas: "))

    # Validação de parcelas
    if num_parcelas < 3 or num_parcelas > 24:
        print("\nERRO: O número de parcelas deve estar entre 3 e 24!")
        return

    # Verificar aprovação
    if not pode_aprovar(idade, renda_mensal, valor_emprestimo):
        print("\n" + "=" * 60)
        print("RESULTADO DO FINANCIAMENTO")
        print("=" * 60)
        print(f"\nCliente: {nome_cliente}")
        print("Status: FINANCIAMENTO NEGADO")

        if idade <= 18:
            print("Motivo: Cliente menor de idade (exigido > 18 anos)")
        else:
            limite_maximo = renda_mensal * 20
            print(f"Motivo: Valor do financiamento excede o limite")
            print(f"Limite máximo: R$ {limite_maximo:.2f}")
            print(f"Valor solicitado: R$ {valor_emprestimo:.2f}")

        print("=" * 60)
        return

    # Cálculos do financiamento
    taxa_juros = definir_taxa(num_parcelas)
    valor_parcela = calcular_parcela(valor_emprestimo, taxa_juros, num_parcelas)
    valor_total_pago = calcular_total(valor_parcela, num_parcelas)
    total_juros = calcular_juros(valor_total_pago, valor_emprestimo)

    # Exibição dos resultados
    print("\n" + "=" * 60)
    print("RESULTADO DO FINANCIAMENTO")
    print("=" * 60)
    print(f"\nCliente: {nome_cliente}")
    print("Status: FINANCIAMENTO APROVADO")
    print(f"\nValor financiado: R$ {valor_emprestimo:.2f}")
    print(f"Taxa de juros aplicada: {taxa_juros * 100:.1f}% ao mês")
    print(f"Número de parcelas: {num_parcelas}")
    print(f"\nValor da parcela: R$ {valor_parcela:.2f}")
    print(f"Valor total pago: R$ {valor_total_pago:.2f}")
    print(f"Total de juros pagos: R$ {total_juros:.2f}")
    print("=" * 60)


if __name__ == "__main__":
    main()