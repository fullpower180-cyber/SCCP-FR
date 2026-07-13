# SCCP Core Database Specification

## Objectif

La SCCP Core Database est la source unique de vérité (Single Source of Truth) du projet SCCP-FR.

Toutes les fonctionnalités du projet utiliseront cette base de données.

---

## Une ligne = Une commande Star Citizen

Chaque ligne représente une commande unique du jeu.

Cette commande pourra être utilisée par :

- Documentation
- Profils Stream Deck
- Raspberry Pi
- Générateur XML
- Applications futures

---

## Cycle de vie d'une commande

Star Citizen
        │
        ▼
Import officiel
        │
        ▼
Enrichissement SCCP
        │
        ▼
Validation
        │
        ▼
Utilisation par les différents modules