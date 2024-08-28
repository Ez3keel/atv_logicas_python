def eh_palindromo(palavra):
  """
  Função que verifica se uma palavra é um palíndromo.

  Argumentos:
    palavra: A palavra a ser verificada.

  Retorno:r
    True se a palavra for um palíndromo, False caso contrário.
  """
  palavra = palavra.lower()
  for i in range(len(palavra) // 2):
    if palavra[i] != palavra[len(palavra) - i - 1]:
      return False
  return True

pontos = 0

while True:
  palavra = input("Digite uma palavra: ")
  if eh_palindromo(palavra):
    print("Palíndromo! Você ganhou 100 pontos!")
    pontos += 100
  else:
    print("Não é um palíndromo. Você perdeu 50 pontos.")
    pontos -= 50
  print(f"Sua pontuação atual é: {pontos}")

  # Pergunte se o jogador deseja continuar
  continuar = input("Deseja continuar jogando? (Sim/Não) ")
  if continuar.lower() != "sim":
    break

print(f"Obrigado por jogar! Sua pontuação final foi: {pontos}")
