usuario = {'Nome': 'Belphegor', 'Idade': 6500, 'username': 'bel'}

del usuario['username']

for k in usuario:
	print('{0} -> {1}'.format(k, usuario[k]))
