import tkinter as tk

# --- 1. DEFINIÇÃO DA CLASSE ---
class Pessoa:
    def __init__(self, nome, data_nascimento, profissao, x, y):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.profissao = profissao
        self.x = x
        self.y = y
        self.pai = None
        self.mae = None
        self.filho = []
  
    def adcionar_pai(self, pai):
        self.pai = pai
        if self not in pai.filho:
            pai.filho.append(self)
  
    def adcionar_mae(self, mae):
        self.mae = mae
        if self not in mae.filho:
            mae.filho.append(self)

# --- 2. FUNÇÕES DE DESENHO ---
def desenhar_pessoa(canvas, pessoa):
    # Desenha a caixa (retângulo)
    canvas.create_rectangle(pessoa.x, pessoa.y, pessoa.x + 140, pessoa.y + 50, 
                            fill='lightblue', outline='black', width=2)
    # Escreve o nome dentro
    canvas.create_text(pessoa.x + 70, pessoa.y + 25, text=pessoa.nome, 
                       font=('Arial', 9, 'bold'), width=130, justify='center')

def ligar_familia(canvas, pessoa):
    # Se a pessoa tem um pai definido, desenha linha entre eles
    if pessoa.pai:
        canvas.create_line(pessoa.pai.x + 70, pessoa.pai.y + 50, 
                           pessoa.x + 70, pessoa.y, fill='gray', width=2)
    # Se a pessoa tem uma mãe definida, desenha linha entre eles
    if pessoa.mae:
        canvas.create_line(pessoa.mae.x + 70, pessoa.mae.y + 50, 
                           pessoa.x + 70, pessoa.y, fill='gray', width=2)

# --- 3. CONFIGURAÇÃO DA INTERFACE ---
root = tk.Tk()
root.title('Árvore Genealógica - Família Silva - Dados Fictícios para fins didáticos')
canvas = tk.Canvas(root, width=1000, height=600, bg='white')
canvas.pack()

# --- 4. CRIAÇÃO DOS DADOS (OBJETOS) ---

# Geração 1 - Avós
joao = Pessoa('João Silva', '1925', 'Agricultor', 400, 30)
maria = Pessoa('Maria Oliveira Silva', '1927', 'Professora', 600, 30)

# Geração 2 - Filhos e Cônjuges
carlos = Pessoa('Carlos Silva', '1950', 'Engenheiro', 200, 150)
ana = Pessoa('Ana Costa Silva', '1953', 'Médica', 20, 150)
helena = Pessoa('Helena Silva', '1955', 'Artista', 450, 150)
roberto = Pessoa('Roberto Mendes', '1952', 'Músico', 620, 150)
paulo = Pessoa('Paulo Silva', '1960', 'MEI', 800, 150)

# Geração 3 - Netos
fernanda = Pessoa('Fernanda Silva', '1979', 'Advogada', 110, 300)
marcos = Pessoa('Marcos Silva', '1982', 'Programador', 270, 300)
luisa = Pessoa('Luisa Mendes', '1980', 'Bailarina', 450, 300)
tiago = Pessoa('Tiago Mendes', '1985', 'Chef', 610, 300)

# Geração 4 - Bisnetos
ricardo = Pessoa('Ricardo Torres', '1976', 'Jornalista', 110, 450)
sofia = Pessoa('Sofia Torres', '1980', 'Eletricista', 270, 450)
lucas = Pessoa('Lucas Torres', '1985', 'Professor', 430, 450)
ricardo.adcionar_pai(paulo)
ricardo.adcionar_mae(fernanda)

# --- 5. DEFININDO QUEM É PAI E MÃE (RELAÇÕES) ---
# Filhos de João e Maria
for filho in [carlos, helena, paulo]:
    filho.adcionar_pai(joao)
    filho.adcionar_mae(maria)

# Filhos de Carlos e Ana
fernanda.adcionar_pai(carlos)
fernanda.adcionar_mae(ana)
marcos.adcionar_pai(carlos)
marcos.adcionar_mae(ana)

# Filhos de Helena e Roberto
luisa.adcionar_pai(roberto)
luisa.adcionar_mae(helena)
tiago.adcionar_pai(roberto)
tiago.adcionar_mae(helena)

# Filhos de Paulo e Fernanda (Exemplo da Sofia e Lucas)
sofia.adcionar_pai(paulo)
sofia.adcionar_mae(fernanda)
lucas.adcionar_pai(paulo)
lucas.adcionar_mae(fernanda)

# --- 6. RENDERIZAÇÃO FINAL ---
familia = [joao, maria, carlos, ana, helena, roberto, paulo, 
           fernanda, marcos, luisa, tiago, ricardo, sofia, lucas]

# Desenha as linhas primeiro para ficarem "atrás" das caixas
for p in familia:
    ligar_familia(canvas, p)

# Desenha as caixas com os nomes por cima
for p in familia:
    desenhar_pessoa(canvas, p)

root.mainloop()
