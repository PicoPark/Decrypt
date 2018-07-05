import string 
import sys

class Atbash:

	def decode(text):
		al_encode =  string.ascii_uppercase[::1]

		text = text.upper()
		result = ""
		tmp=''

		for c in text:
			n = al_encode.find(c)
			if n <0:
				tmp = c
			else:
				tmp = string.ascii_uppercase[n]

			result = result + tmp

		return result;
		