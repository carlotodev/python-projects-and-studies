# verificar se o numero tem digitos seguidos adjacentes
numeroInteiro = int(input("insira aqui um número inteiro: "))

digito1 = 0
digito2 = 1

while numeroInteiro > 0 and digito1 != digito2:
    digito2 = digito1
    digito1 = numeroInteiro % 10
    numeroInteiro = numeroInteiro // 10
    
if digito1 == digito2:
    print("este número possui digitos seguidos e adjacentes")
else:
    print("esse número não possui numeros seguidos e adjacentes")