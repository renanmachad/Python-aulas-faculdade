from sklearn.datasets import load_iris,fetch_kddcup99
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,export_text,plot_tree
from sklearn.svm import SVC


######## Pré-processamento ##############
# Coleta e integração
iris = load_iris()

caracteristicas = iris.data
rotulos = iris.target

print(f'Características:\n {caracteristicas[:2]}')
print('Rotulos :\n ',rotulos[:2])
print('*'*10)
# partição dos dados
carac_treino,carac_teste,rot_treino,rot_teste= train_test_split(caracteristicas,rotulos)

###### Mineração ######
##### ´------ Árvore de decisão ----- #####
arvore = DecisionTreeClassifier(max_depth=5)
arvore.fit(X=carac_treino,y=rot_treino)

rot_preditos = arvore.predict(carac_teste)
acuracia_arvore = accuracy_score(rot_teste,rot_preditos)

####### ---- Máquina de Vetor Suporte ---- #####
clf = SVC()
clf.fit(X=carac_treino,y=rot_treino)
rot_preditos_svm = clf.predict(carac_teste)
acuracia_svm = accuracy_score(rot_teste,rot_preditos_svm)
#### Pós processamento #####
print(f"Acurácia árvore de decisão : {round(acuracia_arvore,5)}")
print(f"Acurácia SVM: {round(acuracia_svm,5)}")
print("*" * 10)

r = export_text(arvore,feature_names=iris['feature_names'])

print("Estrutura da arvore")
print(r)