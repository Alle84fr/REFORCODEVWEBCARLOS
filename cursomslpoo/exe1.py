q2 = "Pedra, papel e tesoura é um jogo com dois participantes. O jogo tem rodadas. Em cada rodada, um participante escolhe um símbolo de pedra, papel ou tesoura, e o outro participante faz o mesmo. O vencedor da rodada é determinado pela comparação dos símbolos escolhidos. As regras do jogo estabelecem que pedra ganha de tesoura, tesoura vence (corta) papel e papel vence (embrulha) pedra. O vencedor da rodada recebe um ponto. O jogo continua pela quantidade de rodadas que os participantes combinarem. O vencedor é o participante com o maior número de pontos."

class Jogo:
   def __init__(self):
      self.fimDeJogo = False
      self.participante1 = Participante()
      self.participantes2 = Participante()
   
   
class Participante:
   def __init__(self):
      self.pontos = 0
      self.escolha = ""

class Rodada:
   

