import string 
import sys

class Polybe:

	def decode(text):
		carre = [['A','B','C','D','E'],['F','G','H','I','K'],['L','M','N','O','P'],['Q','R','S','T','U'],['V','W','X','Y','Z']]
		result = ""


		for i in range(len(text)-1):
			#analyse des chiffre deux par deux
			if(i%2==0):
				# +1 et +2 car l'indice 0 correspond au 
				result = result + carre[int(text[i])-1][int(text[i+1])-1]


		return result
	