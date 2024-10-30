rupla = (1, 2, 5, 9, 10, 2, 3, 2, 8, 0)

print(f"\ntodos elementos - rupla =  {rupla}\n")
print(f"apenas uma dos eleemntos - rupla[2] =  {rupla[2]}\n")
print(f"aqui é fatiamento, quase que pega o elemento, neste caso o 1° e o 2° - rupla[0:2] =  {rupla[0:2]}\n")
print(f"pega os elementos para frente do índice posto, rupla[3:] =  {rupla[3:]}: \n")
print(f"pega do 0 ao 3, ignora o 4 rupla[:4] =  {rupla[:4]}\n")
print(f"vem do último índice para o primeiro - rupla[-3] este inicia no -1 =  {rupla[-3]}\n")
print(f"pega n° de elementos -len (rupla) =  {len(rupla)}\n")
print(f"contar, achar valores repetidos, rupla.count(2) =  {rupla.count(2)}\n")
print(f"organizar o print - sorted - sorted(rupla) =  {sorted(rupla)}: \n")
print(f"pegar a 1° posição de um n° - index - rupla.index(2) =  {rupla.index(2)}\n")


for n in rupla:
   print(f" for n in rupla = {n}")

print("Tuplas são IMUTÁVEIS")
   
animal = ("cavalo", "égua", "pato", "pata", "cachorro", "cadela")
for cont in range(0, len(animal)):
   print(f"cont = {(cont)} + animal[cont] {(animal[cont])}")
   
print("para deletar é só por del(tupla)")

