class pessoa: # método construtor
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    # def mostra(self):
    #     print(self.nome)
    #     print(self.idade)
    #     print(self.altura)

class aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mostra(self):
        print(self.nome)
        print(self.matricula)
        print(self.curso)


def main():
    nome = input("Digite o nome: ")
    matricula = input("Digite o número da matrícula: ")
    curso = input("Digite o seu curso: ")
    guilherme = aluno(nome, matricula, curso)
    guilherme.mostra()

main()
