X = int(input())
Y = int(input())

aux = X - Y
print(aux)
impares = 0
aux2 = X - 1

while(aux > 0):
    print(aux2, "AUX2")
    if aux2 % 2 != 0:
        print(aux2, "IMPAR")
        impares += aux2
    aux-=1
    aux2-=1

print(impares, "resutlado")
