objeto = "caneta"
cor = "amarela"
objeto = objeto + " " +  cor
print(objeto)

str = "caneta amarela"

if objeto not in str:
    print("Amarela é uma substring de str")
else:
    print("não é uma substring de str")

print(" -- ")

str = "a minha casa é amarela"
print(str)
str = str.replace("casa", "")
print(str)

print(len("str")) # tamanho da string

print(str.index("é")) # posicao

parte1 = str.split()

print(parte1[0])
print(" -- ")

parte1 = ["a","b","c", "D", "231412", "fasfsagfasga"]

for i in range(len(parte1)):
    print(parte1[i])
lista = []

for i in range(6):
    lista.append(parte1[i] + " "+ "bla")

for i in range(len(lista)):
    print(lista[i])

for i in range(1,10,3): # inicio, termino-1, incremento
    print(i)


j = 0
while j < 10:
    print(j)
    j+=1
