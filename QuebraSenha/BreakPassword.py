#coding utf-8
import hashlib
import time

'''
Gera o hash do arquivo. O hash do arquivo é um hash MD5.
'''
def geraHash (caminhoArquivo):
	hash = hashlib.md5()
	arquivo = open(caminhoArquivo, 'rb')
	hash.update(arquivo.read())
	arquivo.close()
	return hash.hexdigest()


def geraHashTexto(texto):
    hash = hashlib.md5()
    hash.update(texto.encode('utf-8'))
    return hash.hexdigest()



def main():
    hashSenha = geraHash('senha.txt')
    wordList = open('wordlista', 'r')

    for x in wordList:
        hashSenhaLida = geraHashTexto(x)
        if hashSenhaLida == hashSenha:
            print('Senha quebrada!\nA senha é %s' % x)
            break
            return 1

    wordList.close()
    return 0

if __name__ == '__main__':
    inicio  = time.time()
    retorno = main()
    fim = time.time()
    if retorno == 1:
        print('Tempo gasto: {} segundo(s)'.format(fim - inicio))
    else:
        print('Senha não encontrada na lista!')
