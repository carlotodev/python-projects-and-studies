# mostra se os números dados estão em ordem crescente ou não
numero1 = int(input("insira aqui o primeiro numero: "))
numero2 = int(input("insira aqui o segundo numero: "))
numero3 = int(input("insira aqui o terceiro numero: "))

if numero1 < numero2 < numero3:
    print("crescente")
else: print("não está em ordem crescente")