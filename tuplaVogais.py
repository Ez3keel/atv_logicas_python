palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras:
  print('\n Palavras: {} . Vogais: ' .format(palavra.upper()), end = '')
  for letra in palavra:
    if letra.lower() in 'aeiou':
      print(letra.upper() , end = ' ')