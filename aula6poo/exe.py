class Professor:
   def __init__(self, nome:str, matricula:int, disciplina:str, cargamax:int):
      self.name = nome
      self.matri = matricula
      self.disci = disciplina
      self.carmax = cargamax
      self.status = "me matando de estudar"
   
   def setCargaMx(self):
      cargamax = int(input('corrigir carga de horas máxima:'))
      self.carma = cargamax
   
   
# principal
nome = input("nome: ")
matricula = int(input("matricula: "))
disciplina = input("disciplin: ")
cargamax = int(input("carga max: "))

prof = Professor(nome, matricula, disciplina, cargamax)    

print(f"{prof.name} que leciona {prof.disci}, cuja matrícula é {prof.matri}, tem {prof.carmax}h ")
print(prof.status)

prof.setCargaMx()

print(f"carga máxima de horas atualizou para {prof.carma}")