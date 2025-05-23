# TP3 : Visualiser les statistiques de corpus

## Visualiser le corpus à partir de statistiques de textes

Pour mieux comprendre les caractéristiques stylistiques du corpus poétique, j'ai réalisé une série d’analyses statistiques et de visualisations sur les 300 poèmes extraits à l'aide du script [analyze.py](https://github.com/simeng-song/outils-de-traitement-de-corpus/blob/main/Project/scripts/plot/analyze.py).

- **Longueur des textes**
    
   Une première visualisation montre la distribution de la longueur des poèmes (en nombre de mots). Les poèmes de Victor Hugo se démarquent par leur longueur significativement plus élevée, avec de nombreux extrêmes dépassant les 1000 mots. À l’inverse, ceux de Paul Verlaine sont plus courts et plus homogènes, ce qui reflète son style plus concis et musical.
   
   ![Longueur par auteur](https://raw.githubusercontent.com/simeng-song/outils-de-traitement-de-corpus/main/Project/figures/longueur_par_auteur.png)

- **Mots les plus fréquents (Zipf)**
    
   Pour chaque auteur, j'ai analysé les mots les plus fréquents après suppression des mots vides en français. Cette analyse révèle des différences lexicales marquées :
    
    - *Baudelaire* : prédominance de mots liés au corps et à l’émotion (`yeux`, `coeur`, `nuit`, `douleur`)
    - *Verlaine* : vocabulaire plus abstrait et introspectif (`rien`, `âme`, `loin`, `dieu`)
    - *Hugo* : lexique plus narratif et politique (`peuple`, `jour`, `gloire`, `soldats`, `dieu`)
    
   Ces différences soutiennent la faisabilité d’une tâche de classification d’auteur à partir du texte brut.
   
   ![Exemple : fréquence des mots - Baudelaire](https://raw.githubusercontent.com/simeng-song/outils-de-traitement-de-corpus/main/Project/figures/frequence_mots_charles_baudelaire.png)

- **Nuages de mots**
    
   Afin de visualiser de manière plus intuitive les spécificités stylistiques, j'ai également généré des nuages de mots pour chaque auteur, en utilisant les fréquences pondérées et nettoyées. Cette représentation permet de visualiser les contrastes lexicaux entre les auteurs.

   ![Exemple : Wordcloud - Verlaine](https://raw.githubusercontent.com/simeng-song/outils-de-traitement-de-corpus/main/Project/figures/wordcloud_paul_verlaine.png)


## Utiliser une technique d'augmentation de données pour le corpus

Afin d’améliorer la robustesse de l’apprentissage, j’ai mis en œuvre une **technique d’augmentation contrôlée** du corpus.

J’ai remplacé les mots-clés poétiques par des synonymes ou variantes stylistiques, choisis manuellement (par exemple : `yeux → regards`, `amour → passion`, `nuit → obscurité`). 

Par le script [augment.py](https://github.com/simeng-song/outils-de-traitement-de-corpus/blob/main/Project/scripts/process/augment.py), j’ai sélectionné 10 poèmes par auteur, appliqué entre 2 et 3 substitutions aléatoires, puis fusionné les données originales et augmentées.

Enfin, j’ai obtenu un fichier enrichi [poems_augmented.csv](https://github.com/simeng-song/outils-de-traitement-de-corpus/blob/main/Project/data/clean/poems_augmented.csv) de 330 poèmes (300 originaux + 30 augmentés), avec un champ `is_augmented` et un champ `source` permettant de différencier les types de données.

Cette méthode permet de générer des textes plausibles et stylistiquement proches des originaux, tout en diversifiant légèrement le lexique afin de favoriser la généralisation du modèle.