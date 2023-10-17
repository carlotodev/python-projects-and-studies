# calcula as raízes de uma equação quadrática usando bhaskara e imprime elas em ordem crescente
import math

a = float(input("insira aqui o valor de a: "))
b = float(input("insira aqui o valor de b: "))
c = float(input("insira aqui o valor de c: "))

delta = (b ** 2) - (4 * a * c)

if(delta) == 0:
    raiz1 = (-b + math.sqrt(delta)) / (a * 2)
    print("a raiz desta equação é", raiz1)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
            raiz1 = (-b + math.sqrt(delta)) / (a * 2)
            raiz2 = (-b - math.sqrt(delta)) / (a * 2)
            if raiz1 < raiz2:
                print("as raízes da equação são", raiz1, "e", raiz2)
            else:
                print("as raízes da equação são", raiz2, "e", raiz1)