#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import string
from collections import Counter

poema = 'Eu hoje fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo / Por isso eu fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo'

poema2 = 'Por isso eu fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Isso me deixa triste e cabisbaixo'

print("\nEX -- 3.1 A)")


def ex31a(a):
  b = a.split(" / ")

  print(b[4])
  print(b[5])


ex31a(poema)

print("\nEX -- 3.1 B)")


def ex31b(a):
  b = a.replace(" / ", "\n")
  print(b)


ex31b(poema)

print("EX -- 3.1 C)")


def ex31c(a, b):
  c = a.split(" / ")
  d = b.split(" / ")
  e = c + d
  for frase in e:
    print(frase)


ex31c(poema, poema2)

print("\nEX -- 3.1 D)")


def ex31d(a, b):
  c = a.split(" / ")
  d = b.split(" / ")
  e = c + d
  print(e[-1])
  print(e[-2])


ex31d(poema, poema2)

print("\nEX -- 3.2 A)")


def ex32a(a):
  letraA = "aA"
  letraE = "eE"
  letraI = "iI"
  letraO = "oO"
  letraU = "uU"
  contadorA = 0
  contadorE = 0
  contadorI = 0
  contadorO = 0
  contadorU = 0

  for letra in a:
    if letra in letraA:
      contadorA += 1
    if letra in letraE:
      contadorE += 1
    if letra in letraI:
      contadorI += 1
    if letra in letraO:
      contadorO += 1
    if letra in letraU:
      contadorU += 1

  print("No total existem " + str(contadorA + contadorE + contadorI + contadorO + contadorU) + " vogais")

  print("\n")

  print("A--->" + str(contadorA))
  print("E--->" + str(contadorE))
  print("I--->" + str(contadorI))
  print("O--->" + str(contadorO))
  print("U--->" + str(contadorU))

  numvogalfreq = max(contadorA, contadorE, contadorI, contadorO, contadorU)

  acontecimentos = {"a": contadorA, "e": contadorE, "i": contadorI, "o": contadorO, "u": contadorU}

  if contadorA == numvogalfreq:
    print("A vogal mais frequente é A")
  if contadorE == numvogalfreq:
    print("A vogal mais frequente é E")
  if contadorI == numvogalfreq:
    print("A vogal mais frequente é I")
  if contadorO == numvogalfreq:
    print("A vogal mais frequente é O")
  if contadorU == numvogalfreq:
    print("A vogal mais frequente é U")

  vogal_mais_utilizada = [vogal for vogal, ocorrencias in acontecimentos.items() if ocorrencias == numvogalfreq]
  if len(vogal_mais_utilizada) == 1:
    print(f"A vogal mais utilizada é '{vogal_mais_utilizada[0]}' com {numvogalfreq}")
  else:
    print("As vogais mais utilizadas são:")
    for vogal in vogal_mais_utilizada:
      print(vogal)


ex32a(poema)

print("\nEX -- 3.3")


def bubble_sort(lista):
  # steps:
  steps = 0
  n = len(lista)
  for i in range(n - 1):
    for j in range(n - i - 1): #n* log(n) steps
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
        steps += 1
  #total steps: worst case O = n**2

lista = [64, 34, 25, 12, 43, 22, 11, 90, 108]

print(f"Lista inicial:{lista}")

bubble_sort(lista)
print("Sorting...")

print(f"Lista final:{lista}")

print("\nEX -- 3.4")


def ee_transposta(string1, string2):
  for c in string1:
    string2 = string2.replace(c, '') # 2 steps
    print(string2)
  if string2 == "":
    return True
  return False
  # O = 2n


string1 = "roma"
string2 = "amor"


# print(string2)
# print(ee_transposta(string1, string2))

def equal_strings(str1, str2):
  # O = 2n^2
  lst1 = [str1[i] for i in range(0, len(str1))]
  lst2 = [str2[i] for i in range(0, len(str2))]
  bubble_sort(lst1)
  bubble_sort(lst2)
  if lst1 == lst2 :
    return True
  return False

# print(equal_strings(string1, string2)) #7 PASSOS- falta cronometrar o tempo

def transposed_combinations(word):
  transposed = set()
  transposed.add(word)

  for i in range(len(word)):
    for j in range(i + 1, len(word)):
      transposed_word = list(word)
      transposed_word[i], transposed_word[j] = transposed_word[j], transposed_word[i]
      transposed.add("".join(transposed_word))

      for t in list(transposed):
        transposed_t = list(t)
        transposed_t[i], transposed_t[j] = transposed_t[j], transposed_t[i]
        transposed.add("".join(transposed_t))

  transposed = sorted(list(transposed))
  return transposed

word = "roma"
transposed = transposed_combinations(word)
print(transposed)

def count_chars(word1, word2):
  count1 = Counter(word1)
  count2 = Counter(word2)
  alphabet = string.ascii_letters
  for c in alphabet:
    if count1[c] != count2[c]:
      return False
  print(f"as palavras {word1} e {word2} têm o mesmo numero de caracters iguais")
  return True
  #contar char

count_chars("roma", "amor")

