# "Curso de Python 3 - Mundo 3: Estrutura Composta - Tuplas")

# q72 = "Crie um programa que tenha uma tupla totalmente preenchida com contagem por extensão, de zero a vinte. O rograma deverá ler um n° (0 a 20)e mostrar por extensão"

while True:
   exten = ("zero","um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

   entrada = int(input("digite um valor inteiro: "))
   
   if entrada == 000 : break   
   
   if 0<= entrada <=20:
      print(f"{entrada} = {exten[entrada]}")
   else:
      print("Valor fora do intervalo pedido\n")

   print("Para sair digite 000: ")

print("fim")