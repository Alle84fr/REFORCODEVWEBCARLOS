#73 tupla

# Crie uma tupla com as 20 primeiras linguagens de programação ou de marcação, qualquer outra. 
# a mostre as 5 mais usadas
# b as 4 "mortas"
# c ordem alfabética
# posição que está uma delas
# https://www.tiobe.com/tiobe-index/ - TIOBE Index for October 2024


   

ling = ("\n Python", "C++", "Java", "C", "C#", "JavaScript", "Visual Basic", "Go", "Fortran", "Delphi/Object Pascal", "SQL","Matlab", "Rust", "Scratch", "PHP", "Assembly language", "R", "Ruby", "Cobol", "Swift")
print(f" sorted coloca em ordem alfabética - {sorted(ling)}\n")
print(f" para ver as primeiras do ranking (foram postas na ordem - ling[:5] - {ling[:5]}\n")
print(f" para ver as 4 últimas ling[-4:] - {ling[-4:]}\n")

while True:
   
   entrada = input("Digite o nome de uma das linguagens e veja a posição no ranking: ")
   
   if entrada == "sair": break
   else: print(f"A linguagem {entrada} está na posição {ling.index(entrada)}")
   
   print("digite sair para encerrar")
print("fim")
   
