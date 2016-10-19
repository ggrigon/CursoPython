from Pessoa import Aluno # from ARQUIVO import CLASSE

def main():
    alunos = []
    # a = Aluno("teste", 10, "curso", 1, 2, 3)
    # print(a.getNome(),a.getIdade())
    # a.calculaMedia()
    # geraArquivo(a)
    # lerArquivo(a)

    while True:
        opcao = input("Para cadastrar aluno digite: C\n Para sair digite: S\n Digite a opção desejada: ")
        if opcao == "s":
            break
        elif opcao == "c":
            nome = input("Nome: ")
            idade = input("Idade: ")
            curso = input("Curso: ")
            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))
            nota3 = float(input("Nota 3: "))
            a = Aluno(nome, idade, curso, nota1, nota2, nota3)
            a.calculaMedia()
            alunos.append(a)

    if len(alunos) > 0:
         geraArquivo(alunos)

def geraArquivo(alunos):
    arquivo = open("cadastro.txt", "a")
    for elemento in alunos:
        arquivo.writelines("Nome: " + elemento.getNome() + "\n")
        arquivo.writelines("Idade: " + format(elemento.getIdade() + "\n"))
        arquivo.writelines("Curso: " + elemento.getCurso() + "\n")
        arquivo.writelines("N1: " + format(elemento.getNota1()) + "\n")
        arquivo.writelines("N2: " + format(elemento.getNota2()) + "\n")
        arquivo.writelines("N3: " + format(elemento.getNota3()) + "\n")
        arquivo.writelines("Media: " + format(elemento.getMedia()) + "\n" + "\n")
    arquivo.close()

        # arquivo = open("cadastro.txt", "a")
        # arquivo.writelines("Nome: " + a.getNome() + "\n")
        # arquivo.writelines("Idade: " + format(a.getIdade()) + "\n")
        # arquivo.writelines("Curso: " + a.getCurso() + "\n")
        # arquivo.writelines("Nota 1: " + format(a.getNota1()) + "\n")
        # arquivo.writelines("Nota 2: " + format(a.getNota2()) + "\n")
        # arquivo.writelines("Nota 3: " + format(a.getNota3()) + "\n")
        # arquivo.writelines("Média: " + format(a.getMedia()) + "\n")
        # arquivo.writelines("\n")
        # arquivo.close()


def lerArquivo(a):
    try:
        arquivo = open("cadastro.txt", "r")
        texto = arquivo.readlines()
        print(texto)
        for linha in texto:
            print(linha, end="")
    except:
        print("Erro na função lerArquivo")

main()