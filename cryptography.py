import string

def cesar_cipher(text, key, cipher):
	if type(text) == str and type(key) == int:
		return "".join([chr((ord(char) + (1 if cipher else -1) * key) % 1_114_112)\
																for char in text])
	else:
		raise(TypeError)


def hack_cesar_cipher(crypted_text, alphabet):
	if type(crypted_text) == str and type(alphabet) == str:
		for possible_key in range(0, 1_114_112):
			possible_uncryption = cesar_cipher(crypted_text, possible_key, cipher=False)
			if possible_uncryption[0] in alphabet:
				print(possible_key)
				print(possible_uncryption)
				print("_"*20)
	else:
		raise(TypeError)


def vigenere_cipher(text, password, cipher):
	list_of_crypted_chars = []
	list_of_keys = [ord(char) for char in password]
	
	for index, current_char in enumerate(text):
		
		current_key = list_of_keys[index % len(list_of_keys)]
		current_crypted_char = cesar_cipher(current_char, current_key, cipher)

		list_of_crypted_chars.append(current_crypted_char)

	crypted_text = "".join(list_of_crypted_chars)

	return crypted_text


if __name__ == "__main__":
	message = "le chocolat est bon"

	crypted_text = cesar_cipher(message, 12, cipher=True) # exo 1
	print(crypted_text)

	initial_message = cesar_cipher(crypted_text, 12, cipher=False) # exo 2
	print(initial_message == message)

	hack_cesar_cipher(crypted_text, alphabet=string.printable) # exo3

	crypted_message = vigenere_cipher(text=message, password="Azerty12345!", cipher=True)
	print(crypted_message)
	initial_message = vigenere_cipher(text=crypted_message, password="Azerty12345!", cipher=False)
	print(initial_message)