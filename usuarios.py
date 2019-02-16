#Abrir o arquivo usuários

# Separar o valor por ","

#Escrever na tela o dicionário

#{"nome" : Hector", "Idade" : 27, "email" : "hector.silva@yahoo.com.br"}


def hprint():
    print('{0:.<20} {1:.<40}'.format('NOME', 'EMAIL'))

usuarios = []
for l in open('usuarios.csv'):
    nome, idade, email = l.split(',')
    usuarios.append({"nome" : nome.strip(), "email" : email.strip(), "idade" : int(idade.strip())})

hprint()
for u in sorted(usuarios, key=lambda i : i['nome']):
    print('{0:.<20} {1:.>40}'.format(u['nome'], u['email']))