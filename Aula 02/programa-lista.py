nomes = []
rg = []

for i in range(5):
    nomes.append(input("Nome: "))
    rg.append(input("RG: "))

for i in range(len(nomes)):
    print(nomes[i], rg[i])