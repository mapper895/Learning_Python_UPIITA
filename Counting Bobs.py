"""Contar  Bobs de una frase."""

def bob_count(texto):
	"""Function that counts bob´s times in a text."""
	bob_count = 0

	if 'bob' in texto:
		bob_count+1

	return bob_count

texto = input('Ingrese el texto: ')

print(bob_count(texto))

