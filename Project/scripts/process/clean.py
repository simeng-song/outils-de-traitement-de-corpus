import pandas as pd


fichier_entree = "data/raw/poems.csv"
fichier_sortie = "data/clean/poems.csv"

df = pd.read_csv(fichier_entree)

# Supprimer les lignes incomplètes (titre, auteur ou texte manquant)
df = df.dropna(subset=["title", "author", "text"])

# Supprimer les poèmes trop courts (moins de 30 caractères de texte)
df = df[df["text"].str.len() > 30]

# Nettoyer le champ "title" 
df["title"] = df["title"].str.replace(r"^Poésie\s*:\s*", "", regex=True).str.strip()

# supprimer des espaces multiples et des sauts de ligne
df["text"] = df["text"].str.replace(r"\s+", " ", regex=True).str.strip()

# Écriture du fichier nettoyé
df.to_csv(fichier_sortie, index=False, encoding="utf-8")

print("Fichier nettoyé enregistré dans :", fichier_sortie)
