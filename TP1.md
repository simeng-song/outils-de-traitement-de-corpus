# TP1  

## Partie 1 - étude de cas CoNLL 2003:  

**1. Quelle type de tâche propose CoNLL 2003 ?**

CoNLL 2003 propose une tâche de reconnaissance d'entités nommées indépendante de la langue. Cette tâche consiste à identifier automatiquement dans un texte des entités nommées telles que les *personnes (PER), organisations (ORG), localisations (LOC) et entités diverses (MISC)*. 

**2. Quel type de données y a-t-il dans CoNLL 2003 ?**

Les données se composent de huit fichiers couvrant deux langues : l'anglais et l'allemand. Les données en anglais proviennent du corpus *Reuters* constitué d'articles de presse. Le texte des données allemandes provient du journal allemand *Frankfurter Rundschau*. Chaque fichier contient des textes pré-segmentés en phrases et en mots, avec des annotations en format BIO (Begin, Inside, Outside) indiquant les frontières des entités.

**3. A quel besoin répond CoNLL 2003 ?**

CoNLL 2003 répond au besoin d’évaluer et d’améliorer les systèmes de reconnaissance d'entités nommées (NER) en proposant un benchmark standardisé pour comparer les performances des modèles. Ce corpus permet de tester la robustesse et la précision des modèles sur des textes journalistiques réels et variés, et il a largement contribué au développement des techniques modernes de NER, notamment dans les contextes multilingues.


**4. Quels types de modèles ont été entraînés sur CoNLL 2003 ?**

On a d’abord utilisé des modèles statistiques tels que les HMM (Hidden Markov Models) ou CRF (Conditional Random Fields). Par la suite, les modèles neuronaux basés sur les réseaux récurrents comme LSTM et GRU, ont été largement utilisés. Aujourd’hui, les meilleurs résultats sont obtenus grâce aux modèles transformers comme BERT, RoBERTa, ou Flair, qui exploitent des représentations contextuelles profondes.

**5. Est un corpus monolingue ou multilingue ?**

Il s'agit d'un corpus multilingue dont les données couvrent deux langues, l'anglais et l'allemand.
  

## Partie 2 - projet

**Besoin** :

Ce projet s'inscrit dans le cadre d'une tâche de classification d’auteurs de poésie française. 

L’objectif est de construire un système capable de généraliser sur de nouveaux poèmes en identifiant leur auteur à partir du style lexical.

**Sujet** : 

À partir du texte seul, reconnaître automatiquement de quel auteur provient un poème.

**Type de tâche à réaliser** : 

Classification de texte multiclasse

**Type de données à exploiter** :

Le corpus est composé de poèmes rédigés en français classique. Chaque échantillon est une entrée structurée contenant : un titre, un auteur et un texte complet.


**Où récupérer les données** : 

Les données sont collectées depuis le site web [poésie-française.fr](https://www.poesie-francaise.fr/), une ressource publique regroupant les œuvres des plus grands poètes français.

**Libres d'accès** : 

Oui. Le site est en libre accès, sans authentification requise.