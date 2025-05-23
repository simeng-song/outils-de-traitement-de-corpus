# monkey patch to remove bad argument
import builtins
real_accelerator_init = None

def patch_accelerator():
    from accelerate import Accelerator
    import inspect

    global real_accelerator_init
    real_accelerator_init = Accelerator.__init__

    def safe_init(self, *args, **kwargs):
        if 'use_seedable_sampler' in kwargs:
            del kwargs['use_seedable_sampler']
        return real_accelerator_init(self, *args, **kwargs)

    Accelerator.__init__ = safe_init

patch_accelerator()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import torch

from datasets import load_from_disk
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer
from sklearn.metrics import classification_report, confusion_matrix

# Charger le dataset encodé 
dataset = load_from_disk("data/processed/dataset_train")
test_dataset = dataset["test"]

# Charger le modèle fine-tuné et le tokenizer
model_path = "model/poetique_camembert"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained("camembert-base")

# Créer un Trainer pour l'évaluation
trainer = Trainer(model=model)

# Évaluer le modèle sur l'ensemble test
print("Évaluation sur le jeu de test...")
results = trainer.evaluate(eval_dataset=test_dataset)
print("Résultats bruts :", results)

# Prédictions pour matrice de confusion
print("Génération des prédictions...")
predictions = trainer.predict(test_dataset)
y_true = predictions.label_ids
y_pred = np.argmax(predictions.predictions, axis=1)

# Rapport de classification
print("\nClassification report :")
print(classification_report(y_true, y_pred, target_names=["Baudelaire", "Hugo", "Verlaine"]))

# Matrice de confusion
cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Baudelaire", "Hugo", "Verlaine"],
            yticklabels=["Baudelaire", "Hugo", "Verlaine"])
plt.title("Matrice de confusion sur l'ensemble test")
plt.xlabel("Prédit")
plt.ylabel("Réel")
plt.tight_layout()
plt.savefig("figures/confusion_matrix_test.png")
print("Matrice de confusion sauvegardée dans figures/confusion_matrix_test.png")
