import random

# Função para gerar dados de treinamento
def gerar_dados(tamanho, uninter_ru):
    random.seed(42)  # Para reprodutibilidade
    ids = [random.randint(1, 2 * uninter_ru) for _ in range(tamanho)]
    labels = [1 if id > uninter_ru else -1 for id in ids]
    return ids, labels

# Implementação do Perceptron
class Perceptron:
    def __init__(self, learning_rate=0.1, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = []
        self.bias = 0

    def _step_function(self, x):
        return 1 if x >= 0 else -1

    def fit(self, X, y):
        n_samples = len(X)
        self.weights = [0.0] * len(X[0])
        self.bias = 0.0

        for _ in range(self.n_iters):
            for idx in range(n_samples):
                linear_output = sum(x_i * w_i for x_i, w_i in zip(X[idx], self.weights)) + self.bias
                y_predicted = self._step_function(linear_output)

                # Update weights and bias
                update = self.lr * (y[idx] - y_predicted)
                self.weights = [w_i + update * x_i for x_i, w_i in zip(X[idx], self.weights)]
                self.bias += update

    def predict(self, X):
        y_predicted = []
        for x_i in X:
            linear_output = sum(x_val * w_val for x_val, w_val in zip(x_i, self.weights)) + self.bias
            y_predicted.append(self._step_function(linear_output))
        return y_predicted

# RU de identificação
uninter_ru = 3950764

# Gerar dados de treinamento
ids, labels = gerar_dados(20, uninter_ru)

# Preparar os dados para treinamento
X_train = [[id] for id in ids]
y_train = labels

# Treinar o Perceptron
perceptron = Perceptron()
perceptron.fit(X_train, y_train)

# Testar o Perceptron
# Vamos gerar novos dados de teste
ids_teste, labels_teste = gerar_dados(10, uninter_ru)
X_teste = [[id] for id in ids_teste]
y_teste = labels_teste

# Prever e comparar com os labels verdadeiros
y_pred = perceptron.predict(X_teste)

# Imprimir resultados de forma mais legível
print("ID de Teste | Label Verdadeiro | Predição")
for id_teste, label_verdadeiro, predicao in zip(ids_teste, y_teste, y_pred):
    print(f"{id_teste:10d} | {label_verdadeiro:14d} | {predicao:8d}")
