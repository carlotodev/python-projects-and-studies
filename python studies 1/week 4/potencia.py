# eleva o numero 2 quantas vezes o usuario quiser
numPotencias = int(input("insira aqui a quantidade de vezes que deseja elevar o número 2: "))

potencia = 0

while potencia <= numPotencias:
    print(2 ** potencia)
    potencia = potencia + 1