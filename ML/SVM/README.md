# Taller SVM
1. Seleccionar 1 dataset
2. Evaluar un clasificador SVM que utilice diferentes kernels (RBF, Polinomial, Lineal, Sigmoidal ) con diferentes hiper-parámetros de configuración del kernel.
3. Sacar conclusiones

## Desarrollo
Completo en [svm.py](./svm.py)

## Dataset
[Stack Overflow Survey 2021](https://insights.stackoverflow.com/survey/2021?_ga=2.236209345.190202062.1628102352-126161871.1625855113)

## Clasificador
```python
gammas = [0.001, 0.005, 0.01, 0.1]
Cs = [1, 0.1, 0.001, 2]
kernels = ['rbf', 'linear', 'poly', 'sigmoid']

def run_clasiffer(g, penalty, kernel='rbf'):
    try:
        x = df[['k1', 'k2', 'k3']]
        y = df['age']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)
        #x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target)

        clf = SVC(gamma=g, C=penalty, kernel=kernel)

        print(clf.kernel)

        clf.fit(x_train, y_train)
        clf.score(x_train, y_train)

        clf.score(x_test, y_test)

        clf.predict(df.values.tolist()[-1:])


        plt.figure(1, figsize=(3, 3))
        plt.imshow(df.values.tolist()[-1:], cmap=plt.cm.gray_r, interpolation='nearest')

        plt.savefig(fname='./{}/svm_{}.png'.format(kernel, kernel))
    except Exception as e:
        print("error with kernel: {}, gamma: {}, C:{}".format(kernel, g, penalty))
        print("error descp: {}".format(e))

for i in range(0, len(kernels)):
    run_clasiffer(gammas[i], Cs[i], kernels[i])
```

## Conclusiones
1. Hiperparametros muy elevados no predicen correctamente, la diferencia suele ser mayor al 40% (en este caso)
2. El score por otro lado, dio buenos resultados con un 'C' 2 (digamos alto), con valores de 10 no fueron buenos resultados
3. LA mejor clasificacion fue la sigm
