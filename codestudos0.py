
ling = input('Digite a sua linguagem de programação')
num = input('Digite um numero')
nome = input('Qual é o seu nome?')
dia = input('Qual dia voce nasceu?')
mes = str (input('Qual mes voce nasceu?'))
ano = input('Qual ano voce nasceu?')
primeiro_num = int (input('Digite um número'))
segundo_num = float (input('Digite mais um número'))
soma = (primeiro_num) + (segundo_num)
n = input('Digite algo')

print(f'Hello Mundo!')
print(f'Voce nasceu no dia {dia} de {mes} de {ano}. correto?')
print(f'Seja bem vindo {nome} Prazer te conhecer')
print(f'A soma desses números é {soma}')
print(f"Olá {nome}! seja bem vindo a sua primeira aula de programação e parabéns pelo seu primeiro Hello World :) Sua linguagem de programação é {ling} seu numero digitado foi {num}")
print('Possui letras maisculas?', n.isupper()) #Se a palavra possui apenas letras maiusculas
print('Possui apenas letras?', n.isalpha()) #Se ele é apenas letras
print('Possui apenas numeros?', n.isnumeric()) #Se contem apenas numeros
print('Possui letras e numeros?', n.isalnum()) #Se contem letras e numeros

#Soma, divisão, multiplicação e divisão inteira de numeros inteiros

n1 = int (input('Digite um valor'))
n2 = int (input('Digite outro valor'))
s = n1 + n2 #Soma dos valores
d = n1 / n2 #Divisão dos valores
m = n1 * n2 #Mutiplicação
di = n1 // n2 #Divisão inteira

print(f'A soma dos valores é {s}\nA divisão é {d:.2f}\nA mutiplicação é {m}\nA divisão inteira seria {di}') # \n funciona como quebra de linhas

#Lendo um numero inteiro e mostrando na tela seu antecessor e seu sucessor

n = int (input('Digite um numero inteiro: '))
print(f'Analisando o valor de {n}, seu antecessor é {n-1} e o seu sucessor é {n+1}') 

#Dobro, triplo e raiz quadrada

n1 = int (input('Digite um numero: '))
print(f'O dobro de {n1} é {n1*2} \nO triplo de {n1} é {n1*3} \nA raiz quadrada de {n1} é {n1**(1/2):.2f}')

#Passo a passo
#Passo 1: Saber a nota do aluno
#Passo 2: Saber numeros de falta do aluno

nota = float (input('Digite sua nota'))
faltas = float (input('Informe a quantidade de faltas'))
#Se a nota for maior ou igual a 7 e o aluno tiver menos que 5 faltas aluno aprovado senão esta reprovado
if nota >=7 and faltas <=5:
  print('Aprovado')
elif nota <7 and faltas >=6:
  print('reprovado')

#Média Aritmética

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = float (nota1 + nota2) / 2
print(f'A media entre {nota1} e {nota2} é {media:.1f}')

#Conversor de Medidas em cm e mm 

medida = float(input('Digite uma distancia em metros: '))

cm = medida * 100
mm = medida * 1000
dm = medida * 10
hm = medida * 0.1
km = medida * 0.001
dam = medida * 0.1

print(f'{cm} cm')
print(f'{mm} mm') n
print(f'{dm} dm')
print(f'{hm:.3} hm')
print(f'{km} km')
print(f'{dam:.0} dam')

#Tabuada
# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um numero: '))

print(f'-'*12)
print(f'{num} x 1 = {num*1}')
print(f'{num} x 2 = {num*2}')
print(f'{num} x 3 = {num*3}')
print(f'{num} x 4 = {num*4}')
print(f'{num} x 5 = {num*5}')
print(f'{num} x 6 = {num*6}')
print(f'{num} x 7 = {num*7}')
print(f'{num} x 8 = {num*8}')
print(f'{num} x 9 = {num*9}')
print(f'{num} x 10 = {num*10}')
print(f'-'*12)

#Conversor de Moedas
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

cart = float(input('Quando dinheiro voce tem na carteira? R$'))
dolar = cart / 5.25
euro = cart / 5.66
pesoarg = cart / 0.026

print(f'Voce pode comprar {dolar:.2f} US')
print(f'Voce pode comprar {euro:.2f} EURO')
print(f'Voce pode comprar {pesoarg:.2f} Peso Argentino')

#Pintando Parede
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

alt = float(input('Informe a altura da parede: '))
larg = float(input('Informe a largura da parede: '))
area = alt * larg

print(f'Sua parede tem a dimensão de {alt}x{larg} e sua área é de {area}m²')
tinta = area / 2
print(f'Para pintar essa parede voce vai precisar de {tinta}L de tinta')

#Calculando Descontos
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Informe o preço do produto: R$'))
novo = preço - (preço * 5 / 100)
valprazo = preço + (preço * 4 / 100)
print(f'O produto que custava R${preço} com 5% de desconto na venda a vista vai custar R${novo:.2f} e venda a prazo vai custa R${valprazo:.2f} ')

#Reajuste Salarial
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o seu salario? R$'))
salnovo = salario + (salario * 15 / 100)

print(f'Seu salario atualmente é de R${salario} com o reajuste seu salario é de R${salnovo}')

#Conversor de Temperaturas
#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite a temperatura em graus celsius °c: '))
f = 9 * c / 5 + 32
print(f'{c}°C convertido em {f}°F')

#Aluguel de Carros
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quanto km voce percorreu? '))
dias = int(input('Por quantos dias ele foi alugado? '))
pcarro = (dias * 60) + (dias * 0.15)

print(f'O total a pagar é de {pcarro}')

import math

num = int(input('Digite um numero? '))
raiz = math.sqrt (num)
raiz_arredondada = round(raiz, 2)

print(f'A raiz quadrada de {num} é {raiz_arredondada}')

#Quebrando um número
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
from math import trunc 
num = float(input('Digite um valor: '))
print('O numero digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))

texto = 'Aprendendo Python na disciplina de Linguagem de programação'

print(f'Tamanho do texto = {len(texto)}') # O operador "len" ler a quantidade de letras do texto
print(f'Python in texto = {"Python" in texto}') # O operador "in", por sua vez permite saber se um valor esta ou não na sequência
print(f'Quantidade de y no texto = {texto.count("y")}') # O operador ".count" permite contar a quantidade de ocorrencia de um valor
print(f'As cincos primeiras letras são = {texto[0:6]}') # O operador "[0:6]" permite fatiar a sequência, exibindo apenas partes dela

vogais = ['a','e','i','o','u']

for vogal in vogais:
  print(f'Posição = {vogais.index(vogal)}, valor {vogal}')

texto = 'Aprendendo Python na disciplina de Linguagem de programação'

print(f'texto = {texto}')
print(f'Tamanho do texto = {len(texto)}')

palavras = texto.split() # Função usada para "cortar" um texto e transformar ele em uma lista 

print(f'Palavras = {palavras}')
print(f'Tamanho de palavras = {len(palavras)}')

linguagem = ['PYTHON','GO','JAVA','C#','C++','KOTLIN']

print(f'Antes do Liscomp = {linguagem}')

linguagem = [item.lower() for item in linguagem] #A função 'item.lower' transforma o texto em letras minusculas

print(f'\nDepois do Liscomp = {linguagem}')

#Catetos e Hipotenusa
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = hypot (co,ca) #Função 'hypot' calcula a hipotenusa

print(f'O comprimento da hipotenusa é {hi:.2f}')

#Sorteando um item na lista
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
n5 = str(input('Digte quinto nome: '))
lista = [n1, n2, n3, n4, n5]
escolhido = choice(lista) #Função 'random.choice' escolhe um texto aleatorio 

print(f'O nome escolhido foi {escolhido}')

#Sorteando uma ordem na lista
#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

aluno1 = str(input('Digite o primeiro nome: '))
aluno2 = str(input('Digite o segundo nome: '))
aluno3 = str(input('Digite o terceiro nome: '))
aluno4 = str(input('Digite o quarto nome: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print(f'A ordem de apresentação será: ')
print(lista)

#Tocando um MP3
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

frase = 'Curso em video python'
len(frase) # Função len mostra o comprimento da frase
frase.count('o') # Função count mostra a quantidade de letras 
frase.find('deo') # Função find encontra a string informada e diz sua posição
frase.find('Android') # Caso não tenha essa string na variavel ele retorna o valor -1
'Curso' in frase # Operador in tem como objetivo booleano informar se existe determinada string na variavel frase
frase.replace('python','android') # Replace tem como função troca uma string por outra
frase.upper() # Transforma as letras minusculas em maiusculas
frase.lower() # Transforma as letras maiusculas em minusculas
frase.capitalize() # Transforma a frase toda para minuscula exeto a primeira letra 
frase.title() # Transforma as frase apos os espaços para maiusculo
frase.strip() # remove todos os espaços inuteis do inicio e fim da frase
frase.rstrip() # remove os espaço inuteis da direita
frase.lstrip() # remove os espaço inuteis da esquerda
frase.split()
'-'.join(frase)
print(frase[1:13:2])
print("""O Python possui apenas um tipo de objeto de módulo e todos os módulos são desse tipo, 
independentemente de o módulo estar implementado em Python, C ou qualquer outra coisa. 
Para ajudar a organizar os módulos e fornecer uma hierarquia de nomes, o Python tem o conceito de pacotes.""")

time.sleep(5)
print(pyautogui.position())

# Passo 5: Acessar Chat Do suporte
#Abrir uma nova aba

pyautogui.hotkey("ctrl","t")

#Informar o link do site
time.sleep(5)
pyautogui.write("www.smsolucoesdigital.com.br/")

#Precionar enter para entrar no site
time.sleep(5)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=1634, y=748)
time.sleep(5)
pyautogui.click(x=77, y=216)
time.sleep(5)
pyautogui.click(x=143, y=329)
time.sleep(5)
pyautogui.press("F11")

class ClassAnimal:
  def imprimir_mensagem(self, nome):
    print(f'Ola {nome}, seja bem vindo')
    objeto1 = ClassAnimal()
    objeto1.imprimir_mensagem('Ryan')

#programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome ').strip())
print('Analisando seu nome...')
print('Seu nome é {}'.format(nome))
print('Seu nome maiuscula é {}'.format(nome.upper()))
print('Seu nome minuscula é {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome possui {} letras'.format(nome.find(' ')))
