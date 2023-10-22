#multiplica os numeros dados pelo usuario
tamanho = int(input("insira aqui quantos números serão multiplicados: "))

vezes = 0
valorTotal = 1

while tamanho > vezes:
    numero = int(input("insira aqui os números a serem multiplicados: "))
    valorTotal = valorTotal * numero
    vezes = vezes + 1
    
print("a multiplicação dos seus números é:", valorTotal)