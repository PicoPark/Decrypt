
import string 
import sys
import Polybe
import Cesar
import Atbash
import Scytale



def main():
	result =""

	#text ="Wvevmri oryiv vhg fmv nzozwrv jfr hv gizmhnvg kzi ov hzmt. Fmv ulrh xlmgizxgvv, zfxfm kzgilm, zfxfm tlfevimvnvmg, zfxfmv kirhlm mr zfxfmv zinv mv elfh vm tfvirhhvmg. X'vgzrg xvoz jfr nv izhhfizrg jfzmw qv elbzrh ovh vmuzmgh xlfiri wzmh ovh erooztvh. Roh vgzrvmg wvqz zggvrmgh, roh vgzrvmg glfh nzozwvh, tzmtivmvh wv oryvigv... "

	text="GHYHQLU OLEUH HVW XQH PDODGLH TXL VH WUDQVPHW SDU OH VDQJ. XQH IRLV FRQWUDFWHH, DXFXQ SDWURQ, DXFXQ JRXYHUQHPHQW, DXFXQH SULVRQ QL DXFXQH DUPH QH YRXV HQ JXHULVVHQW. F'HWDLW FHOD TXL PH UDVVXUDLW TXDQG MH YRBDLV OHV HQIDQWV FRXULU GDQV OHV YLOODJHV. LOV HWDLHQW GHMD DWWHLQWV, LOV HWDLHQW WRXV PDODGHV, JDQJUHQHV GH OLEHUWH..."

	if(text.isdigit()):
		# essayer atbash ou polybe
		
			polybeDecode = Polybe.Polybe.decode(text)
			if(isDecrypt(polybeDecode)):
				result = "Polybe : " + polybeDecode

	else:
		atbashDecode = Atbash.Atbash.decode(text)
		if(isDecrypt(atbashDecode)):
			result = "Atbash : " + atbashDecode
		else:
			scytaleDecode = Scytale.Scytale.decode(text)

			if(isDecrypt(scytaleDecode)):
				result = "Scytale : " + scytaleDecode
			else:

				cesarDecode= Cesar.Cesar.decode(text)
				if(isDecrypt(cesarDecode)):
					result = "Cesar : " + cesarDecode

		#essayer cesar, scytale ou vigenere (optionnel)


	print(result)
	#print(Polybe.decode("31111342543544342242113523241511511513353431541215"))



def isDecrypt(textDecode):
	freq = [0]*26 
	for character in textDecode.upper(): 
		if character in string.ascii_uppercase: 
			freq[ord(character) - ord('A')] += 1 

	key = freq.index(max(freq)) - 4 

	if(key == 0):
		return True
	else:
		return False


if __name__ == '__main__':
	main()