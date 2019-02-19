#Calsse que define uma abstração de mamiferos

class Animal():
	#def __init__(self, peso=0, idade=0, cor='', nome='', especie=''): #Esse é o construtor
	def __init__(self, **kwargs): #Esse é o construtor

		for k in kwargs:
			self[k] = kwargs[k]
		

	def __str__(self):
		return 'Voce printou o gatinho:  {0}'.format(self.nome)

	def __setitem__(self, key, value)
		setattr(self)

gatin = Animal(nome='Lucas', cor='Rosa')
gatin2 = Animal(nome='Roger', cor='Pink')

print(gatin)
print(gatin)
