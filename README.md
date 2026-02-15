# Django Components

Un projet Django avec auto-reload et Tailwind CSS intégré.

## 🚀 Démarrage rapide

### Prérequis

- [Devbox](https://www.jetify.com/devbox/docs/installing_devbox/) - Gère Python, pnpm, Tailwind CSS
- Git

### Installation

1. **Installer les dépendances :**

   ```bash
   devbox shell         # Installe automatiquement tailwindcss + daisyui
   uv sync              # Crée .venv et installe les dépendances Python
   source .venv/bin/activate  # Active l'environnement virtuel
   ```

2. **Effectuer les migrations :**

   ```bash
   devbox run migrate # migrations des apps Django par défaut (Pas de modèles = pas besoin de makemigrations)
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
django-cotton-examples/
├── components/              # App Django principale
│   ├── views.py
│   ├── models.py
│   └── ...
├── djangocomponents/        # Configuration Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/               # Templates HTML
│   ├── cotton/             # Composants Cotton
│   │   ├── button.html
│   │   ├── card.html
│   │   └── select.html
│   └── index.html          # Template principal
├── theme/                   # Thème et assets
│   ├── static/
│   │   └── css/
│   │       ├── input.css   # Source Tailwind CSS
│   │       └── style.css   # CSS compilé
│   └── templates/
│       └── base.html
├── manage.py                # CLI Django
├── devbox.json              # Config Devbox
├── package.json             # Dépendances pnpm (daisyui)
├── pyproject.toml           # Dépendances Python (uv)
├── livereload.conf          # Config auto-reload
└── README.md
```

## 🛠️ Technologies utilisées

**Backend :**

- **Django 6.0** - Framework web Python
- **Django Cotton** - Système de composants pour Django
- **django-livereload-server** - Rechargement automatique

**Frontend :**

- **Tailwind CSS 4.1** - Framework CSS utility-first
- **DaisyUI 5.0** - Composants UI pour Tailwind CSS

**Outils de développement :**

- **Devbox** - Environnement de développement reproductible
- **UV** - Gestionnaire de dépendances Python ultra-rapide
- **pnpm** - Gestionnaire de paquets Node.js rapide

## 🔧 Scripts disponibles

- `devbox run dev:all` - Lance tout le stack de développement
- `devbox run tw:watch` - Lance seulement la compilation Tailwind CSS
- `devbox run django` - Lance seulement le serveur Django
- `devbox run livereload` - Lance seulement le serveur Livereload
- `devbox run migrate` - Effectue les migrations
- `devbox run makemigrations` - Crée les migrations

## 🐛 Dépannage

Si vous rencontrez des problèmes, vérifiez que :

- L'environnement virtuel est activé
- Toutes les dépendances sont installées
- Les ports 8000 et 35729 sont libres
- Les migrations ont été effectuées
