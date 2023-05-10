from sklearn.tree import DecisionTreeClassifier

lisa = 'lisa'
irregular = 'irregular'
pera = 'pera'
laranja = 'laranja'

pomar = [[120, lisa], [140, lisa], [160, irregular], [200, irregular]]
resultado = [pera, pera, laranja, laranja]

clf = DecisionTreeClassifier()
clf = clf.fit(pomar, resultado)

peso = 220
superficie = irregular
resultadousu = clf.predict([[peso, superficie]])

if resultadousu == pera:
    print('pera')
else:
    print('laranja')