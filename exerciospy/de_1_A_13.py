q1 = 'Escreva um programa que mostre na tela a mensagem "Saluton, Mondo!Cio Mondo!Hello world!"'

print("""Saluton, Mondo!
Cio, Mondo!
Hello, World!
Fala aí, Mundo!\n""")

q2 = "Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas para ela:"

nome = input("Digite um nome: ")
texto = "Bonvenon komencanto"
print(f"{texto}, {nome}\n")

q3 = "Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem."

sal = float(input("Diginte valor do seu salário: R$ "))
print(f"O salário do/a funcinário/a {nome} é R${sal}\n")

q4 = "Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório entre eles."

num1 = int(input("Digite um valor inteiro: "))
num2 = int(input("Digite outro valor inteiro: "))
soma = num1+num2
print(f"A soma no n° {num1} com o n° {num2} é igual a {soma}.\n")

q5 = "Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina."

nota1 = float(input("Valor nota 1: "))
nota2 = float(input("Valor nota 2: "))
mat = input("Digite a matéria: ")
print(f"O aluno {nome} tirou {nota1:.2} na primeira prova e {nota2:.2} na segunda prova de {mat}, ficando com {(nota1+nota2)/2:.3} de média\n")

q6 = "Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor."
print(f" {num1-1}, {num1}, {num1+1} \n")

q7 = "Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte."
print(f""" N° real são numeros float, decimais 'por mais que em matemática é o conjunto de muuitos tipos de números'
o dobre de {nota1} é {nota1*2:.2}
a terça parte de {nota1} é {nota1/3:.2} \n""")

q8 = "Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas." 

metro = float(input("Digite valor do metro a ser convertido, caso seja decimal, usar ponto (.) no lugar da vírgula (,): "))
dam = metro/10
hm = dam/10
km = hm/10
dm = metro*10
cm = dm*10
mm = cm * 10
print(f"""{metro:.4} metros -m- equivale a:
{dam::.4} decâmetro/s -dam-,
{hm:.4} hectômetro/s -hm-,
{km:.4} Quilômetro/s -km-,
{dm:.4} decímetro/s -dm-,
{cm:.4} centímetro/s -cm-,
{mm:.4} milímetro/s -m-.""")

q9 = "Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45."
dol = 3.45
print(f"Caso {nome} queira comprar doletas com seu salários de R${sal}, consequirá U${sal/3.45:.4}")

q10 = "Faça um algoritmo que leia a largura (b) e altura (h) de uma parede, calcule e mostre a área (a) a ser pintada e a quantidade de tinta (tinta)necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados. Uma demão"

b = float(input("Digite a largura: "))
h= float(input("Digite a altura: "))
A = b*h
tinta = A*2
print(f"com altura de {h}m² e largura de {d}m², será necessário {tinta}litros de tinta")

q11 = "Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta."