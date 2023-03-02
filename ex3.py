#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
poema = 'Eu hoje fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo / Por isso eu fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo'

poema2 = 'Por isso eu fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Isso me deixa triste e cabisbaixo'

print("EX -- 3.1 A)")
def ex31a(a):
  b = a.split(" / ")

  print(b[4])
  print(b[5])

ex31a(poema)

print("EX -- 3.1 B)")
def ex31b(a):
  b = a.replace(" / ","\n")
  print(b)

ex31b(poema)

print("EX -- 3.1 C)")

def ex31c(a,b):
  c = a.split(" / ")
  d = b.split(" / ")
  e = c + d
  for frase in e:
    print(frase)

ex31c(poema,poema2)

print("EX -- 3.1 D)")

def ex31d(a,b):
  c = a.split(" / ")
  d = b.split(" / ")
  e = c + d
  print(e[-1])
  print(e[-2])

ex31d(poema,poema2)

print("EX -- 3.2 A)")

def ex32a(a):
  letraA="aA"
  letraE="eE"
  letraI="iI"
  letraO="oO"
  letraU="uU"
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

  print("No total existem "+ str(contadorA+contadorE+contadorI+contadorO+contadorU) + " vogais")

  print("\n")

  print("A--->" + str(contadorA))
  print("E--->" + str(contadorE))
  print("I--->" + str(contadorI))
  print("O--->" + str(contadorO))
  print("U--->" + str(contadorU))

  numvogalfreq = max(contadorA,contadorE,contadorI,contadorO,contadorU)

  acontecimentos={"a" : contadorA,"e":contadorE,"i":contadorI,"o":contadorO,"u":contadorU}

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

  vogal_mais_utilizada = [vogal for vogal,ocorrencias in acontecimentos.items() if ocorrencias == numvogalfreq]
  if len(vogal_mais_utilizada) == 1:
    print(f"A vogal mais utilizada é '{vogal_mais_utilizada[0]}' com {numvogalfreq}")
  else:
    print("As vogais mais utilizadas são:")
    for vogal in vogal_mais_utilizada:
      print(vogal)



ex32a(poema)

print("EX -- 3.3")

def bubble_sort(lista):
  n = len(lista)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]


lista = [64, 34, 25, 12,43, 22, 11, 90,108]

print(f"Lista inicial:{lista}")

bubble_sort(lista)
print("Sorting...")

print(f"Lista final:{lista}")











