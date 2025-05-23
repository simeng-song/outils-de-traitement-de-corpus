# TP5 : Finetuner le modèle pretrained qui correspond le plus à vos données grâce au trainer d'hugging face

## Entraînement du modèle

L’objectif de cette étape était de fine-tuner le modèle pré-entraîné `camembert-base` sur le corpus poétique enrichi. Le modèle a été entraîné sur un dataset issu du fichier [poems_augmented.csv](https://github.com/simeng-song/outils-de-traitement-de-corpus/blob/main/Project/data/clean/poems_augmented.csv), comprenant à la fois les textes originaux et des exemples artificiellement augmentés par substitution lexicale contrôlée. Cette augmentation a permis de renforcer la robustesse du modèle face aux variations stylistiques.

L'entraînement a été réalisé à l’aide de la classe `Trainer` de Hugging Face, avec une stratégie d’évaluation à chaque époque et une sauvegarde automatique du meilleur modèle en fonction du score F1. J’ai mis en place l’ensemble de ce processus dans le script [train_model.py](https://github.com/simeng-song/outils-de-traitement-de-corpus/blob/main/Project/scripts/process/train_model.py), où le modèle a été entraîné pendant 4 époques, avec une taille de batch fixée à 8 et un taux d’apprentissage de 2e-5.

```python
# Définir les arguments d'entraînement
training_args = TrainingArguments(
    output_dir="results",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=4,
    weight_decay=0.01, # éviter le surapprentissage
    logging_dir="logs",
    load_best_model_at_end=True,
    metric_for_best_model="f1",
)
```

## Résultats obtenus

Les résultats montrent une progression constante et cohérente des performances au fil des époques, comme le résume le tableau suivant :

| Époque | Accuracy | F1-score | Loss | Précision | Rappel |
| --- | --- | --- | --- | --- | --- |
| 1 | 0.545 | 0.489 | 1.069 | 0.808 | 0.545 |
| 2 | 0.697 | 0.699 | 0.992 | 0.778 | 0.697 |
| 3 | 0.758 | 0.759 | 0.895 | 0.795 | 0.758 |
| 4  | **0.788** | **0.780** | **0.851** | **0.835** | **0.788** |

Le F1-score est passé de **0,489** à l’époque 1 à **0,780** à l’époque 4. La précision a atteint **0,835**, le rappel **0,788**, et l’exactitude globale **0,788** également. La courbe des pertes diminue à chaque époque (de **1,069** à **0,851**), ce qui confirme une convergence stable du modèle. 

Le meilleur modèle a logiquement été sauvegardé à l’issue de la quatrième époque (`checkpoint-132`) et exporté dans le dossier `model/poetique_camembert`.

Ces résultats confirment que l’architecture choisie est bien adaptée à la tâche, et que l’ensemble du pipeline (nettoyage, augmentation, tokenisation, entraînement) fonctionne de manière cohérente.
