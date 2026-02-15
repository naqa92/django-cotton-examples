# Django Components

Un projet Django avec auto-reload et Tailwind CSS intégré.

## 🚀 Démarrage rapide

### Prérequis

- Python 3.12+
- [Devbox](https://www.jetify.com/devbox/docs/installing_devbox/)
- Git

### Installation

1. **Installer les dépendances :**

   ```bash
   devbox shell  # Installe automatiquement daisyui (pnpm install)
   uv sync       # Installe les dépendances Python
   ```

2. **Effectuer les migrations :**
   ```bash
   uv run python manage.py migrate
   ```

### Lancement du serveur de développement

```bash
devbox run dev:all
```

Cette commande lance automatiquement :

- 🔄 **Livereload** - Rechargement automatique du navigateur
- 🌐 **Serveur Django** - http://127.0.0.1:8000
- 🎨 **Tailwind CSS** - Compilation en temps réel

Le projet sera accessible sur [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📁 Structure du projet

```
djangocomponents/
├── components/         # Application Django principale
├── templates/          # Templates HTML
│   ├── cotton/        # Composants Cotton
│   └── index.html     # Template principal
├── theme/             # Thème et assets
│   └── static/
│       └── css/
│           ├── input.css   # Source Tailwind CSS
│           └── style.css   # CSS compilé
└── venv/              # Environnement virtuel
```

## 🛠️ Technologies utilisées

- **Django 5.2.4** - Framework web Python
- **Django Cotton** - Système de composants pour Django
- **Tailwind CSS 4.1** - Framework CSS utility-first
- **DaisyUI 5.0** - Composants UI pour Tailwind CSS
- **Livereload** - Rechargement automatique du navigateur

## 🔧 Scripts disponibles

- `devbox run dev:all` - Lance tout le stack de développement
- `devbox run tw:watch` - Lance seulement la compilation Tailwind CSS
- `devbox run django` - Lance seulement le serveur Django
- `devbox run livereload` - Lance seulement le serveur Livereload

## 🐛 Dépannage

Si vous rencontrez des problèmes, vérifiez que :

- L'environnement virtuel est activé
- Toutes les dépendances sont installées
- Les ports 8000 et 35729 sont libres
- Les migrations ont été effectuées
