q2 = "Pedra, papel e tesoura é um jogo com dois participantes. O jogo tem rodadas. Em cada rodada, um participante escolhe um símbolo de pedra, papel ou tesoura, e o outro participante faz o mesmo. O vencedor da rodada é determinado pela comparação dos símbolos escolhidos. As regras do jogo estabelecem que pedra ganha de tesoura, tesoura vence (corta) papel e papel vence (embrulha) pedra. O vencedor da rodada recebe um ponto. O jogo continua pela quantidade de rodadas que os participantes combinarem. O vencedor é o participante com o maior número de pontos."

class Jogo:
   def __init__(self):
      self.fimDeJogo = False
      self.participante1 = Participante()
      self.participantes2 = Participante()
      
   def start (self):
      rodada = Rodada(self.participante1, self.participantes2)
   
   def condicaoDefimDeJogo(self):
      print(" implement, adicone lógica futura")
      
   def ganhador(self):
      pprint(" implement, adicone lógica futura")

   
class Participante:
   def __init__(self, name):
      self.pontos = 0
      self.escolha = ""
      self.name = name
      
   def escolha(self):
      input(f"{self.name}, selecione pedra, papel ou tesoura: ")
      print(f"{self.name} ecolheu {self.escolha}")
      
   def numerosDeChoise(self):
      switcherTroca = {
         "pedra": 0,
         "papel": 1,
         "tesoura": 2
      }
      return switcherTroca [self.escolha]

      
#adicionando adiconado name como parâmentro e função chance
#input = > {name} é um espaço reservado (placeholder) que será subtituido polo valor da variável name - "{name}, selecione pedra, papel ou tesoura:" esta parte significa que é uma string formatada
#final do input = > o método .format() que mostra a "referência de onde irá tirar a informação que será substituida"
#ex: self.name = Abidu - ao mostrar na tela aparecerá - Abidu, selecione pedra, papel ou tesoura: 

#duas formas de escrever, usarei f-string 
# input("{name}, selecione pedra, papel ou tesoura: ".format(name=self.name))
# input(f"{self.name}, selecione pedra, papel ou tesoura: ")
# print("{name} ecolheu {choise}".format(name = self.name, choise = self.chance))
# print(f"{self.name} ecolheu {self.chance}")



 class Rodada:
   
   def __init__(self, p1, p2):
      self.rules = [
         [0, -1, 1],
         [1, 0, -1],
         [-1, 1, 0]
      ]
      
      p1 escolha()
      p2 escolha()
      
      result = self.compareEscolha(p1, p2)
      print(f"Resultado da partida {self.getResult(result)}")
   
   def comparacao(self):
      print(" implement, adicone lógica futura")
   
   def awardPointsPremiarPontos(self):
      print(" implement, adicone lógica futura")
      
   def compareEscolha(self, p1, p2):
      return self.rule[p1.numerosDeChoise()][p2.numerosDeChoise()]

#def compareEscolha permite a comparação e escolher o vencedor

   def getResult(self, result):
      res = {
         0: "empate",
         1: "vendedor"
         -1: "perdedor"
      }
      return res [result]

#esse método ajudará a determinar o resultado e imprimirá um texto fácil de entender na tela.
# O código anterior introduz o campo rules, que contém uma implementação das regras para pedra, papel e tesoura. Além disso, a #chamada a self.compareChoices() compara duas escolhas feitas. Por fim, há uma linha que imprime resultados amigáveis para leitores #na tela.

#principal

game = Jogo()

game.start()

# estou chamando a classe Jogo para que seja criada, e depois estou chamndo o MÉTODO, MÉTODO start que está dentro de Jogo e estou chamando este método start na variável game