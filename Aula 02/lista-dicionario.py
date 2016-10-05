dicionario = {"Nome": "Guilherme", "idade": 30, "RG": 6064367839}
lista = []
lista.append(dicionario)

dicionario2 = {"Nome": "abcde", "idade": 1, "RG": 123456}

lista.append(dicionario2)

print(lista[0]["Nome"])
print(lista[1]["Nome"])