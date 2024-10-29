class TriLegal:
      
   def __init__(self, ladoA:float, ladoB:float, ladoC:float):
      
      self.ladoA = ladoA
      self.ladoB = ladoB
      self.ladoC = ladoC
   
   def calcularPerimetro(self) -> float:
      return self.ladoA + self.ladoB + self.ladoC
   
   # def recalcular(self) -> float:
   #    ladoA = float(input("lado a: "))
   #    ladoB = float(input("lado b: "))
   #    ladoC = float(input("lado c: "))
   # entrei no loop, então automaticamente irá chamar a função do começo, não tendo que recalcular
      
   def tipoTrian(self) -> str:
      if self.ladoA == self.ladoB == self.ladoC : return "Equilátero, os três lados são iguais"
      elif self.ladoA == self.ladoB or self.ladoA == self.ladoC or self.ladoB == self.ladoC : return "Isóceles, dois lados possuem a mesma medida "
      else: return "Escaleno, nenhum lado igual"
   
   def condicao(self) -> bool:
      if self.ladoA <=0 or self.ladoB <=0 or self.ladoC <=0 : 
         print("ValueError: numero deve ser maior que zero")
         return False
      return True
   
#principal:
while True: 
   
   ladoA = float(input("lado a: "))
   ladoB = float(input("lado b: "))
   ladoC = float(input("lado c: "))
   
   if ladoA == -1 and ladoB == -1 and ladoC == -1: break
   
   triangulo = TriLegal(ladoA, ladoB, ladoC)
   
   if triangulo.condicao() == False:
      continue

   perim = triangulo.calcularPerimetro()
   tipo = triangulo.tipoTrian()
   
   print(f"o perímetro do triângulo com {triangulo.ladoA}, {triangulo.ladoB}, {triangulo.ladoC} é de {perim}. e ele é do tipo {tipo}\n")
   print("digite -1 para todos os lados sair: \n")
print("\nfim")


