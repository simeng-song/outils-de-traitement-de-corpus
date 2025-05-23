# TP2 : Récuperer votre corpus de travail à partir d'une resource web

## Récupération des données

J’ai d’abord écrit un script Python [crawl.py](https://github.com/simeng-song/outils-de-traitement-de-corpus/blob/main/Project/scripts/process/crawl.py) utilisant les bibliothèques `requests` et `BeautifulSoup`. Ce script automatise l’extraction des poèmes pour chacun des trois auteurs, en parcourant les pages listant leurs œuvres, puis en accédant à chaque page de poème. Chaque poème est extrait avec son **titre**, **auteur** et **texte intégral.** Le fichier brut `poems.csv` est sauvegardé dans `data/raw/`.

## Nettoyage du corpus

Un second script [clean.py](https://github.com/simeng-song/outils-de-traitement-de-corpus/blob/main/Project/scripts/process/clean.py) permet de filtrer et de nettoyer les données en supprimant les doublons, les textes vides ou trop courts, et les en-têtes inutiles. Le corpus nettoyé est sauvegardé dans `data/clean/poems.csv`.

## Structure du corpus

- Nombre total de poèmes : 300 (100 par auteur)
- Champs : `title`, `author`, `text`
- Encodage : UTF-8
- Format : CSV
