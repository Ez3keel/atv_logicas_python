#Organizar de forma crescente, caso queira deixar em decrescente então colocar tam +1
def bubbleSort(dados):
  tam = len(dados);
  #aqui selecionado o quanto de vezes o loop vai iterar sobre dados start, stop, step.
  for v in range(0, tam, 1): #
      for i in range(0, tam - 1, 1):
        if dados[i] > dados[i + 1]:
          aux = dados[i]
          dados[i] = dados[i + 1]
          dados[i + 1] = aux


dados = [6, 5, 3, 1, 8, 7, 2, 4]
bubbleSort(dados)
print(dados);
