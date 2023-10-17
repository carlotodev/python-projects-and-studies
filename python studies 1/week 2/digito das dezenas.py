# mostra apenas o numero da casa das dezenas de algum numero dado
numerostr = input("Digite um número inteiro: ")
numero = int(numerostr)

dezenas1 = numero // 10
dezenas = dezenas1 % 10

print("O dígito das dezenas é", dezenas)