# x = 10
# y = 0
# while x < 100:
#     x+=10
#     y += x + 1
#     print(y)
#
# print("O numero é " + format(y))
# print("O numero é " + str(y))

def calculoMedia(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def calculoExame(media):
    nexame = float(input("Digita a nota do exame: "))
    return nexame + media / 2

def main():
    nome = input("Digite o nome: ")
    n1 = float(input("NOTA 1: "))
    n2 = float(input("NOTA 2: "))
    n3 = float(input("NOTA 3: "))
    media = calculoMedia(n1, n2, n3)
    print("Media: %.2f" % media)
    print("Aluno: ", nome, end=" ")

    if media >= 7:
        print("PASSOU JOVENZINHO")
        if media >= 9:
            print("EIEIEI")
    elif media < 7 and media >= 5:
        print("EXAME JOVENZINHO")
        notafinal = calculoExame(media)
        print("Nota final com exame: %.2f" % notafinal, end = " ")
        if(notafinal > 5):
            print("APROVADO!")
        else:
            print("REPROVADO")
    else:
        print("RODOU JOVENZINHO")

if __name__ == '__main__':
    main()