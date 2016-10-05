nomecompleto = ""
nomecompleto = input("Digite o nome e sobrenome: ")

nome = nomecompleto.split()[0]
sobrenome = nomecompleto.split()[1]

print(nome)
print(sobrenome)

for i in range(2):
    print(nomecompleto.split()[i])