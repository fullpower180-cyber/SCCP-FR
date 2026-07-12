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

# Sauvegarde dans le dossier Database
workbook.save("Database/SCCP_Master_Database_v0.1.xlsx")

print("Classeur créé avec succès !")
print("Base de données enregistrée.")
