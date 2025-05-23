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


# normal imports
from datasets import load_from_disk
from transformers import CamembertForSequenceClassification, Trainer, TrainingArguments, AutoTokenizer
import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import os

# Charger le dataset préparé
dataset = load_from_disk("data/processed/dataset_train")

# Charger le modèle CamemBERT pour la classification
model = CamembertForSequenceClassification.from_pretrained("camembert-base", num_labels=3)

# Définir les métriques d'évaluation
def compute_metrics(pred):
    labels = pred.label_ids
    preds = np.argmax(pred.predictions, axis=1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average="weighted")
    acc = accuracy_score(labels, preds)
    return {
        "accuracy": acc,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }

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

# Créer le trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["dev"],
    tokenizer=AutoTokenizer.from_pretrained("camembert-base"),
    compute_metrics=compute_metrics,
)

# Lancer l'entraînement
trainer.train()

# Sauvegarder le modèle finetuné
model.save_pretrained("model/poetique_camembert")
