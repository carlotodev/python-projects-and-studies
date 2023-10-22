#soma os digitos de um numero
numeroInteiro = int(input("insira aqui um numero inteiro a ter digitos somados: "))

soma = 0
digito = 0

while numeroInteiro > 0:
    digito = numeroInteiro % 10
    numeroInteiro = numeroInteiro // 10
    soma = soma + digito
    
print("a soma dos digitos do seu número é: ", soma)