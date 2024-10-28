q1 = "Como lição de casa, tente criar uma classe com base em um livro que você leria. Pense em como você escreveria a classe e quais propriedades ela deveria ter."

class Livro:
   def __init__(self, titu: str, aut: str, edit: str, edic: int, tipo: str,qtDePag: int, cdd:int ):
      self.titulos = titu
      self.autores = aut
      self.editoras = edit
      self.edicoes = edic
      self._tipos = tipo
      self.quantPags = qtDePag
      self.__codcdd = cdd
      
   def get_tipo(self):
      return self._tipos
   def get_cdd(self):
      return self.__codcdd
   
   def set_cdd(self, tipo):
      if tipo == 1536:
         self.__ = "brsp"

# principal

titulo = input("Título: ")
autor = input("Autor: ")
qt_pag = int(input("Quantidade de pags: "))
edit = input("Editora: ")
tipo = "terror"
edicao = int(input("Edição: "))
cdd = 123

obj_livro = Livro(titulo, autor, edit, edicao, tipo, qt_pag, cdd)
print(f"o livro {titulo} do autor {autor}, e editora {edit}, está na edição {edicao}, possui {qt_pag} paginas, é do tipo {tipo}, e este tem o cdd {cdd} ")
print(cdd)