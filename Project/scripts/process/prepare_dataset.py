import pandas as pd
from sklearn.model_selection import train_test_split
from datasets import Dataset, DatasetDict
from transformers import AutoTokenizer
import os

# Charger les données augmentées
df = pd.read_csv("data/clean/poems_augmented.csv")

# Nettoyer et mapper les auteurs vers des labels
label_map = {name: i for i, name in enumerate(sorted(df["author"].unique()))}
df["label"] = df["author"].map(label_map)
df["label"] = df["label"].astype(int)


# Séparer en train/dev/test
train_dev, test = train_test_split(df, test_size=0.1, stratify=df["label"], random_state=42)
train, dev = train_test_split(train_dev, test_size=0.1111, stratify=train_dev["label"], random_state=42)

# Créer DatasetDict
dataset = DatasetDict({
    "train": Dataset.from_pandas(train),
    "dev": Dataset.from_pandas(dev),
    "test": Dataset.from_pandas(test)
})

# Charger le tokenizer CamemBERT
tokenizer = AutoTokenizer.from_pretrained("camembert-base")

# Tokenisation
def tokenize(example):
    return tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=512
    )

dataset = dataset.map(tokenize, batched=True)

# Supprimer les colonnes inutiles pour l'entraînement
cols_to_remove = [col for col in ["title", "author", "text", "is_augmented", "source", "__index_level_0__"] if col in dataset["train"].column_names]
dataset = dataset.remove_columns(cols_to_remove)

# Définir la colonne de labels
dataset = dataset.cast_column("label", dataset["train"].features["label"])

# Sauvegarder le dataset tokenisé
dataset.save_to_disk("data/processed/dataset_train")

print("Dataset prêt et sauvegardé dans data/processed/dataset_train")
