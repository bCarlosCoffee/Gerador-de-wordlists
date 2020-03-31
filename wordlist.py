#! -*- coding:utf-8 -*-
# ~> CarlosCoffee


from sys import argv, exit
from random import randint
from os import path

teste = argv # Argumentos de entrada!
senhas_criadas = [] # Senhas que serão criadas

# Senhas predefinidas
poss = ['12345678','um2345678','1dois345678','12tres45678','123quatro5678','1234cinco678','12345seis78','123456sete8','1234567oito',
		'1234567','um234567','1dois34567','12tres4567','123quatro567','1234cinco67','12345seis7','123456sete','1234567','987654321','87654321']


def mododeusar():
	"""
	Função chamanda quando ocorre um erro.
	"""

	print("[!--------------- Modo de uso ---------------------!]\n")
	print("python3 word.py [ Número de voltas que o script irá fazer ] [ argumentos ]")
	print("Não precisa usar os seguintes caracteres como argumento [  @  e  _ ] o programa já adiciona por padrão!") 
	print("\n[!] Podes usar até quatro chaves!\n")
	print("Exemplo de uso: ")
	print("[ Exemplo 1 ] ~> python3 word.py 50 teste 60 ")
	print("[ Exemplo 2 ] ~> python3 word.py 300 teste 1234 python ")
	print("[ Exemplo 3 ] ~> python3 word.py 200 teste coffee 1234 code \n")
	print("\n< ! Recomendado usar letras minusculas porque o programa vai")
	print("passar para maiusculas na hora da execucao do programa !>\n")
	print("( Aguarde ) irá começar a gerar as senhas....")
	print("\n\n ~~~~~ CarlosCoffee ~~~~~\n\n")
	exit()


def verifica(key):
	"""
	Verifica se a palavra(key) está dentro de senhas criadas, se estiver retorna False, caso contrario adiciona a palavra para lista(senhas criadas)
	Depois verifica se a palavra é um número, se não for adiciona a palavra novamente em upper()
	Depois Verifica se a primeira posicao da palavra é aplha se for adiciona a palavra novamente em capitalize()

	"""
	if key in senhas_criadas: return False
	else:
		senhas_criadas.append(key)
		print(key)

		if key.isnumeric() == False:
			senhas_criadas.append(key.upper())
			print(key.upper())
		
		if key[0].isalpha() == True:
			senhas_criadas.append(key.capitalize())
			print(key.capitalize())


if len(teste[::2]) < 2: # Nescessario o primeiro argumento! > python3 word.py ('5')
	mododeusar()
	exit()
else:
	quantidade = teste[1] # define a quantidade de voltas  que o loop vai dá!
	contador = 0 # Conta quantas voltas já foram dadas

print("[!] Gerando senhas...")
print("[!] Verifique se não já existe um arquivo chamado 'wordlist.txt'!\n\n")
[verifica(add) for add in argv[2::]]
[verifica(add) for add in poss] # Percorre as senhas pré definidas e chama verifica cada palavra.

