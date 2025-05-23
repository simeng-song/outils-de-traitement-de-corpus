import requests
from bs4 import BeautifulSoup
import csv
import time
import random

# URL de base du site de poésie
BASE_URL = "https://www.poesie-francaise.fr"

# Dictionnaire des auteurs et leurs pages listant tous leurs poèmes
poets = {
    "Victor Hugo": "/poemes-victor-hugo/",
    "Charles Baudelaire": "/poemes-charles-baudelaire/",
    "Paul Verlaine": "/poemes-paul-verlaine/"
}

# Nombre maximal de poèmes à récupérer par auteur
MAX_POEMS = 100

# Nom du fichier CSV de sortie
output_file = "poems.csv"

# Récupérer les liens vers les pages de chaque poème
def get_poem_links(author_path):
    url = BASE_URL + author_path
    print(f"Chargement de la page : {url}")
    response = requests.get(url)
    response.encoding = 'utf-8'

    # Analyse du HTML
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a", href=True)

    # Sélectionner des liens contenant "poeme-" (format typique des pages de poèmes)
    poem_links = []
    for a in links:
        href = a["href"]
        if "poeme-" in href and href.endswith(".php"):
            # Compléter le lien si besoin
            full_url = BASE_URL + href if href.startswith("/") else href
            poem_links.append(full_url)

    # Supprimer les doublons, limiter à MAX_POEMS
    unique_links = list(dict.fromkeys(poem_links))[:MAX_POEMS]
    print(f"{len(unique_links)} liens de poèmes récupérés")
    return unique_links

# Extraire le titre et le texte d’un poème
def extract_poem(poem_url):
    try:
        response = requests.get(poem_url, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, "html.parser")

        # Titre du poème
        title_tag = soup.find("h1")
        title = title_tag.get_text(strip=True) if title_tag else "Sans titre"

        # Contenu du poème
        poem_paragraph = soup.find("p")
        if not poem_paragraph:
            return title, None
        
        # Extraire le contenu ligne par ligne
        content_lines = []
        for el in poem_paragraph.contents:
            if el.name == "br":
                content_lines.append("\n")
            elif isinstance(el, str):
                content_lines.append(el.strip())

        content = "".join(content_lines).strip()
        return title, content if content else None

    except Exception as e:
        print(f"Échec extraction {poem_url} → {e}")
        return None, None

with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "author", "text"])  # En-tête du CSV

    # Parcours de chaque auteur
    for author, path in poets.items():
        print(f"\n Traitement de {author}...")
        links = get_poem_links(path)

        # Parcours des liens de poèmes
        for link in links:
            title, content = extract_poem(link)

            # Vérification que le contenu est non vide
            if title and content and len(content) > 30:
                writer.writerow([title, author, content])
                print(f"{title}")
            else:
                print(f"Contenu vide ou trop court : {link}")

            # Pause aléatoire pour imiter un comportement humain
            time.sleep(random.uniform(1.0, 1.8))

print("\n Extraction terminée. Fichier créé : poems.csv")
