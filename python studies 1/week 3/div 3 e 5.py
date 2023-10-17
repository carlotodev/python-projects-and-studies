# mostra se o numero dados é divisivel por 3 e por 5 ao mesmo tempo
numero = int(input("insira um número inteiro: "))

if numero % 5 == 0 and numero % 3 == 0:
    print("FizzBuzz")
else:
    print(numero)