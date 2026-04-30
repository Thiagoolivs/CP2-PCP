a = float(input("Insira o lado A (sendo o maior lado) do triângulo: "))
b = float(input("Insira o lado B do triângulo: "))
c = float(input("Insira o lado C do triângulo: "))

#se forma ou não triângulo
if not (a + b > c and a + c > b and b + c > a):
    print('não forma triangulo')

#lados
if a == b and b == c:
    print('triângulo equilátero')
elif a==b or a == c or b ==c:
    ('triângulo isósceles')
elif a != b or a !=c or b != c:
    print('triangulo escaleno')
else:
    print('Algum erro de digitação, revise.')

#angulos
hip = a**2
cat = b**2 + c**2

#definição do tipo
if hip == cat:
    print('triângulo retângulo')
elif hip > cat:
    print('triângulo obtuso')
elif hip < cat:
    print('triângulo agudo')
else:
    print('existe algum erro de digitação, revise.')