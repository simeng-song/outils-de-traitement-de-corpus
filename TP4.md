# TP4 Préparer le dataset et choisir un modèle


**A partir des données que vous avez récupérées, créez un dataset synthétique.**

À partir du corpus enrichi [poems_augmented.csv](https://github.com/simeng-song/outils-de-traitement-de-corpus/blob/main/Project/data/clean/poems_augmented.csv), j’ai préparé un `DatasetDict` en trois sous-ensembles :

- `train` (80%)
- `dev` (10%)
- `test` (10%)

La division a été réalisée de manière stratifiée afin de respecter la distribution des auteurs. J’ai  utilisé le tokenizer de CamemBERT pour encoder chaque poème sous forme de vecteurs numériques (`input_ids` et `attention_mask`) prêts à être utilisés par un modèle Transformer. 

Le label de chaque poème correspond à l’auteur, encodé sous forme d'entier (`0 = Baudelaire`, `1 = Hugo`, `2 = Verlaine`).

Le script utilisé, [prepare_dataset.py](https://github.com/simeng-song/outils-de-traitement-de-corpus/blob/main/Project/scripts/process/prepare_dataset.py), sauvegarde enfin le dataset encodé dans le format Hugging Face  (via `save_to_disk()`). Ce jeu de données final est ensuite prêt à être utilisé par la classe `Trainer` dans l’étape suivante.    

  
**Choississez l'architecture adaptée à votre tâche et trouvez un modèle qui correspond à votre tâche et à cette architecture.**

J’ai choisi d'utiliser **CamemBERT**, un modèle pré-entraîné de type RoBERTa spécifiquement adapté à la langue française. Le modèle `camembert-base` a été instancié pour une tâche de classification de texte multiclasse **(num_labels = 3)**.

Ce choix m’a paru pertinent pour traiter des textes poétiques, souvent riches en structures syntaxiques complexes et en vocabulaire littéraire. CamemBERT offre en effet des représentations sémantiques fines, et son tokenizer est optimisé pour les subtilités de la langue française. De plus, son intégration fluide dans l’écosystème Hugging Face m’a permis de le mettre en œuvre rapidement dans une architecture de classification multiclasse, avec trois étiquettes correspondant aux auteurs étudiés.

Le modèle a été entraîné avec les paramètres suivants :

- 4 époques
- batch size = 8
- learning rate = 2e-5
- optimisation basée sur le F1-score

