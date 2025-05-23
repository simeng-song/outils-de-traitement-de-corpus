# TP6 : Évaluer le modèle

## Évaluation finale sur l’ensemble test

À l’aide du script [evaluer.py](https://github.com/simeng-song/outils-de-traitement-de-corpus/blob/main/Project/scripts/process/train_model.py), l’évaluation finale du modèle a été réalisée sur un sous-ensemble de test composé de 33 poèmes répartis équitablement entre les trois auteurs. Le modèle atteint une précision globale de **73 %**, ce qui reste satisfaisant compte tenu de la taille relativement réduite du corpus.

![Matrice de confusion](https://raw.githubusercontent.com/simeng-song/outils-de-traitement-de-corpus/main/Project/figures/confusion_matrix_test.png)

La matrice de confusion révèle des performances contrastées selon les auteurs : les poèmes de *Verlaine* sont parfaitement reconnus (**11/11**), tout comme ceux de *Baudelaire* à 91 % (**10/11**). En revanche, le modèle rencontre davantage de difficultés à identifier les textes de *Victor Hugo*, avec seulement **3 bons classements sur 11**, et une confusion marquée vers Verlaine.

Ces résultats se reflètent également dans le rapport de classification :

- Baudelaire : F1 = **0,83**, précision = 0,77, rappel = 0,91
- Verlaine : F1 = **0,79**, précision = 0,65, rappel = 1,00
- Hugo : F1 = **0,43**, précision = 1,00, mais rappel = **0,27**

On constate que si le modèle identifie bien les poèmes non-hugoliens, il a tendance à confondre Hugo avec Verlaine, probablement en raison de similarités lexicales ou de structures stylistiques partagées dans certains cas. Ce déséquilibre invite à envisager des stratégies complémentaires, telles qu’un enrichissement ciblé du corpus Hugo ou une pondération des classes.


## Perspectives d’amélioration
Malgré les résultats encourageants obtenus pour certains auteurs comme Verlaine ou Baudelaire, l’évaluation finale révèle une faiblesse marquée dans la reconnaissance des poèmes de **Victor Hugo**. Ce déséquilibre suggère que le modèle peine à capter les spécificités stylistiques propres à cet auteur, dont la langue est souvent plus soutenue et les structures syntaxiques plus complexes. 

Pour remédier à cette limite, plusieurs pistes peuvent être envisagées. D’abord, un **enrichissement du corpus**, notamment du côté des textes de Hugo, permettrait de mieux équilibrer les données et d’offrir au modèle une base plus représentative. De même, le recours à des modèles préentraînés davantage spécialisés dans les textes littéraires, comme **FlauBERT** ou des architectures de type **LSTM**, pourrait pourrait capturer plus finement les particularités poétiques et améliorer la qualité des représentations contextuelles. En plus, une meilleure **répartition des exemples par auteur**, notamment dans la phase d’augmentation, pourrait réduire les biais d’apprentissage. Enfin, une **étape intermédiaire de pré-entraînement** sur un corpus poétique plus large (poésie du XIXe par exemple) ou une meilleure intégration des traits stylistiques dans la phase de préparation des données pourraient faciliter l’adaptation fine du modèle.