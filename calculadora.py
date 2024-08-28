
#Uma classe para representar uma calculadora.

#Possui as seguintes propriedades:
  # - num1: O primeiro número da operação.
  #- num2: O segundo número da operação.
  #- resultado: O resultado da operação.


class calculadora:
  def __inint__(self):  #Construtor da classe Calculadora.
    self.num1 = 0
    self.num2 = 0
    self.resultado = 0
  #Assim define as propriedades num1, num2 e resultado para 0.

  def somar(self, num1, num2): #- somar(num1, num2): Soma dois números.
    self.num1 = num1
    self.num2 = num2
    self.resultado = self.num1 + self.num2
    return self.resultado

  def subtrair(self, num1, num2): #    - subtrair(num1, num2): Subtrai dois números.
    self.num1 = num1
    self.num2 = num2
    self.resultado = self.num1 - self.num2
    return self.resultado

  def multiplicar(self, num1, num2): #    - multiplicar(num1, num2): Multiplica dois números.
    self.num1 = num1
    self.num2 = num2
    self.resultado = self.num1 * self.num2
    return self.resultado

  def dividir(self, num1, num2):        #    - dividir(num1, num2): Divide dois números.
    self.num1 = num1
    self.num2 = num2
    self.resultado = self.num1 / self.num2
    return self.resultado

  def expoente(self, num1, num2): # - expoente(num1, num2): Calcula a exponenciação de dois números
    self.num1 = num1
    self.num2 = num2
    self.resultado = self.num1 ** self.num2
    return self.resultado

  def resto(self, num1, num2):   #- resto(num1, num2): Calcula o resto da divisão de dois números.
    self.num1 = num1
    self.num2 = num2
    self.resultado = self.num1 % self.num2
    return self.resultado

def continuar(entrada): #Verifica se o usuário deseja continuar a usar a calculadora
  if entrada:
    return True
  else:
    return False

def menu(): #  """Exibe o menu da calculadora e solicita a entrada do usuário.
  #opc é as opções de calculo
  opc = {1: 'Adição',
         2:'Subtração',
         3:'Multiplicação',
         4:'Divisão',
         5:'Exponenciação',
         6:'Módulo (resto)',}

  calc = calculadora()
  print("""Qual é a operação matemática desejada?
  1 --> Adição
  2 --> Subtração
  3 --> Multiplicação
  4 --> Divisão
  5 --> Exponenciação
  6 --> Módulo (resto)
  Digite o número desejado e aperte ENTER""")
  calcular = True
  while calcular:
    opcao = input("\nEscolha a opção de cálculo desejada (1,2,3,4,5,6)")
    if not(opcao in '1 2 3 4 5 6'):
      print("Opção escolhida é inválida!")
      continue
    else:
      opcao = int(opcao)
      print(f"A operação matemática escolhida é {opc[opcao]}")
      print("Apenas número inteiros serão trabalhados!!!")
    if opcao == 1:  #Se digitar 1 vai calcular a soma
      num1 = int(input("Digite o penúltimo número de seu RU:"))
      num2 = int(input("Digite o último número de seu RU:"))
      resultado = calc.somar(num1, num2)
      print(f"O valor da operação de adição é {resultado}.")
      calcular = continuar(input("Digite alguma coisa para continuar ou apertar ENTER para sair da calculadora."))

    elif opcao == 2: #Se digitar 2 vai calcular a subtração
      num1 = int(input("Digite o penúltimo número de seu RU:"))
      num2 = int(input("Digite o último número de seu RU:"))
      resultado = calc.subtrair(num1, num2)
      print(f"O valor da operação de subtração é {resultado}.")
      calcular = continuar(input("Digite alguma coisa para continuar ou apertar ENTER para sair da calculadora."))

    elif opcao == 3: #Se digitar 3 vai calcular a multiplicação
      num1 = int(input("Digite o penúltimo número de seu RU:"))
      num2 = int(input("Digite o último número de seu RU:"))
      resultado = calc.multiplicar(num1, num2)
      print(f"O valor da operação de multiplicação é {resultado}.")
      calcular = continuar(input("Digite alguma coisa para continuar ou apertar ENTER para sair da calculadora."))

    elif opcao == 4: #Se digitar 4 vai calcular a divisão
      num1 = int(input("Digite o penúltimo número de seu RU:"))
      num2 = int(input("Digite o último número de seu RU:"))
      resultado = calc.dividir(num1, num2)
      print(f"O valor da operação de divisão é {resultado}.")
      calcular = continuar(input("Digite alguma coisa para continuar ou apertar ENTER para sair da calculadora."))

    elif opcao == 5: #Se digitar 5 vai calcular a exponenciação
      num1 = int(input("Digite o penúltimo número de seu RU:"))
      num2 = int(input("Digite o último número de seu RU:"))
      resultado = calc.expoente(num1, num2)
      print(f"O valor da operação de expoenciação é {resultado}.")
      calcular = continuar(input("Digite alguma coisa para continuar ou apertar ENTER para sair da calculadora."))

    elif opcao == 6: ##Se digitar 6 vai calcular o resto
      num1 = int(input("Digite o penúltimo número de seu RU:"))
      num2 = int(input("Digite o último número de seu RU:"))
      resultado = calc.resto(num1, num2)
      print(f"O valor da operação de módulo(resto) é {resultado}.")
      calcular = continuar(input("Digite alguma coisa para continuar ou apertar ENTER para sair da calculadora."))
      print("Calculadora Encerrada!") #Encerra a calculadora


menu()
