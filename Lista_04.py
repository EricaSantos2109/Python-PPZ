#Entrega de exercicios lista 4

#lista 4
#Sorteie 10 números inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.

from random import randint

numeros = []
for i in range(10):
    numero = randint(1, 100)
    numeros.append(numero)
print(f'números sorteados: { numeros }')
max_numero = numeros[0]
min_numero = numeros[0]
for numero in numeros:
    if numero > max_numero:
        max_numero = numero
    if numero < min_numero:
        min_numero = numero
print(f'maior número: { max_numero }\menor número: { min_numero }')

# 05 - Seja o mesmo texto acima 'splitado'. Calcule quantas palavras possuem uma das
#      letras "python" e que tenham mais de 4 characteres. Não se esqueça de
#      transformar maiúsculas para minúsculas e de remover antes o characteres
#      especiais.

text = '''
    The Python Software Foundation and the global Python community welcome and encourage
    participation by everyone. Our community is based on mutual respect, tolerance, and
    encouragement, and we are working to help each other live up to these principles.
    We want our community to be more diverse: whoever you are, and whatever your
    background, we welcome you.
'''
for special_character in ['\n', '.', ':', ',']:
    text = text.replace(special_character, '')
words = text.split(' ')
words_selected = []
for word in words:
    if len(word) <= 4:
        continue
    match = ('p', 'y', 't', 'h', 'o', 'n')
    word_lower = word.lower()
    if word_lower.startswith(match) or word_lower.endswith(match):
        words_selected.append(word)
print(f'{ len(words_selected) } palavras')

# 03 - Faça um programa que crie 2 vetores com 10 elementos aleatórios entre 1
#      e 100. Gere um terceiro vetor de 20 elementos, cujo os valores deverão
#      ser compostos pelos elementos intercalados dos dois  outros vetores.
#      Imprima os 3 vetôres.

from random import randint

vector_one = []
vector_two = []
vector_three = []
for i in range(10):
    number_one = randint(1, 100)
    number_two = randint(1, 100)
    vector_one.append(number_one)
    vector_two.append(number_two)
    vector_three.append(number_one)
    vector_three.append(number_two)
print(f'vetor 1: { vector_one }\nvetor 2: { vector_two }\nvetor 3: { vector_three }')


# 04 - Seja o statement sobre diversidade: "The Python Software Foundation and the global
#      Python community welcome and encourage participation by everyone. Our community
#      is based on mutual respect, tolerance, and encouragement, and we are working
#      to help each other live up to these principles. We want our community to be more
#      diverse: whoever you are, and whatever your background, we welcome you.".
#      Gere uma lista de palavras deste texto com split(), a seguir crie uma lista
#      com as palavras que começam ou terminam com uma das letras "python". Imprima
#      a lista resultante. Não se esqueça de remover antes os caracteres especiais
#      e cuidado com maiúsculas e minúsculas.

text = '''
    The Python Software Foundation and the global Python community welcome and encourage
    participation by everyone. Our community is based on mutual respect, tolerance, and
    encouragement, and we are working to help each other live up to these principles.
    We want our community to be more diverse: whoever you are, and whatever your
    background, we welcome you.
'''
for special_character in ['\n', '.', ':', ',']:
    text = text.replace(special_character, '')
words = text.split(' ')
words_selected = []
for word in words:
    match = ('p', 'y', 't', 'h', 'o', 'n')
    word_lower = word.lower()
    if word_lower.startswith(match) or word_lower.endswith(match):
        words_selected.append(word)
print(words_selected)

# 02 - Sorteie 20 números inteiros entre 1 e 100 numa lista. Armazene os números pares
#      na lista par e os númeors impares na lista impar. Imprima as 3 listas

from random import randint

numbers = []
odd = []
even = []
for i in range(10):
    number = randint(1, 100)
    numbers.append(number)
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(f'números: { numbers }\nimpares: { odd }\npares: { even }')

