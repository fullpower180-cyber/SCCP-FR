"""
============================================================
SCCP-FR
generate_master_database.py

Auteur : Jean-Michel
Projet : SCCP-FR

Devise :
Apprendre • Construire • Partager
Rendre Star Citizen plus accessible.
============================================================
"""

# -----------------------------
# Affichage du démarrage
# -----------------------------

print("==========================================")
print("        SCCP MASTER DATABASE")
print("==========================================")
print()

print("Bonjour Jean-Michel !")
print("Bienvenue dans SCCP-FR")
print()

print("Début de la génération...")
# Importation de la bibliothèque Excel
from openpyxl import Workbook

print()

print("Création du classeur Excel...")

# Création du classeur
workbook = Workbook()

# ==========================================
# Création des feuilles
# ==========================================

print("Création des feuilles...")

# Renommer la première feuille
sheet = workbook.active
sheet.title = "00_PROJET"

# Liste des autres feuilles
feuilles = [
    "01_COMMANDES",
    "02_CATEGORIES",
    "03_PERIPHERIQUES",
    "04_TRADUCTIONS",
    "05_PROFILS",
    "06_STREAMDECK",
    "07_ICONES",
    "08_TESTS",
    "09_CHANGELOG"
]

# Création automatique
for nom in feuilles:
    workbook.create_sheet(title=nom)

print("Toutes les feuilles ont été créées.")

# Sauvegarde dans le dossier Database
workbook.save("database/SCCP_Master_Database_v0.1.xlsx")

print()
print("Base de données créée avec succès !")
print("Fin du programme.")
