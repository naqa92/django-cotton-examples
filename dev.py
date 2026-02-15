#!/usr/bin/env python
"""
Script de développement pour lancer Django avec auto-reload
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def main():
    print("🚀 Démarrage du serveur de développement avec auto-reload...")
    print("📁 Répertoire de travail:", os.getcwd())
    
    # Vérifier que nous sommes dans le bon répertoire
    if not Path("manage.py").exists():
        print("❌ Erreur: manage.py non trouvé. Assurez-vous d'être dans le répertoire du projet Django.")
        sys.exit(1)
    
    # Lancer le serveur Django avec livereload
    try:
        print("🌐 Lancement du serveur Django sur http://127.0.0.1:8000")
        print("🔄 Auto-reload activé - les modifications seront automatiquement rechargées")
        print("⏹️  Appuyez sur Ctrl+C pour arrêter le serveur")
        print("-" * 50)
        
        # Lancer le serveur Django
        subprocess.run([
            sys.executable, "manage.py", "runserver", 
            "--noreload",  # Désactiver le reload Django pour éviter les conflits
            "127.0.0.1:8000"
        ])
        
    except KeyboardInterrupt:
        print("\n👋 Arrêt du serveur de développement")
    except Exception as e:
        print(f"❌ Erreur lors du lancement du serveur: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 