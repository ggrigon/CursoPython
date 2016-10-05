A, B, C = map(float, input().split())
aux = 0

if B > A:
    aux = A
    A = B
    B = aux

if C > A:
    aux = A
    A = C
    C = aux

if C > B:
    aux = B
    B = C
    C = aux

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if (A ** 2) == (B ** 2) + (C ** 2):
        print("TRIANGULO RETANGULO")
    if (A ** 2) > (B ** 2) + (C ** 2):
        print("TRIANGULO OBTUSANGULO")
    if (A ** 2)  < (B ** 2) + (C ** 2):
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if (A == B and A != C) or (B == C and B != A) or (A == C and A != B):
         print("TRIANGULO ISOSCELES")