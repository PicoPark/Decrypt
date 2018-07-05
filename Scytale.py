import string 
import sys

class Scytale:

	def findKey(text):

		return 8

	def decode(text,key=0):
		
		if(key=0):
			key = findKey(text)
		result = ""
		for i in range(text):
			for j in range (i,len(text), key):
				result = result+text[j]


		return result