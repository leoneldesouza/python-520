#Abrir o arquivo usuários

# Separar o valor por ","

#Escrever na tela o dicionário

#{"nome" : Hector", "Idade" : 27, "email" : "hector.silva@yahoo.com.br"}



arquivo = open('usuarios.csv')
for linha in arquivo:
	nome, idade, email = linha.split(',')
	print({"nome" : nome.strip(), "idade" : int(idade.strip()), "email" : email.strip()})











