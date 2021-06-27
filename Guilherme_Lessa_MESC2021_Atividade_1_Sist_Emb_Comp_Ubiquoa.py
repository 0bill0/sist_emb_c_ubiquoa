#coding: utf-8

"""
1 ) Desenvolva uma função em Python que retorne o número de palavras de uma string recebida como argumento. Para tanto, explore a função split().
Adicionais: carregue um texto de um arquivo para passar como parâmetro para a função do usuário. 

2 ) Faça uma função que, dado uma lista de strings, retorne uma lista com as strings ordenadas, exceto as strings que iniciam com ‘x’, as quais devem vir no início da lista retornada. Por exemplo: ['milho', 'xyz', 'amora', 'xicara', 'abacaxi'] resulta em: ['xicara', 'xyz', 'abacaxi', 'amora', 'milho']
Dica: crie duas listas, uma para palavras que iniciam com ‘x’ e outra não). Para cada palavra armazene na lista correspondente. Ao final, ordene cada lista e junte uma à outra. 

-- Palavras para validar questão 2 : xicara, xacara, xuxa, justiça, xenofobia 
"""

def word_counts(text): #questão 1
    text = text.split()
    return (text)

def ordena_palavras(lista_string):
	lista_iniciando_com_x = []
	lista_ordenada_exceto_iniciando_com_x = []
	sorted(lista_string)
	for palavra in lista_string:
		if palavra.lower().startswith("x"):
			lista_iniciando_com_x.append(palavra)
		else:
			lista_ordenada_exceto_iniciando_com_x.append(palavra.lower()) #ordenar, independente se a primeira letra é maiúscula ou minúscula

	lista_final = sorted(lista_iniciando_com_x) + sorted(lista_ordenada_exceto_iniciando_com_x)
	return lista_final

if __name__ == "__main__":
	text =  open('lista1.py','r')
	string = text.read()
	result = word_counts(string)
	print("Exercício 1 - O arquivo contém um total de",str(len(result))+" palavras.") #q1
	palavras_ordenadas = ordena_palavras(result) #q2
	#for palavra in palavras_ordenadas:
	#	print(palavra)
	#EN