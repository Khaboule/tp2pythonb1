# 🚀 Gestionnaire de Flottes Spatiales

## 📋 Description

Système de gestion de flottes spatiales développé en Python orienté objet. Ce projet permet de créer, gérer et sauvegarder des flottes composées de vaisseaux et d'équipages variés.

## ✨ Fonctionnalités

### Gestion des Flottes
- 🆕 Créer une nouvelle flotte
- 📂 Charger une flotte depuis un fichier JSON
- 🗑️ Supprimer une flotte
- ✏️ Renommer une flotte
- 💾 Sauvegarder une flotte en JSON

### Gestion des Vaisseaux
- ➕ Ajouter un vaisseau à la flotte (max 15)
- ➖ Supprimer un vaisseau
- 📊 Types de vaisseaux : Marchand, Destroyer, Cargo
- ✅ Vérifier la préparation d'un vaisseau

### Gestion des Équipages
- 👥 Ajouter des membres d'équipage (max 10 par vaisseau)
- 🗑️ Supprimer des membres
- 📋 Afficher les informations d'un équipage
- 🎯 Vérifier l'action d'un membre

### Types de Membres
- **Opérateur** : Possède un rôle (pilote, technicien, navigateur, médecin, ingénieur) et de l'expérience
- **Mentaliste** : Possède du mana (utilisable pour des actions spéciales)
- **Membre de base** : Membre standard sans compétences particulières

### Statistiques
- 📈 Nombre total de membres
- 📊 Répartition par rôle
- ⭐ Expérience moyenne des opérateurs

## 🏗️ Architecture

```
tp2pythonb1/
│
├── main.py           # Programme principal avec menu interactif
├── Fleet.py          # Classe Fleet (gestion des flottes)
├── Spaceship.py      # Classe Spaceship (gestion des vaisseaux)
├── Member.py         # Classe Member (membre de base)
├── Operator.py       # Classe Operator (hérite de Member)
├── Mentalist.py      # Classe Mentalist (hérite de Member)
└── *.json           # Fichiers de sauvegarde
```

## 🎮 Utilisation

### Lancer le programme

```bash
python main.py
```

### Menu Principal

```
--- Gestion des flottes ---
[A] Créer une nouvelle flotte
[B] Charger une flotte
[C] Supprimer une flotte

--- Gestion de la flotte active ---
[1] Renommer la flotte
[2] Ajouter un vaisseau à la flotte
[3] Supprimer un vaisseau de la flotte
[4] Ajouter un membre d'équipage
[5] Supprimer un membre d'équipage
[6] Afficher les informations d'un équipage
[7] Vérifier la préparation d'un vaisseau
[8] Vérifier l'action d'un membre d'équipage
[9] Sauvegarder la flotte
[10] Afficher les statistiques

[0] Quitter
```

### Exemple d'utilisation

1. **Créer une flotte**
   ```
   [A] → Entrer "Flotte Alpha"
   ```

2. **Ajouter un vaisseau**
   ```
   [2] → Nom: "Enterprise" / Type: "Destroyer"
   ```

3. **Ajouter un équipage**
   ```
   [4] → Type: Opérateur
   → Prénom: "Jean" / Nom: "Dupont"
   → Genre: "homme" / Âge: 35
   → Rôle: "pilote"
   ```

4. **Sauvegarder**
   ```
   [9] → Nom: "ma_flotte.json"
   ```

5. **Charger une flotte existante**
   ```
   [B] → Nom: "ma_flotte.json"
   ```

## 💾 Format de Sauvegarde

Les flottes sont sauvegardées en JSON avec la structure suivante :

```json
{
    "_Fleet__name": "Flotte Alpha",
    "_Fleet__spaceships": [
        {
            "_Spaceship__name": "Enterprise",
            "_Spaceship__ship_type": "Destroyer",
            "_Spaceship__condition": "Prêt",
            "_Spaceship__crew": [
                {
                    "_Member__first_name": "Jean",
                    "_Member__last_name": "Dupont",
                    "_Member__gender": "homme",
                    "_Member__age": 35,
                    "_Operator__role": "pilote",
                    "_Operator__experience": 0
                }
            ]
        }
    ]
}
```

## 🔧 Prérequis

- Python 3.10 ou supérieur
- Modules standards : `json`, `ast`

## 📦 Installation

```bash
# Cloner le repository
git clone https://github.com/votre-username/tp2pythonb1.git

# Aller dans le dossier
cd tp2pythonb1

# Lancer le programme
python main.py
```

## 🎯 Règles du Jeu

- **Flotte** : Maximum 15 vaisseaux
- **Vaisseau** : Maximum 10 membres d'équipage
- **Préparation** : Un vaisseau est prêt s'il a au moins 1 pilote et 1 technicien
- **Expérience** : Les opérateurs commencent avec 0 d'expérience
- **Mana** : Les mentalistes commencent avec 100 de mana

## 👨‍💻 Auteur

**Khalil SERDOUN**
- GitHub: [@votre-username](https://github.com/votre-username)

## 📝 Licence

Ce projet est un travail académique réalisé dans le cadre du cours 1PROG – Initiation à la programmation.

## 🙏 Remerciements

- École Hexagone
- Chris Chevalier (Professeur)

---

**Version** : 1.0.0  
**Date** : Décembre 2024  
**Statut** : ✅ Projet Terminé
