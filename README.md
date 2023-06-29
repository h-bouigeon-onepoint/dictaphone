# DICTAPHONE SYNTHETIZER (POC Oméga)

Cette application permet de générer automatiquement un compte rendu de réunion dans la langue française ou anglais depuis un fichier audio (wav, m4a, wav, webm, mp3, mp4, mpga ou mpeg). Vous pouvez uploader un fichier audio ou vous enregistrer depuis l'application. Le compte rendu est ensuite exportable au format word ou power point. Et vous trouverez le transcript de l'audio dans le dossier "./data/transcript". L'application fonctionne pour le moment uniquement en local.

# Utilisation

Pour le moment, la façon la plus pratique d'utiliser cette application et de générer un compte rendu de réunion en uploadant un fichier audio au format mp3 de moins de 25MB. Puis d'enlever les éléments moins pertinents, voire corriger les quelques éléments approximatifs.

## Lancer l'application en local

### Créer l'environnement virtuel et installer les dépendances

Il est également nécessaire d'installer la librarie ffmpeg sur votre système, qui est disponible auprès de la plupart des gestionnaires de packages :

```Python
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg

# Using anaconda
conda install ffmpeg
```

Installez [anaconda](https://www.anaconda.com/download) si ce n'est pas déjà fait.

Puis, créez votre environnement virtuel :

```Python
conda create -n dictaphone python=3.9.6
conda activate dictaphone

python -m pip install -U pip
python -m pip install -r requirements.txt
```

### Crédentials

Enfin, créez les variables d'environnement suivantes avec les secrets :

- OPENAI_API_KEY (OpenAI)
- GPT_TURBO_API_KEY (Azure OpenAI)

### Pour lancer la flask app :

```Python
python app.py
```

### Pour lancer les tests unitaires :

```Python
python setup_test.py
```

## Spécifités techniques

- Langues disponible : Anglais ou français
- Temps de calcul : environ 5mn pour un fichier audio de 30mn au format mp3 ou m4a
- Taille maximal du fichier audio uploadé dépend du format du fichier, le fichier est compressé au format MP3 quoiqu'il arrive et si le fichier compressé fait moins de 25MB il sera traité correctement (le format mp3 est donc à privilégier car c'est un format compressé plus léger)
- Attention pour information l'export au format power point limite le nombre d'actions exportées à 5 et le nombre d'éléments discutés à 7 pour avoir un affichage cohérent et éviter de déborder. Vous pouvez toujours récupérer les éléments tronqués depuis le json ou depuis l'interface web directement
- Stockage des données : actuellement tout est stocké en local, il s'agit d'un POC
- Utilisation du mode "Refine" de Langchain :
  ![Include](./static/img/Refine%20Method%20to%20handle%20large%20text.png)

## Built With

- [Flaskapp](https://pypi.org/project/flaskapp/) - The web framework used
- [OpenAI](https://platform.openai.com/docs/api-reference) - The APIs used
- [Langchain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html) - Package to deal with large text

# Author

Feel free to contact me for feedback and further improvements.  
Made with heart : **Stéphan Adjarian** *s.adjarian@groupeonepoint.com*
