def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)

something = input('Введите текст:')
something = ''.join([c for c in something if c not in ('!', '?', '.', ' ', ',')])

something = something.replace(" ", "")
something = something.lower()

if (is_palindrome(something)):
	print('Да, это палиндром')
else:
	print('Нет, это не палиндром')