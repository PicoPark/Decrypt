import string 
import sys

class Atbash:

	def decode(text):
		alphabet =  string.ascii_uppercase
		al_encode =  alphabet[::-1]

		text = text.upper()
		result = ""
		tmp=''

		for c in text:
			n = al_encode.find(c)
			if n < 0:
				#print("echec")
				tmp = c
			else:
				tmp = string.ascii_uppercase[n]

			result = result + tmp
		return result;

