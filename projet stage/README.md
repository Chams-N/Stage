
# Gestion du Système de Vaccination Antirabique

## Description

Cette application de gestion du système de vaccination antirabique a été développée pour faciliter la gestion des protocoles de vaccination, optimiser le suivi des patients, et automatiser le calcul des doses de sérum antirabique à administrer.  
Elle est destinée à améliorer l'efficacité du Service de Vaccination de l’Institut Pasteur de Tunis grâce à une digitalisation complète des processus.

## Fonctionnalités Principales

- **Enregistrement des informations des patients** : Collecte et gestion des données personnelles nécessaires.
- **Gestion des protocoles de vaccination** : Implémentation des protocoles spécifiques, suivi des dates de vaccination et des doses administrées.
- **Calcul automatique des doses de sérum** : Basé sur les caractéristiques des patients et des lésions identifiées.
- **Interface utilisateur intuitive** : Développée avec le framework Flet, elle garantit une expérience utilisateur fluide.
- **Suivi des vaccinations** : Historique détaillé des interventions pour chaque patient.
- **Gestion des données sécurisée** : Utilisation de MySQL pour stocker et gérer les informations critiques.

## Technologies Utilisées

- **Python** : Langage principal pour la logique métier.
- **MySQL** : Système de gestion des bases de données relationnelles.
- **Flet** : Framework utilisé pour construire l'interface graphique de l'application.

## Structure des Fichiers

- **`calender.py`** : Implémentation d’un calendrier interactif pour gérer les dates de vaccination.
- **`connector.py`** : Contient les fonctions pour interagir avec la base de données (insertion, mise à jour, suppression, récupération).
- **`interface.py`** : Définit l’interface utilisateur et les interactions principales.
- **`costom_check_box.py`** : Classe personnalisée pour les cases à cocher interactives, avec des animations et des styles configurables, intégrées à l'interface graphique pour une meilleure interaction utilisateur.

## Installation

### Prérequis
- Python 3.9 ou une version ultérieure
- MySQL installé localement ou accessible via un serveur distant
- Bibliothèques Python requises : `flet`, `mysql-connector-python`, `python-dateutil`, `babel`

### Étapes
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-repo.git
   cd votre-repo
   ```
2. Créez un environnement virtuel :
   ```bash
   python -m venv env
   source env/bin/activate # Pour Linux/MacOS
   env\Scripts\activate    # Pour Windows
   ```
3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
4. Configurez la base de données MySQL :
   - Créez une base de données nommée `python`.
   - Exécutez le script SQL pour créer les tables nécessaires.
5. Lancez l'application :
   ```bash
   python interface.py
   ```

## Utilisation

1. Accédez à l'interface utilisateur pour enregistrer les informations des patients.
2. Suivez les protocoles de vaccination guidés par l'application.
3. Générez et visualisez les calendriers de vaccination et les doses calculées automatiquement.

## Défis et Solutions Techniques

- **Interopérabilité des composants** : Une attention particulière a été portée pour garantir une communication fluide entre l'interface graphique et la base de données.
- **Gestion des doses et protocoles complexes** : Les calculs ont été optimisés pour prendre en compte toutes les variables cliniques.

## Contributions

Si vous souhaitez contribuer, veuillez ouvrir une *issue* ou soumettre une *pull request*.  

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.

## Acknowledgements

Ce projet a été réalisé dans le cadre de la digitalisation des services de l’Institut Pasteur de Tunis.
