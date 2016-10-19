# Herança de atributos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, n1, n2, n3):
        super(Aluno, self).__init__(nome, idade)  # herda da classe pessoa
        self.curso = curso
        self.nota1 = n1
        self.nota2 = n2
        self.nota3 = n3
        self.media = 0

    def getCurso(self):
        return self.curso

    def getNota1(self):
        return self.nota1

    def getNota2(self):
        return self.nota2

    def getNota3(self):
        return self.nota3

    def getMedia(self):
        return self.media

    def calculaMedia(self):
        self.media = (self.nota1 + self.nota2 + self.nota3) / 3