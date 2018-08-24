#coding: utf-8

import threading as thr
import os
import string, random
import hashlib



def getHashSenhaASerProcurada():
	return geraHash('senha.txt')


def geraHashTexto(texto):
    hash = hashlib.md5()
    hash.update(texto.encode('utf-8'))
    return hash.hexdigest()


def geraHash (caminhoArquivo):
	hash = hashlib.md5()
	arquivo = open(caminhoArquivo, 'r')
	hash.update(arquivo.read())
	arquivo.close()
	

	return hash.hexdigest()

def gerarNovasPalavras():
    tamMinPalavra=6
    tamMaxPalavra=8
    totalPalavras=100

    alfabeto = string.ascii_letters + string.digits + string.punctuation

    palavra = ''
    wordlist = open('wordlist.txt','w')
    palavrasDict = {}

    while True:
        palavraGerada = random.sample(alfabeto, random.randint(tamMinPalavra, tamMaxPalavra))
        palavra= ''.join(palavraGerada)

    	palavrasDict[palavra] = None
        palavra = ''

        if len(palavrasDict) == totalPalavras:
            break


    for text in palavrasDict:
        wordlist.write(text + '\n')

    wordlist.close()
    

def verificarNoArquivoRecebido():
	retorno = verificarArquivo('wordlista')
	
	if retorno == 1:
		print('Senha encontrada no arquivo recebido!')
	else:
		print('Senha não encontrada no arquivo recebido!')
	
def verificarNoArquivoGerado():
	 gerarNovasPalavras()
	 
	 retorno = verificarArquivo('wordlist.txt')
	 
	 if retorno == 1:
		print('Senha encontrada no arquivo gerado!')
	 else:
		print('Senha não encontrada no arquivo gerado!')
	 
	 
def verificarArquivo(caminho):
	arquivo = open(caminho, 'r')
	hashSenhaPrincipal = getHashSenhaASerProcurada()
	print(hashSenhaPrincipal)
	
	
	for palavra in arquivo:
		hashPalavra = geraHashTexto(palavra)
		if hashPalavra == hashSenhaPrincipal:
			return 1
	
	return 0
	
	
	


def main():
	#verificarNoArquivoGerado()
	verificarNoArquivoRecebido()
	return 0
 

if __name__ == '__main__' :
    main()
