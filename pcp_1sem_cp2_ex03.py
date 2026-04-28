import pandas as pd

cp = list(map(float, input("Digite as notas dos 3 checkpoints separados por espaço.").split()))
sp1 = float(input("Digite a nota da sprint 1: "))
sp2 = float(input("Digite a nota da sprint 2: "))
gs = float(input("Digite sua nota Global Solution: "))

#ordena em ordem crescente e remove o menor valor(o primeiro item)
cp.sort()
cp.pop(0)

#calculo da media sem peso
mediaSpeso = (cp[0] + cp[1] + sp1 + sp2)/4

#calculo da media com peso
mediaCpeso = mediaSpeso * 0.4 + (gs * 0.6)

#exibição das médias
print()
print('---Seus resultados do semestre---')
print(f'A sua média do semestre sem peso é de: {mediaSpeso:.1f}')
print(f'A sua média do semestre com peso é de: {mediaCpeso:.1f}')

#criação de uma tabela para mostrar as notas, usando pandas
tabela = pd.DataFrame ({
    'Média-S-Peso' , mediaSpeso,
    'Média-C-peso' , mediaCpeso
})
print(tabela)