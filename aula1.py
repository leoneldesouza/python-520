#!/usr/bin/python3


#Capiturar dois niumetoas no teminal 
# e escrever a soma dos dos

# Se o numero resultante da soma for maior que 100
# Escrever: "Que numero grandao...."
#Caso conrtrario: "Que numero pequeno....."

# Se o numero for igual a 50, escrever "....."

texto_grotesco = 'Por conseguinte, o novo modelo estrutural aqui preconizado nos obriga à análise das condições financeiras e \
administrativas exigidas. Ainda assim, existem dúvidas a respeito de como o surgimento do comércio irtual faz parte de um processo de \
gerenciamento das regras de conduta normativas. Neste sentido, a execução dos pontos do programa exige a precisão e a definição do fluxo de informações.'

nomes = ['Hector', 'Guilherme', 'Joel', 'Flávio', 'Fabiano', 'Roger', 'Cícero', 'Hugo', 'Ayron', 'Leonel', 'Pedro', 'Lucas']

#verificar se a palavra "virtual" está dentro do texto_groptesco
#Exibir apenas os 4 ultimos nomes
#.split() contar quantas palavbras tem no texto_grotesco
#exit()

#num1 = input('Digite o primeiro numero: ')

#num2 = input('Digite o segundo numero: ')


#soma = int(num1) + int(num2)


#if soma > 100:
#	print('Que numero grandao.....!')
#elif soma == 50:
#	print('...')

#else:

#	print('Que numeo pequeno....!')
#rint(nomes[-4:])

#Percorrer a linsta nomes e exibir apenas os nomes que começasm com a letra F e H

for i in nomes:
	if i[0] == 'F' or i[0] == 'H':
	print(i)



