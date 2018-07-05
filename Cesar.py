import string 
import sys

class Cesar:

	def decode(text):
		result=""
		freq = [0]*26 
		for character in text.upper(): 
			if character in string.ascii_uppercase: 
				freq[ord(character) - ord('A')] += 1 

		key = freq.index(max(freq)) - 4 

		if (key > 0):
			key = 0 - key

		for i in range(len(text)): 
			c = text[i] 

			if c in string.ascii_uppercase: 
				result += chr((ord(c) +  key - ord('A')) % 26 + ord('A')) 
			elif c in string.ascii_lowercase: 
				result += chr((ord(c) + key - ord('a')) % 26 + ord('a')) 
			else: 
				result += c 

		return result












