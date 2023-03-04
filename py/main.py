class Number:
  def __init__(self, left, right):
    self.left = left
    self.right = right


poema = "Eu hoje fiz um samba bem prafrente / Dizendo realmente o que é que euacho / Eu acho que o meu samba é umacorrente / E coerentemente assino embaixo/ Hoje é preciso refletir um pouco / E verque o samba está tomando jeito / Só mesmoembriagado ou muito louco / Pra contestare pra botar defeito / Precisa ser muitosincero e claro / Pra confessar que andeisambando errado / Talvez precise até tomarna cara / Pra ver que o samba está bemmelhorado / Tem mais é que ser bem cara detacho / Não ver a multidão sambar contente/ Isso me deixa triste e cabisbaixo / Porisso eu fiz um samba bem pra frente /Dizendo realmente o que é que eu acho / Euacho que o meu samba é uma corrente / Ecoerentemente assino embaixo / Hoje épreciso refletir um pouco / E ver que osamba está tomando jeito / Só mesmoembriagado ou muito louco / Pra contestare pra botar defeito / Precisa ser muitosincero e claro / Pra confessar que andeisambando errado / Talvez precise até tomarna cara / Pra ver que o samba está bemmelhorado / Tem mais é que ser bem cara detacho / Não ver a multidão sambar contente/ Isso me deixa triste e cabisbaixo "

l = poema.split(' / ')

def main():
  number = Number(3,2) # criar instancia de uma Classe denominada Number
  print('3 + 2 = ', number.left + number.right)

  word = 'Hello World'
  print(word[:5])  # seperar uma palavra 'word' desde o caracter 0 ao 4 (excluindo o 5º)
  print(word[-5:])  # print de uma parte de 'word' desde o 5º caracter a contar do fim até ao fim da palavra
  word2 = word[-5:]

  # print caracter a caracter da segunda palavra utilizando o 'for'
  for c in word2:
    print(c)

  print(poema, "\n")
  print(l[4])
  print(l[5])

if __name__ == '__main__':
  main()



