# Changelog

Toutes les modifications importantes du projet SCCP-FR seront documentées dans ce fichier.

Le format est inspiré de **Keep a Changelog**.
Le projet suit le principe du **Semantic Versioning**.

---

# [0.2.0] - En développement

## ✨ Ajouté

### Documentation

- Création du document `ACADEMY.md`
- Mise en place de la méthode SCCP Academy
- Documentation du parcours d'apprentissage
- Création de la progression par niveaux Python

### Développement Python

- Création du premier générateur Python
- Création automatique du classeur Excel
- Création automatique des feuilles de la Master Database
- Création automatique des en-têtes de la feuille `01_COMMANDES`
- Première mise en forme automatique des en-têtes
- Utilisation des styles OpenPyXL
- Première fonction Python réutilisable
- Première constante Python (`COLONNES_COMMANDES`)

### Architecture

- Séparation du programme en :
  - Imports
  - Constantes
  - Fonctions
  - Programme principal
- Début de la standardisation du code Python
- Création de la version de développement `generate_master_database_v2.py`

### Gestion de projet

- Mise en place des Sprints de développement
- Définition des objectifs par Sprint
- Début des revues de code
- Mise en place d'une méthode de validation après chaque Sprint

---

## 🔄 Modifié

### Générateur Python

- Réorganisation complète du script
- Amélioration de la lisibilité
- Centralisation des constantes
- Utilisation des fonctions Python
- Simplification du code de génération

### Méthode de développement

- Adoption d'un développement incrémental
- Validation après chaque fonctionnalité
- Début des revues de code

---

## 🛠️ Corrigé

- Correction de l'ordre d'exécution du programme
- Correction des appels de fonctions
- Correction de l'utilisation des variables
- Correction de la génération des en-têtes
- Correction de la structure du programme
- Correction de plusieurs erreurs liées aux tests

### Débogage

- Identification d'erreurs d'exécution
- Correction d'un lancement de la mauvaise version du programme
- Correction de plusieurs oublis d'enregistrement avant exécution
- Mise en place d'une méthode de diagnostic
- Création de la première checklist développeur

---

# [0.1.0] - Fondation du projet

## ✨ Ajouté

### Initialisation

- Création du dépôt GitHub
- Création du README
- Création du CHANGELOG
- Création du DESIGN_SYSTEM
- Création de la structure du projet

### Environnement

- Installation de Python
- Installation de VS Code
- Installation de GitHub Desktop
- Installation d'OpenPyXL

### Projet

- Création des dossiers :
  - assets
  - Database
  - docs
  - profiles
  - tools
  - xml

- Premier programme Python exécuté avec succès
- Première génération d'un fichier Excel
