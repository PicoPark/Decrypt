
import string 
import sys
import Polybe
import Cesar
import Atbash
import Scytale



def main():
	result =""
	dicoScytale = [" ca "," est "," ce ", " ci ", " de "," du ", " en ", " es ", " et ", " eu " , " il "," je " ," la " ," le " ," ma " , " me " , " ou " , " sa " , " se " , " si " , " ta " , " te " , " tu " ,  " un " , " va " , " vu "]
	resulytScytale = []
	#text ="Wvevmri oryiv vhg fmv nzozwrv jfr hv gizmhnvg kzi ov hzmt. Fmv ulrh xlmgizxgvv, zfxfm kzgilm, zfxfm tlfevimvnvmg, zfxfmv kirhlm mr zfxfmv zinv mv elfh vm tfvirhhvmg. X'vgzrg xvoz jfr nv izhhfizrg jfzmw qv elbzrh ovh vmuzmgh xlfiri wzmh ovh erooztvh. Roh vgzrvmg wvqz zggvrmgh, roh vgzrvmg glfh nzozwvh, tzmtivmvh wv oryvigv... "

	#text="GHYHQLU OLEUH HVW XQH PDODGLH TXL VH WUDQVPHW SDU OH VDQJ. XQH IRLV FRQWUDFWHH, DXFXQ SDWURQ, DXFXQ JRXYHUQHPHQW, DXFXQH SULVRQ QL DXFXQH DUPH QH YRXV HQ JXHULVVHQW. F'HWDLW FHOD TXL PH UDVVXUDLW TXDQG MH YRBDLV OHV HQIDQWV FRXULU GDQV OHV YLOODJHV. LOV HWDLHQW GHMD DWWHLQWV, LOV HWDLHQW WRXV PDODGHV, JDQJUHQHV GH OLEHUWH..."

	#text = "CGESICEE  ME  LHP MEAAO ES UR STPTT S LEA ADU N"
	#text = "DSQ NTOR N  U SOVTEES ETUPEENNPEECIQ UIAIN LV IA E ER N  ULRLINT IEU RF  MIA EMAEILET GBNNS O AESRGTENSRANSTAEIEELIAUNOMUA D  GT ONRR  ESUCTNEEIR EDE  UGT MT  CU   RTAJNASDISRELARSCUN NNI SEFN EL E ILAAON AIESCS AS JSMN BANNN GU  SEUVN IA AE RDSGTPOCAVELROTLL ELS EIM.RAUUUONAAYSESATA   EE ATVNCUT IA S TADD E TUCREEUS QTIC ETIEE "
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
			for i in range(0,20):
				cpt = 0
				scytaleDecode = Scytale.Scytale.decode(text,i)
				#if(isDecrypt(scytaleDecode)):
				result = "Scytale : " + str(i) +" :" + scytaleDecode
				print(result)

				
				for item in dicoScytale:
					if (item in scytaleDecode.lower()):
						cpt +=1

				resulytScytale.append(cpt)

			key = resulytScytale.index(max(resulytScytale))

			scytaleDecode = Scytale.Scytale.decode(text,key)
			print(resulytScytale)
			result = "Scytale : " + str(key) +" :" + scytaleDecode
			print(result)


			#else:

				#cesarDecode= Cesar.Cesar.decode(text)
			#	if(isDecrypt(cesarDecode)):
			#		result = "Cesar : " + cesarDecode

		#essayer cesar, scytale ou vigenere (optionnel)


	print(result)
	

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