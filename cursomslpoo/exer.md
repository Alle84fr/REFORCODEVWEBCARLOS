1. = "Como lição de casa, tente criar uma classe com base em um livro que você leria. Pense em como você escreveria a classe e quais propriedades ela deveria ter."
- o que um livro tem de característica física ou que traga um valor?

- título, autor, quantidade de pag, editora, tipo, edição, cdd

- o que farei, variáveis para cada um deles, que o objeto receberá e depois devolverá

2. A primeira parte do jogo envolve configurá-lo, o que significa criar uma instância do próprio jogo e levar o jogo para um ponto em que ele fique aguardando a ação dos participantes.

class Participant:

    def __init__(self):

        self.points = 0

        self.choice = ""

class GameRound:

class Game:

    def __init__(self):

        self.endGame = False

        self.participant = Participant()

        self.secondParticipant = Participant()

-  para criar um programa em estilo OOP (object oriented programming)/ poo (programação orientada a objetos), primeiro você modela e depois codifica. A modelagem produziu a saída de uma tabela que representava por quais objetos, dados e comportamento o seu programa parece ser composto.

Desta vez vamos preencher com métodos que serão adicionados à classe e adicionar código a esse método paraq ue funcioname da maneira que deveriam

class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        self.choice = input("{name}, select rock, paper or scissor: ".format(name= self.name))
        print("{name} selects {choice}".format(name=self.name, choice = self.choice))

class GameRound:
    def __init__(self, p1, p2):
        p1.choose()
        p2.choose()
    def compareChoices(self):
        print("implement")
    def awardPoints(self):
        print("implement")

class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")
    def start(self):
        game_round = GameRound(self.participant, self.secondParticipant)

    def checkEndCondition(self):
        print("implement")
    def determineWinner(self):
        print("implement")

game = Game()
game.start()
