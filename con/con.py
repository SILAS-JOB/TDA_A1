

"""
Seleção de idade mínima e verificação de idade do usuário
"""


idade_necessaria = int(input("Digite a idade mínima necessária para entrar no evento: "))

idade_usuario = int(input("Digite a sua idade: "))

if idade_usuario >= idade_necessaria:
    print("Aproveite o evento !")
else:
    print("Senhor vamos acionar a polícia.")