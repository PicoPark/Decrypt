import string 
import sys

class Vigenere:



	def decode(text, secret):
		result = ""
	    for i , c in enumerate(text) :
	        d = secret[ i % len(secret) ]
	        d = ord(d) - 65
	        d = 26 - d
	        result += chr((ord(c)-65+d)%26+65)
	    return result