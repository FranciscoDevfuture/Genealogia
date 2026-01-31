#Projeto criar Árvore Genealógica
#mistura de lógica, estrutura de dados,
#Passo 01- Criar modelo de dados(classe Pessoa)
#Em construção
#Criando classes

class Pessoa:
  def __init__(self,nome,nascimento=None,profissao=None,x=0,y=0):
    self.nome = nome
    self.nascimento = nascimento
    self.profissao = profissao
    self.pai = None
    self.mae = None
    self.filho = []
    self.x = x 
    self.y = y

  def adcionar_pai(self,pai):
    self.pai = pai
    pai.filhos.append(self)

  def adcionar_mae(self,mae):
    self.mae = mae
    mae.filhos.append(self)
# Essa classe representa qulquer pessoa da árvore.

#passo 02- Implementando função de desenho no Canvas

def desenhar_pessoa(canvas, pessoa):
  largura = 140
  altura = 50

  canvas.create_rectangle(pessoa.x, pessoa.y,pessoa.x + largura,pessoa.y+altura,fill='#e6f2ff', outline='black')

  texto = pessoa.nome
  if pessoa.nascimento:
    texto += f'{pessoa.nascimento}'

  canvas.create_text(
      pessoa.x + largura / 2,
      pessoa.y + altura / 2,
      text=texto, fonte=('Arial',10,'bold')
  )
  
  #Passo 03-Funções que são úteis para consultar
#Formas de navegar na Árvore

#Mostrar pais e Mostrar Filhos

def mostrar_pais(pessoa):
  if pessoa.pai:
    print('Pai:',pessoa.pai.nome)
  if pessoa.mae:
    print('Mâe:',pessoa.mae.nome)

def mostrar_filhos(pessoa):
  for filho in pessoa.filhos:
    print('Filho:',filho.nome)

#ligaçao entre pai e mae

def ligar(canvas,pai,mae,filho):
  canvas.create_line(
      pai.x + 70, pai.y + 50,
      filho.x + 70, filho.y, width=2
  )
#Passo - 03 - Montando a Familia Silva
#Primeira geração- Avós

joao = Pessoa('João Silva','1925-1998','Agricultor',350,30)
maria = Pessoa('Maria Oliveira Silva','1927-2005','Professora',550,30)
