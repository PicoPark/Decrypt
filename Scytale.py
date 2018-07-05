import string 
import sys

class Scytale:

	def decode(text,key):
		result = ""
		for i in range(0,key):
			for j in range (i,len(text), key):
				result+= text[j]


		return result