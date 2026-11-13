# a) Classe Planta
class Planta:

    # Atributo de classe: pertence à classe Planta
    viveiro = "Viveiro Verde"

    # Método construtor: executado ao criar um objeto
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    # b) Método para calcular o valor total da planta
    def valor_total(self):
        return self.preco * self.quantidade

    # Método para exibir os dados da planta
    def exibir(self):
        print(f"{self.nome} - R$ {self.preco:.2f} "
              f"x {self.quantidade} = R$ {self.valor_total():.2f}")


# c) Função para calcular o valor total de todas as plantas
def calcular_total(plantas):

    total = 0

    # Percorre a lista e soma o valor de cada planta
    for planta in plantas:
        total += planta.valor_total()

    return total


# d) Entrada de dados
plantas = []

print("================================")
print("       VIVEIRO VERDE")
print("================================")

# Pergunta quantas plantas serão cadastradas
qtd_plantas = int(input("Quantas plantas deseja cadastrar? "))

# Laço para cadastrar cada planta
for i in range(qtd_plantas):

    print(f"\nCadastro da planta {i + 1}")

    nome = input("Nome da planta: ")
    preco = float(input("Preço da planta: R$ "))
    quantidade = int(input("Quantidade: "))

    # Cria um objeto da classe Planta
    planta = Planta(nome, preco, quantidade)

    # Adiciona o objeto na lista
    plantas.append(planta)


# e) Saída de dados
print("\n================================")
print(f"Viveiro: {Planta.viveiro}")
print("================================")

# Exibe os dados de cada planta cadastrada
for planta in plantas:
    planta.exibir()

# Calcula e mostra o valor total de todas as plantas
total = calcular_total(plantas)

print("--------------------------------")
print(f"Total geral: R$ {total:.2f}")


# f) Manipulação de arquivos

# Primeiro: grava os dados no arquivo (modo w)
with open("plantas.txt", "w", encoding="utf-8") as arquivo:

    # Escreve os dados de cada planta no arquivo
    for planta in plantas:
        arquivo.write(
            f"{planta.nome};{planta.preco:.2f};{planta.quantidade}\n"
        )


# Segundo: acrescenta o valor total (modo a)
with open("plantas.txt", "a", encoding="utf-8") as arquivo:

    arquivo.write(f"Total: {total:.2f}\n")


# Terceiro: abre o arquivo para leitura (modo r)
with open("plantas.txt", "r", encoding="utf-8") as arquivo:

    print("\n================================")
    print("DADOS SALVOS NO ARQUIVO")
    print("================================")

    # Lê e apresenta todo o conteúdo do arquivo
    conteudo = arquivo.read()
    print(conteudo)
