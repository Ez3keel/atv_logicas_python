#Ezequiel Gonçalves
# Ru: 3950764

# Definição da classe Nodo, que representa um cartão numerado contendo: número, cor e um ponteiro para o próximo nodo
class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

# Definição da classe ListaEncadeada, que contém um ponteiro para a cabeça da lista (head)
class ListaEncadeada:
    def __init__(self):
        self.head = None

    # Função para inserir um nodo no final da lista (sem prioridade)
    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    # Função para inserir um nodo com prioridade (após todos os nodos de cor "A")
    def inserirComPrioridade(self, nodo):
        if not self.head or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    # Função para inserir um nodo na lista baseado na cor e no número fornecidos pelo usuário
    def inserir(self):
        cor = input("Digite a cor do cartão (A ou V): ").upper()
        numero = int(input("Digite o número do cartão: "))
        print("\n")
        novo_nodo = Nodo(numero, cor)

        if not self.head:
            self.head = novo_nodo
        elif cor == 'V':
            self.inserirSemPrioridade(novo_nodo)
        elif cor == 'A':
            self.inserirComPrioridade(novo_nodo)

    # Função para imprimir todos os cartões na lista de espera
    def imprimirListaEspera(self):
        atual = self.head
        while atual:
            print(f"Cartão: {atual.numero}, Cor: {atual.cor}")
            print("\n")
            atual = atual.proximo

    # Função para atender (remover) o primeiro paciente da lista
    def atenderPaciente(self):
        if not self.head:
            print("Nenhum paciente na fila de espera.")
        else:
            print(f"Chamando paciente com cartão: {self.head.numero}")
            self.head = self.head.proximo

# Função para exibir o menu e gerenciar as opções do sistema
def menu():
    lista = ListaEncadeada()

    while True:
        print("Menu:")
        print("1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
            print("\n")
        except ValueError:
            print("Opção inválida. Tente novamente.")
            continue

        if opcao == 1:
            lista.inserir()
        elif opcao == 2:
            lista.imprimirListaEspera()
        elif opcao == 3:
            lista.atenderPaciente()
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")

# Teste do sistema conforme as instruções fornecidas
def teste():
    lista = ListaEncadeada()

    # Inserção dos pacientes na ordem especificada
    pacientes = [('V', 1), ('V', 2), ('V', 3), ('A', 201), ('A', 202), ('V', 4), ('V', 5), ('A', 203), ('A', 204), ('A', 205)]
    for cor, numero in pacientes:
        novo_nodo = Nodo(numero, cor)
        if cor == 'V':
            lista.inserirSemPrioridade(novo_nodo)
        else:
            lista.inserirComPrioridade(novo_nodo)

    # Impressão da lista de espera
    print("Lista de espera inicial:")
    lista.imprimirListaEspera()

    # Atendimento de dois pacientes e impressão da lista de espera
    print("\nAtendimento de dois pacientes:")
    lista.atenderPaciente()
    lista.atenderPaciente()
    print("\nLista de espera após atendimento de dois pacientes:")
    lista.imprimirListaEspera()

# Execução dos testes
#teste()
menu()
