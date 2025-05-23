import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud
import os
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
# Liste des mots vides en français (NLTK + extension manuelle)
stopwords_fr = set(stopwords.words("french"))
stopwords_fr.update([
    "comme", "sans", "plus", "ainsi", "dont", "trop", "même", "tout","toujours",
    "très", "encore", "souvent", "rien", "peu", "cette","où", "si", "sous"
])


# Charger le corpus nettoyé
df = pd.read_csv("data/clean/poems.csv")

# Créer le dossier de sortie
os.makedirs("figures", exist_ok=True)

# 1. Longueur des textes
df["nb_caracteres"] = df["text"].str.len()
df["nb_mots"] = df["text"].str.split().apply(len)

# Histogramme général
plt.figure(figsize=(10, 5))
sns.histplot(df["nb_mots"], bins=30, kde=True, color="skyblue")
plt.title("Distribution de la longueur des poèmes (en mots)")
plt.xlabel("Nombre de mots")
plt.ylabel("Nombre de poèmes")
plt.savefig("figures/longueur_textes_mots.png")
plt.close()

# Par auteur
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x="author", y="nb_mots", palette="Set2")
plt.title("Longueur des poèmes par auteur")
plt.xlabel("Auteur")
plt.ylabel("Nombre de mots")
plt.savefig("figures/longueur_par_auteur.png")
plt.close()

# 2. Mots fréquents 
def calculer_frequences(textes):
    mots = " ".join(textes).lower().split()
    mots_filtres = [m for m in mots if m not in stopwords_fr and m.isalpha() and len(m) > 1]
    return Counter(mots_filtres)

# Zipf par auteur
for auteur in df["author"].unique():
    sous_df = df[df["author"] == auteur]
    freqs = calculer_frequences(sous_df["text"])
    mots, compte = zip(*freqs.most_common(30))

    plt.figure(figsize=(12, 4))
    sns.barplot(x=list(mots), y=list(compte), palette="mako")
    plt.xticks(rotation=45, ha="right")
    plt.title(f"Mots significatifs les plus fréquents - {auteur}")
    plt.ylabel("Fréquence")
    plt.xlabel("Mot")
    plt.tight_layout()
    plt.savefig(f"figures/frequence_mots_{auteur.replace(' ', '_').lower()}.png")
    plt.close()

# 3. Nuage de mots pour chaque auteur
for auteur in df["author"].unique():
    sous_df = df[df["author"] == auteur]
    freqs = calculer_frequences(sous_df["text"])
    
    # nuage de mots à partir des fréquences filtrées
    wordcloud = WordCloud(
        width=1000,
        height=400,
        background_color="white",
        colormap="magma",
        max_words=100
    ).generate_from_frequencies(freqs)

    # Sauvegarde de l'image
    plt.figure(figsize=(10, 4))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"Nuage de mots - {auteur}")
    plt.tight_layout()
    plt.savefig(f"figures/wordcloud_{auteur.replace(' ', '_').lower()}.png")
    plt.close()

print("Analyse terminée (avec stopwords supprimés). Graphiques dans 'figures/'")
