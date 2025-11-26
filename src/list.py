import utils.cl as cl


"""
Listagem de alunos e resultado no terminal após comando exit
"""

names : str = ""
while True:
    name: str = input("Escreva o nome dos alunos, ou exit para sair : \n")
    if name.lower() == 'exit':
        break
    names += name + ", "
names = names[:-2]  
print("Nomes dos alunos:", names)
cl.clean()

