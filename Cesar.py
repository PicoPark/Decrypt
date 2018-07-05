import string 
import sys

class Cesar:

	#Calcul la fréquence d'appartition des lettre dans une chaine de charactère
	def frequency(data): 
		freq = [0]*26 
		for character in data.upper(): 
			if character in string.ascii_uppercase: 
				freq[ord(character) - ord('A')] += 1 

		return freq 


	#algo qui permet de trouver la clé de décryptage
	def findKey(encodedStr): 
		frequencies = frequency(encodedStr) 
		max_value = max(frequencies) 
		#4 : indice de E 
		key = frequencies.index(max_value) - 4 
		return key


	def algo(text, key):
		result = "" 
		for i in range(len(text)): 
			c = text[i] 

			if c in string.ascii_uppercase: 
				result += chr((ord(c) +  key - ord('A')) % 26 + ord('A')) 
			elif c in string.ascii_lowercase: 
				result += chr((ord(c) + key - ord('a')) % 26 + ord('a')) 
			else: 
				result += c 

		return result


	def decode(text):
		result=""
		key = findKey(text)

		if (key > 0):
			key = 0 - key

		return algo(text, key)

#	def main(argv):
#		# Extrait de la zone du dehors d'Alain Damasio
#		text ="Devenir libre est une maladie qui se transmet par le sang. Une fois contractee, aucun patron, aucun gouvernement, aucune prison ni aucune arme ne vous en guerissent. C'etait cela qui me rassurait quand je voyais les enfants courir dans les villages. Ils etaient deja atteints, ils etaient tous malades, gangrenes de liberte... "#

#		print("text initiale : \n "+ text +"  \n")

#		resultEncode = CesearCode(text, 5,False)
#		print("Encodage : " + resultEncode+"  \n")

#		resultDecode = CesearCode(resultEncode,5)
#		print("Decodage : " + resultDecode+"  \n")

#		resultDecodeWithoutKey = CesearCode(resultEncode)
#		print("Decodage Sans clé : " + resultDecodeWithoutKey +"\n")#
#












