# Planeur Phénix Bleu

Ce dépôt contient la preuve thermodynamique et les modules de simulation du projet **Phénix Bleu** : un planeur autonome à propulsion hybride (Argon-Plasma / Stirling / Venturi) avec gestion fermée des flux et biosphère embarquée.

## Fonctionnalités principales
- Simulation complète du cycle énergétique (jour/nuit, piqué, croisière)
- Modélisation des flux Argon, N2, H2O, CO2 en boucle fermée
- Gestionnaire d'accumulation hermétique (Accumulateur d'Infini)
- Systèmes de secours (Flash H2, charbon, cycles BSF, etc.)
- Calculs de puissance, traînée, rendement Carnot, autonomie
- Boucle nutritionnelle fermée (Spiruline + Black Soldier Flies)

## Structure du dépôt
- `preuve_thermodynamique_argon.py` : Script principal, version unifiée
- `archive/` : Anciennes versions, modules de test, résultats
- `accumulateur.md` : Documentation sur le protocole zéro-rejet

## Exécution

```bash
python preuve_thermodynamique_argon.py
```

## Auteur
- LaoHanX (2024-2026)

## Licence
MIT
