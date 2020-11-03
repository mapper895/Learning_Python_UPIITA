"""Contar  Bobs de una frase."""

def counting_bobs(text):
    """Function that counts bob´s times in a text."""
    text = text.lower()
    bobs_count = 0
    for char in range(len(text)):
        if text[char:char+3] == 'bob':
            bobs_count += 1

    return bobs_count

text = input('Enter a text: ')
bobs_count = counting_bobs(text)
print(f'There are {bobs_count} in the text')
