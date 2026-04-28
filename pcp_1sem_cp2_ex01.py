# Exercício 1 - Imposto e valor da carga
estado = int(input("Digite o código referente ao seu Estado (entre 1 e 5): "))
carga_toneladas = float(input("Digite o peso da sua carga em TONELADAS: "))
cod_carga = int(input("Digite o código da sua carga (entre 10 e 40): "))

peso_quilos = carga_toneladas * 1000

teve_erro = False
imposto = 0.0
preco_kg = 0.0

#match/case para definir o imposto
match estado:
    case 1:
        imposto = 0.35
    case 2:
        imposto = 0.25
    case 3:
        imposto = 0.05
    case 4:
        imposto = 0.15
    case 5:
        imposto = 0.00
    case _:
        print("Erro: Código de Estado inválido.")
        teve_erro = True

#if/elif/else para definir o preço por quilo
if 10 <= cod_carga <= 20:
    preco_kg = 100
elif 21 <= cod_carga <= 30:
    preco_kg = 250
elif 31 <= cod_carga <= 40:
    preco_kg = 340
else:
    print("Erro: Código de carga inválido.")
    teve_erro = True

#função que calcula as informações
def infoTotais(kilos, preco, taxa_imposto):
    valorCarga = kilos * preco
    valorImposto = valorCarga * taxa_imposto
    valorTotal = valorCarga + valorImposto
    return valorCarga, valorImposto, valorTotal

#chamar a função e exibir os valores finais
if not teve_erro:
    valor_carga, valor_imposto, valorTotal_total = infoTotais(peso_quilos, preco_kg, imposto)

    print("\n--- RESUMO DA CARGA ---")
    print(f"O valor puro da carga é: R$ {valor_carga:.2f}")
    print(f"O valor do imposto é: R$ {valor_imposto:.2f}")
    print(f"O valor TOTAL a pagar é: R$ {valorTotal_total:.2f}")