while True:
	try:
		contador += 1
		# Escolher um numero, detro da quantidade de argumentos de teste e adicionar como palavra, misturando
		# Criando varias possibilidades de senhas e adicionar em senhas_criadas

		if len(teste[2::]) == 2:
			c1 = randint(2, len(teste[1::])) # Seleciona uma posicao aleatoria
			c2 = randint(2, len(teste[1::]))

			# Junta as palavras em variaveis de forma misturada.
			palavra1 = str(teste[c1]) + str(teste[c2])
			palavra2 = str(teste[c1]) + "_" + str(teste[c2])
			palavra3 = str(teste[c1]) + "@" + str(teste[c2])

			# ! Acontece o mesmo com o restante abaixo

		elif len(teste[2::]) == 3:
			c1 = randint(2, len(teste[1::]))
			c2 = randint(2, len(teste[1::]))
			c3 = randint(2, len(teste[1::]))

			palavra1 = str(teste[c1]) + str(teste[c2])
			palavra2 = str(teste[c1]) + "_" + str(teste[c2])
			palavra3 = str(teste[c1]) + "@" + str(teste[c2])
			palavra4 = str(teste[c1]) + str(teste[c2]) + str(teste[c3])
			palavra5 = str(teste[c1]) + "_" + str(teste[c2]) + str(teste[c3])
			palavra6 = str(teste[c1]) + "_" + str(teste[c2]) + "_" + str(teste[c3])
			palavra7 = str(teste[c1]) + str(teste[c2]) + "_" + str(teste[c3])
			palavra8 = str(teste[c1]) + "@" + str(teste[c2]) + str(teste[c3])
			palavra9 = str(teste[c1]) + "@" + str(teste[c2]) + "@" + str(teste[c3])
			palavra10 = str(teste[c1]) + str(teste[c2]) + "@" + str(teste[c3])
		
		elif len(teste[2::]) == 4:
			c1 = randint(2, len(teste[1::]))
			c2 = randint(2, len(teste[1::]))
			c3 = randint(2, len(teste[1::]))
			c4 = randint(2, len(teste[1::]))

			palavra1 = str(teste[c1]) + str(teste[c2])
			palavra2 = str(teste[c1]) + "_" + str(teste[c2])
			palavra3 = str(teste[c1]) + "@" + str(teste[c2])
			palavra4 = str(teste[c1]) + str(teste[c2]) + str(teste[c3])
			palavra5 = str(teste[c1]) + "_" + str(teste[c2]) + str(teste[c3])
			palavra6 = str(teste[c1]) + "_" + str(teste[c2]) + "_" + str(teste[c3])
			palavra7 = str(teste[c1]) + str(teste[c2]) + "_" + str(teste[c3])
			palavra8 = str(teste[c1]) + "@" + str(teste[c2]) + str(teste[c3])
			palavra9 = str(teste[c1]) + "@" + str(teste[c2]) + "@" + str(teste[c3])
			palavra10 = str(teste[c1]) + str(teste[c2]) + "@" + str(teste[c3])
			palavra11 = str(teste[c1]) + str(teste[c2]) + str(teste[c3]) + str(teste[c4])
			palavra12 = str(teste[c1]) + "_" + str(teste[c2]) + str(teste[c3]) + str(teste[c4])
			palavra13 = str(teste[c1]) + "_" + str(teste[c2]) + "_" + str(teste[c3]) + str(teste[c4])
			palavra14 = str(teste[c1]) + "_" + str(teste[c2]) + "_" + str(teste[c3]) + "_" + str(teste[c4])
			palavra15 = str(teste[c1]) + str(teste[c2]) + "_" + str(teste[c3]) + str(teste[c4])
			palavra16 = str(teste[c1]) + str(teste[c2]) + "_" + str(teste[c3]) + "_" + str(teste[c4])
			palavra17 = str(teste[c1]) + str(teste[c2]) + str(teste[c3]) + "_" + str(teste[c4])
			palavra18 = str(teste[c1]) + "@" + str(teste[c2]) + str(teste[c3]) + str(teste[c4])
			palavra19 = str(teste[c1]) + "@" + str(teste[c2]) + "@" + str(teste[c3]) + str(teste[c4])
			palavra20 = str(teste[c1]) + "@" + str(teste[c2]) + "@" + str(teste[c3]) + "@" + str(teste[c4])
			palavra21 = str(teste[c1]) + str(teste[c2]) + "@" + str(teste[c3]) + str(teste[c4])
			palavra22 = str(teste[c1]) + str(teste[c2]) + "@" + str(teste[c3]) + "@" + str(teste[c4])
			palavra23 = str(teste[c1]) + str(teste[c2]) + str(teste[c3]) + "@" + str(teste[c4])

		else:
			print("\n\n[ Ajuda ] Voce precisa pelo menos de 2 chaves...\n")
			input("...")
			mododeusar()

	except Exception as error:
		print(f"Erro: {error}")
		mododeusar()

	try:
		
		if len(teste[2::]) == 2:
			verifica(palavra1);verifica(palavra2);verifica(palavra3)

		if len(teste[2::]) == 3:
			verifica(palavra1);verifica(palavra2);verifica(palavra3);verifica(palavra4);verifica(palavra5);verifica(palavra6);verifica(palavra7);verifica(palavra8);verifica(palavra9);verifica(palavra10)
		
		if len(teste[2::]) == 4:
			verifica(palavra1);verifica(palavra2);verifica(palavra3);verifica(palavra4);verifica(palavra5);verifica(palavra6);verifica(palavra7);verifica(palavra8);verifica(palavra9);verifica(palavra10);verifica(palavra11);verifica(palavra12);verifica(palavra13);verifica(palavra14);verifica(palavra15);verifica(palavra16);verifica(palavra17);verifica(palavra18);verifica(palavra19);verifica(palavra20);verifica(palavra21);verifica(palavra22);verifica(palavra23)

	except Exception as erro:
		print(f"Erro: {erro}")
		exit()

	if int(contador) == int(quantidade): break

nome_do_arquivo = input("Nome do arquivo ~> ").strip()
if "." in nome_do_arquivo:
	nome_do_arquivo = nome_do_arquivo.split(".")[0]
	
if path.exists(f'{nome_do_arquivo}.txt') == True:
	print(f"O arquivo {nome_do_arquivo}.txt já existe!")
	exit()

else:
	print("[!] Salvando senhas no arquivo...")
	with open(f'{nome_do_arquivo}.txt', 'x') as arquivo:
		
		for palavra in senhas_criadas:arquivo.write(str(palavra)+"\n")
		
		print(f'\n\n\n\n\t{len(senhas_criadas)} Palavras Criadas :)\n\n')
		arquivo.close()


print("\t-------- Finalizado! --------\n\n")
