import pandas as pd
import random
import os

# Liste des synonymes ou mots proches en style poétique
SUBSTITUTIONS = {
    "yeux": ["regards", "pupilles"],
    "coeur": ["âme", "esprit"],
    "nuit": ["soir", "obscurité"],
    "jour": ["matin", "aurore"],
    "mort": ["tombe", "fin"],
    "amour": ["passion", "désir"],
    "beau": ["joli", "charmant"],
    "vers": ["lignes", "paroles"],
    "dieu": ["seigneur", "divin"],
    "douleur": ["peine", "souffrance"]
}

# Charger les données d'entraînement
df = pd.read_csv("data/clean/poems.csv")

# Supprimer les lignes vides ou incomplètes si nécessaire
df = df.dropna(subset=["title", "author", "text"])
df = df[df["text"].str.strip().str.len() > 0]

# Sélectionner aléatoirement N poèmes à augmenter
N = 10  # nombre par auteur
augmented_rows = []

for author in df["author"].unique():
    sous_df = df[df["author"] == author].sample(n=N, random_state=42)

    for _, row in sous_df.iterrows():
        texte = row["text"]
        nouveau_texte = texte

        # Appliquer 2 à 3 substitutions aléatoires
        substitutions = random.sample(list(SUBSTITUTIONS.items()), k=random.randint(2, 3))
        for mot, alternatives in substitutions:
            if mot in nouveau_texte:
                nouveau_texte = nouveau_texte.replace(mot, random.choice(alternatives), 1)

        # Ajouter comme une nouvelle ligne
        augmented_rows.append({
            "title": row["title"] + " (augmenté)",
            "author": row["author"],
            "text": nouveau_texte,
            "is_augmented": True,
            "source": "manuel"
        })

# Convertir en DataFrame
df_aug = pd.DataFrame(augmented_rows)

# Ajouter colonne is_augmented et source aux originaux
df["is_augmented"] = False
df["source"] = "original"

# Fusionner données originales et augmentées
df_final = pd.concat([df, df_aug], ignore_index=True)

# Sauvegarder les données augmentées
df_final.to_csv("data/clean/poems_augmented.csv", index=False, encoding="utf-8")

print("Données augmentées générées et enregistrées dans data/clean/poems_augmented.csv")
