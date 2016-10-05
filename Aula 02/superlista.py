#lista dentro de listas

lista = []
lista.append("123")
lista.append("456")
lista.append(789)
superlista = []
superlista.append(lista)

print(superlista[0][1])