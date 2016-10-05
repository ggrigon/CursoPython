lista = []
i = 0
while i < 10:
    lista.append(input("Digite: "))
    i+=1

print(lista)

for i in range(len(lista)):
    print(lista[i])


lista.insert(1, "insert")
print(lista)
print(type(lista))