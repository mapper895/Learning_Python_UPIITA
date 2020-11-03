"""Function class."""

def hello(name='persona', lastname='exposito'):
	"""Function that return 'Hello World'.
	name: string,
	lastname: string,

 	return:string
	"""
	if name != 'persona':
		return f'¿Como estas {name}?'
	return f'Hola {name} {lastname}'

print(hello(lastname=5, name=True))