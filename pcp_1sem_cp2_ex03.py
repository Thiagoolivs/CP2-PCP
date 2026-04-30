#Exercício 2 - notas do semestre e média
cp1 = cp1 = float(input("Digite a nota do checkpoint 1: "))
while cp1 < 0 or cp1 > 10:
    cp1 = float(input("Digite a nota do checkpoint 1: "))

cp2 = float(input("Digite a nota do checkpoint 2: "))
while cp2 < 0 or cp2 > 10:
    cp2 = float(input("Digite a nota do checkpoint 1: "))

cp3 = float(input("Digite a nota do checkpoint 3: "))
while cp3 < 0 or cp3 > 10:
    cp3 = float(input("Digite a nota do checkpoint 1: "))

sp1 = float(input("Digite a nota da sprint 1: "))
while sp1 < 0 or sp1 > 10:
    sp1 = float(input("Digite a nota do checkpoint 1: "))

sp2 = float(input("Digite a nota da sprint 2: "))
while sp2 < 0 or sp2 > 10:
    sp2 = float(input("Digite a nota do checkpoint 1: "))

gs = float(input("Digite sua nota Global Solution: "))
while gs < 0 or gs > 10:
    gs = float(input("Digite a nota do checkpoint 1: "))

#definindo qual a menor nota entre os checkpoint
if cp1 <= cp2 and cp1 <= cp3:
    mCP = cp1
elif cp2 <= cp1 and cp2 <= cp3:
    mCP = cp2
else:
    mCP = cp3

Checkpoints = cp1 + cp2 + cp3 - mCP

#calculo da media sem peso
mediaSpeso = (Checkpoints + sp1 + sp2) / 4

#calculo da media com peso
mediaCpeso = mediaSpeso * 0.4 + (gs * 0.6)

#exibição das médias
print()
print('---Seus resultados do semestre---')
print(f'A sua média do semestre sem peso é de: {mediaSpeso:.1f}')
print(f'A sua média do semestre com peso é de: {mediaCpeso:.1f}')
