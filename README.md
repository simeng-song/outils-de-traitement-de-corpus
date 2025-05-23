# outils-de-traitement-de-corpus

Ce projet vise à entraîner un **modèle de classification** pour attribuer automatiquement un poème à son auteur parmi trois grands noms de la poésie française : *Victor Hugo*, *Charles Baudelaire* et *Paul Verlaine*.

Le corpus utilisé est composé de 300 poèmes collectés depuis le site [Poésie-Française.fr](https://www.poesie-francaise.fr/), puis enrichi par des techniques d’augmentation de données afin d’améliorer la robustesse du modèle.

Les spécificités lexicales et stylistiques propres à chaque poète sont analysées à travers des statistiques de fréquence, de longueur textuelle et des visualisations comme les nuages de mots. Le modèle CamemBERT a été fine-tuné sur ces données pour apprendre à reconnaître ces styles d’écriture distincts.

À travers cette tâche, on découvre notamment que Verlaine présente une régularité thématique et lexicale forte, alors que **Hugo**, avec un style plus complexe et des structures syntaxiques plus variées, s'avère plus difficile à classifier automatiquement. Cette observation illustre les limites actuelles des modèles face à des œuvres littéraires riches en profondeur sémantique.


