#soma os numeros dados pelo usuario
numero = 0
valorTotal = 0

while numero != "pronto":
    numero = input("insira aqui números a serem somados, termine digitando pronto. ")
    if numero != "pronto":
        numero = int(numero)
        valorTotal = valorTotal + numero
    
print("a soma dos seus números é:", valorTotal)