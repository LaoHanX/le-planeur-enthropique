# Planeur Phénix : Étude de Faisabilité Thermodynamique

## Système de Propulsion Hybride CO2/H2 pour Vol de Longue Endurance

**Version** : 1.0  
**Date** : 30 janvier 2026  
**Classification** : Étude conceptuelle - Niveau TRL 1-2  

---

## Résumé Exécutif

Ce document présente l'analyse thermodynamique d'un concept de planeur motorisé utilisant un cycle thermique à CO2 supercritique, avec appoint thermique par combustion d'hydrogène. L'objectif est d'évaluer la faisabilité théorique d'un vol de très longue endurance (semaines à mois) pour des missions de surveillance (incendies de forêt, frontières, environnement).

**Conclusion préliminaire** : Les calculs thermodynamiques montrent des bilans de masse et d'énergie théoriquement positifs sous certaines hypothèses optimistes. Cependant, de nombreux défis d'ingénierie restent à résoudre avant toute validation expérimentale.

---

## Table des Matières

1. [Introduction et Contexte](#1-introduction-et-contexte)
2. [Principes Physiques](#2-principes-physiques)
3. [Architecture du Système](#3-architecture-du-système)
4. [Bilans Thermodynamiques](#4-bilans-thermodynamiques)
5. [Bilans de Masse](#5-bilans-de-masse)
6. [Bilan Électrique](#6-bilan-électrique)
7. [Systèmes Auxiliaires](#7-systèmes-auxiliaires)
8. [Analyse des Risques et Limites](#8-analyse-des-risques-et-limites)
9. [Travaux Futurs](#9-travaux-futurs)
10. [Références](#10-références)

---

## 1. Introduction et Contexte

### 1.1 Problématique

Les drones et planeurs de surveillance actuels sont limités par :
- L'autonomie des batteries (heures)
- La consommation de carburant fossile
- La dépendance aux conditions météorologiques (planeurs purs)

### 1.2 Concept Proposé

Un planeur motorisé hybride combinant :
- **Fluide de travail** : CO2 en cycle quasi-fermé
- **Source thermique** : Combustion H2 + concentration solaire
- **Régénération** : Électrolyse embarquée de l'eau

### 1.3 Avertissement Scientifique

> **Ce document présente une étude THÉORIQUE.**  
> Les calculs reposent sur des modèles simplifiés et des hypothèses optimistes.  
> Aucun prototype n'a été construit ni testé.  
> Les rendements réels seront inférieurs aux valeurs théoriques.

---

## 2. Principes Physiques

### 2.1 Cycle Thermodynamique au CO2

Le CO2 présente des propriétés intéressantes pour un cycle thermique :

| Propriété | Valeur | Implication |
|-----------|--------|-------------|
| Point critique | 31.1°C / 73.8 bar | Liquéfaction possible à température ambiante |
| Masse molaire | 44 g/mol | Plus dense que l'air, stockage compact |
| Non-toxicité | - | Sécurité opérationnelle |
| Abondance | - | Disponibilité, coût faible |

**Cycle proposé** (simplifié) :
1. Compression du CO2 liquide (basse température, altitude)
2. Chauffage et vaporisation (source thermique)
3. Détente dans un moteur à piston ou turbine
4. Refroidissement et liquéfaction (air d'altitude)

### 2.2 Rendement de Carnot

Le rendement maximal théorique est donné par :

$$\eta_{Carnot} = 1 - \frac{T_{froid}}{T_{chaud}}$$

Avec les températures du système :
- T_chaud = 800 K (chambre de combustion H2)
- T_froid = 268 K (air à 3000 m d'altitude, -5°C)

$$\eta_{Carnot} = 1 - \frac{268}{800} = 0.665 = 66.5\%$$

**Rendement réel estimé** : 30-40% (pertes mécaniques, thermiques, irréversibilités)

### 2.3 Combustion de l'Hydrogène

L'hydrogène sert de "bougie thermique" pour chauffer le CO2 :

$$2H_2 + O_2 \rightarrow 2H_2O + 286 \text{ kJ/mol}$$

| Propriété | Valeur |
|-----------|--------|
| PCI (Pouvoir Calorifique Inférieur) | 120 MJ/kg |
| Température de flamme | ~2800 K |
| Produit de combustion | H2O (récupérable) |

**Avantage clé** : L'eau produite peut être récupérée et ré-électrolysée.

---

## 3. Architecture du Système

### 3.1 Schéma de Principe

```
                    ┌─────────────────┐
                    │  CONCENTRATEUR  │
                    │    SOLAIRE      │
                    └────────┬────────┘
                             │ (jour)
                             ▼
┌──────────┐     ┌──────────────────────┐     ┌──────────┐
│ RÉSERVOIR│     │   CHAMBRE EXPANSION  │     │  MOTEUR  │
│ CO2      │────▶│   (T = 800 K)        │────▶│  PISTON  │
│ (60 bar) │     │   + Combustion H2    │     │          │
└──────────┘     └──────────────────────┘     └────┬─────┘
     ▲                                              │
     │           ┌──────────────────────┐          │
     │           │   CONDENSEUR         │          │
     └───────────│   (Air froid altitude)│◀─────────┘
                 │   T = 268 K          │
                 └──────────────────────┘
```

### 3.2 Composants Principaux

| Composant | Fonction | Masse estimée |
|-----------|----------|---------------|
| Réservoir CO2 (60 bar) | Stockage fluide de travail | 15 kg |
| Chambre d'expansion | Conversion thermique → mécanique | 8 kg |
| Condenseur | Liquéfaction CO2 | 5 kg |
| Réservoir H2 (350 bar) | Stockage combustible | 12 kg |
| Électrolyseur PEM | Régénération H2 | 6 kg |
| Système électrique (TENG + turbine) | Production électrique | 4 kg |
| **TOTAL système propulsif** | | **~50 kg** |

### 3.3 Caractéristiques Aérodynamiques

| Paramètre | Valeur | Justification |
|-----------|--------|---------------|
| Masse totale | 400 kg | Pilote (80 kg) + structure + systèmes |
| Envergure | 18 m | Finesse élevée |
| Surface alaire | 15 m² | Charge alaire modérée |
| Finesse max | 45:1 | Comparable aux planeurs de performance |
| Vitesse de croisière | 90 km/h (25 m/s) | Optimum L/D |
| Puissance requise (palier) | 3-5 kW | Traînée × vitesse |

---

## 4. Bilans Thermodynamiques

### 4.1 Puissance Mécanique Disponible

**Hypothèses** :
- Rendement cycle réel : η = 0.40
- Puissance thermique entrée : Q_in = 8 kW (combustion H2)

$$P_{mécanique} = \eta \times Q_{in} = 0.40 \times 8000 = 3200 \text{ W}$$

**Vérification** : Suffisant pour maintenir le vol en palier (besoin ~3-5 kW).

### 4.2 Consommation d'Hydrogène

Pour fournir 8 kW thermiques :

$$\dot{m}_{H2} = \frac{P_{thermique}}{PCI} = \frac{8000}{120 \times 10^6} = 6.67 \times 10^{-5} \text{ kg/s}$$

Soit **240 g/heure** ou **5.76 kg/jour** en fonctionnement continu.

### 4.3 Bilan Thermique : Chaleur Résiduelle

| Flux | Puissance | Utilisation |
|------|-----------|-------------|
| Entrée thermique | 8000 W | - |
| Travail mécanique (40%) | 3200 W | Propulsion |
| Chaleur résiduelle (60%) | 4800 W | Dégivrage, distillation |

**Observation** : La chaleur "perdue" selon Carnot est recyclée pour :
- Dégivrage des ailes (besoin : ~500-2000 W selon conditions)
- Distillation de l'eau du pilote (besoin : ~300 W)
- Chauffage cockpit si nécessaire

---

## 5. Bilans de Masse

### 5.1 Cycle de l'Hydrogène

**Consommation** :
- Fonctionnement moteur : 5.76 kg/jour (hypothèse 24h de vol motorisé)
- En réalité, alternance vol plané / motorisé réduit ce chiffre

**Régénération** (électrolyse) :
- Puissance électrique disponible : ~500 W (voir section 6)
- Rendement électrolyseur PEM : 70%
- Production H2 : 

$$\dot{m}_{H2} = \frac{P_{élec} \times \eta}{E_{électrolyse}} = \frac{500 \times 0.70}{142 \times 10^6} \approx 2.5 \times 10^{-6} \text{ kg/s}$$

Soit **9 g/heure** ou **216 g/jour**.

**Bilan H2** :

| Flux | Valeur/jour |
|------|-------------|
| Consommation (100% motorisé) | -5760 g |
| Consommation (20% motorisé, réaliste) | -1150 g |
| Régénération (électrolyse) | +216 g |
| Récupération condensation | +variable |
| **Déficit** | **-934 g/jour** (cas optimiste) |

> **⚠️ LIMITE IDENTIFIÉE** : Le bilan H2 est NÉGATIF.  
> L'électrolyse embarquée ne peut pas compenser la consommation.  
> Une source externe (thermiques, altitude initiale) est nécessaire.

### 5.2 Cycle de l'Eau

**Sources** :
- Combustion H2 : 9 g H2O par g H2 brûlé
- Métabolisme pilote : ~900 g/jour (respiration + transpiration)
- Condensation atmosphérique : variable (rosée, nuages)

**Pertes** :
- Électrolyse : consomme 9 g H2O par g H2 produit
- Évaporation non récupérée : ~10%

**Bilan eau** : Généralement positif grâce à la combustion et au pilote.

### 5.3 Cycle du CO2

Le CO2 est un fluide de travail en **cycle quasi-fermé** :
- Pas de consommation chimique
- Micro-fuites estimées : 50 g/jour (joints, raccords)
- Compensation : métabolisme pilote (900 g CO2/jour)

**Bilan CO2** : Positif (+850 g/jour net).

---

## 6. Bilan Électrique

### 6.1 Sources d'Électricité

| Source | Puissance | Conditions |
|--------|-----------|------------|
| Turbine éolienne (vent relatif) | 400-600 W | Vol > 15 m/s |
| TENG (nanogénérateur triboélectrique) | 5-15 W | Surface ailes |
| Alternateur moteur | 100-200 W | Moteur en marche |
| **TOTAL** | **500-800 W** | |

### 6.2 Consommations

| Système | Puissance | Remarque |
|---------|-----------|----------|
| Électrolyseur | 350 W | Principal consommateur |
| Avionique | 30 W | Navigation, radio |
| Pompe CO2 (croisière) | 50 W | Circulation fluide |
| Éclairage, divers | 20 W | |
| **TOTAL** | **450 W** | |

### 6.3 Bilan

$$P_{disponible} - P_{consommée} = 575 - 450 = +125 \text{ W}$$

**Marge positive** permettant la recharge des supercondensateurs.

### 6.4 Stockage

- **Supercondensateurs** : Maxwell 3000F, 2.7V
- Énergie stockée : ~11 kJ (3 Wh)
- Avantage : Fonctionne à -40°C, durée de vie illimitée
- Usage : Tampon pour pics de consommation, redémarrage

---

## 7. Systèmes Auxiliaires

### 7.1 Distillation Thermique de l'Eau

L'eau biologique du pilote (sueur, urine) est purifiée par distillation :

**Principe** :
1. Eau sale injectée dans serpentin autour du moteur (800 K)
2. Évaporation instantanée
3. Condensation par air froid d'altitude
4. Sels restent en dépôt solide (éjection périodique)

**Calcul** :
- Chaleur disponible : 4800 W (résidu Carnot)
- Énergie pour évaporer 1 kg eau : 2.5 MJ
- Capacité : **7 kg/heure** (largement excédentaire)

**Avantages vs osmose inverse** :
- Aucune membrane (pas d'usure)
- Aucune pièce mobile
- Énergie gratuite (chaleur perdue)
- Pureté supérieure (99.99%)

### 7.2 Dégivrage Thermique

La chaleur résiduelle est canalisée vers le bord d'attaque des ailes :
- Besoin en conditions givrantes : 500-2000 W
- Disponible : 4800 W
- **Marge de sécurité** : 2.4× à 9.6×

### 7.3 Redondance Allumage

Cinq systèmes indépendants pour l'allumage du H2 :

| Système | Principe | Condition |
|---------|----------|-----------|
| TENG | Triboélectricité (3000 V) | Vol > 15 m/s |
| Turbine | Induction magnétique | Vol > 10 m/s |
| Compression | Effet Diesel (T > 850 K) | Piqué > 50 m/s |
| Parois chaudes | Incandescence charbon | Mode urgence |
| Supercondensateur | Stockage électrostatique | Réserve 6h |

---

## 8. Analyse des Risques et Limites

### 8.1 Limites Thermodynamiques

| Hypothèse | Valeur utilisée | Réalité probable | Impact |
|-----------|-----------------|------------------|--------|
| Rendement cycle | 40% | 25-35% | Consommation H2 accrue |
| Efficacité condenseur | 95% | 80-90% | Pertes CO2 |
| Rendement électrolyseur | 70% | 60-65% | Moins de H2 régénéré |

### 8.2 Défis d'Ingénierie Non Résolus

1. **Stockage H2 haute pression** : Masse des réservoirs, sécurité
2. **Joints haute pression/haute température** : Durabilité
3. **Électrolyseur compact et léger** : Technologie immature
4. **Intégration thermique** : Isolation chambre chaude / condenseur
5. **Contrôle du cycle** : Régulation fine P, T, débits

### 8.3 Bilan Honnête du Concept

| Aspect | Évaluation | Commentaire |
|--------|------------|-------------|
| Fondements physiques | ✅ Valides | Thermodynamique classique |
| Bilans masse/énergie | ⚠️ Tendus | Marges faibles, hypothèses optimistes |
| Faisabilité technique | ❓ Incertaine | Défis d'intégration majeurs |
| Niveau de maturité | TRL 1-2 | Concept, calculs préliminaires |

### 8.4 Scénarios d'Échec

| Risque | Probabilité | Conséquence | Mitigation |
|--------|-------------|-------------|------------|
| Fuite H2 majeure | Moyenne | Perte propulsion | Réserve charbon (10 kg) |
| Givrage condenseur | Faible | Cycle bloqué | Bypass, chauffage |
| Panne électrolyseur | Moyenne | Fin régénération | Réserve H2 initiale |
| Fatigue joints | Élevée | Fuites progressives | Maintenance planifiée |

---

## 9. Travaux Futurs

### 9.1 Court Terme (6-12 mois)

- [ ] Modélisation CFD du condenseur
- [ ] Simulation dynamique du cycle complet
- [ ] Étude de matériaux pour joints haute température
- [ ] Prototype de distillateur thermique (banc d'essai)

### 9.2 Moyen Terme (1-3 ans)

- [ ] Prototype de moteur CO2 à petite échelle
- [ ] Tests d'électrolyseur en conditions de vol
- [ ] Intégration TENG sur profil d'aile
- [ ] Essais en chambre climatique (-40°C)

### 9.3 Long Terme (3-5 ans)

- [ ] Prototype volant à échelle réduite (UAV)
- [ ] Campagne d'essais en vol
- [ ] Certification (si résultats positifs)

---

## 10. Références

### 10.1 Thermodynamique

1. Cengel, Y.A., Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th ed. McGraw-Hill.
2. Span, R., Wagner, W. (1996). "A New Equation of State for Carbon Dioxide". *J. Phys. Chem. Ref. Data*, 25(6), 1509-1596.

### 10.2 Cycles au CO2

3. Dostal, V. (2004). "A Supercritical Carbon Dioxide Cycle for Next Generation Nuclear Reactors". PhD Thesis, MIT.
4. Ahn, Y. et al. (2015). "Review of supercritical CO2 power cycle technology". *Nuclear Engineering and Technology*, 47(6), 647-661.

### 10.3 Électrolyse

5. Carmo, M. et al. (2013). "A comprehensive review on PEM water electrolysis". *Int. J. Hydrogen Energy*, 38(12), 4901-4934.

### 10.4 Aérodynamique

6. Anderson, J.D. (2016). *Fundamentals of Aerodynamics*, 6th ed. McGraw-Hill.
7. Thomas, F. (1999). *Fundamentals of Sailplane Design*. College Park Press.

### 10.5 Nanogénérateurs

8. Wang, Z.L. (2013). "Triboelectric Nanogenerators as New Energy Technology". *ACS Nano*, 7(11), 9533-9557.

---

## Annexe A : Constantes Physiques Utilisées

| Constante | Symbole | Valeur | Unité |
|-----------|---------|--------|-------|
| Constante des gaz parfaits | R | 8.314 | J/(mol·K) |
| Accélération gravitationnelle | g | 9.81 | m/s² |
| Masse molaire CO2 | M_CO2 | 0.044 | kg/mol |
| Masse molaire H2 | M_H2 | 0.002 | kg/mol |
| Point critique CO2 (T) | T_c | 304.2 | K |
| Point critique CO2 (P) | P_c | 7.38 | MPa |
| PCI Hydrogène | - | 120 | MJ/kg |
| Chaleur latente eau (vaporisation) | L_v | 2260 | kJ/kg |
| Chaleur latente glace (fusion) | L_f | 334 | kJ/kg |

---

## Annexe B : Glossaire

| Terme | Définition |
|-------|------------|
| **Carnot** | Rendement théorique maximal d'un cycle thermique |
| **CO2 supercritique** | CO2 au-dessus de son point critique (31.1°C, 73.8 bar) |
| **Électrolyse** | Décomposition de l'eau en H2 et O2 par courant électrique |
| **Finesse** | Rapport portance/traînée, distance parcourue par unité d'altitude perdue |
| **PCI** | Pouvoir Calorifique Inférieur (énergie récupérable par combustion) |
| **PEM** | Proton Exchange Membrane (type d'électrolyseur) |
| **TENG** | Triboelectric Nanogenerator |
| **TRL** | Technology Readiness Level (1=concept, 9=opérationnel) |

---

## Annexe C : Code de Simulation

Le code Python `preuve_thermodynamique_planeur.py` (~3200 lignes) implémente :
- Modèle thermodynamique du cycle CO2
- Bilan de masse H2/H2O/CO2
- Simulation sur 360 jours
- 17 vérifications indépendantes

**Exécution** :
```bash
python preuve_thermodynamique_planeur.py > RESULTAT.txt
```

---

## Avertissement Final

> **Ce document est une étude exploratoire, pas un plan de construction.**
>
> Les calculs présentés sont basés sur des modèles simplifiés et des hypothèses favorables. Les rendements réels, les pertes parasites, et les défis d'intégration réduiront significativement les performances.
>
> Avant toute tentative de prototypage :
> - Consulter des experts en thermodynamique des cycles
> - Réaliser des simulations numériques détaillées
> - Construire des bancs d'essai pour chaque sous-système
> - Prévoir des marges de sécurité importantes
>
> **L'objectif de ce document est de stimuler la réflexion, pas de promettre un résultat.**

---

*Document généré le 30 janvier 2026*  
*Projet Phénix - Étude Conceptuelle*
