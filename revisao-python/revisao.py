# debugar o nosso codigo
#print("Ola mundo")

# variaveis (= atribuicao)
nome = "Augusto" # string
idade = 24 # int
altura = 1.66 # float
status = True # boolean

# operadores aritmeticos
# + soma
# - subtracao
# * multiplicacao
# / divisao
# // divisao inteiro
# % resto

soma = 5 + 5
diminuicao = soma - 3
multiplicacao = diminuicao * 2
divisao = multiplicacao / 2
# print(divisao)
# print(multiplicacao % 2 == 0)

# operados logicos / relacionais
# == igualdade
# != diferenca
# > maior
# < menor
# >= maior ou igual
# <= menor ou igual

# print(10 > 11)

# ESTRUTURAS DE CONDICAO (IF, ELIF, ELSE)

nota = 2

if nota > 7 or nota == 7: # nota >= 7
    print("Aprovado")
elif nota > 3 and nota < 7:
    print("Pegou exame")
else:
    print("Reprovado")


# ESTRUTURAS DE REPETICAO ou LACOS DE REPETICAO (WHILE, FOR)

#WHILE

"""
contador = 0

while contador < 10:
    print(f"Contador: {contador}")

    if contador == 5:
        print("Saindo do fluxo do WHILE")
        break

    contador += 1
"""

# FOR

for i in range(5):
    print(i)

listaDeNomes = ["Augusto", "Bruno", "Carlos", "Diego"]

for nome in listaDeNomes:
    if nome == "Bruno":
        continue

    print(nome)

    