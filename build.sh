#!/usr/bin/env bash
set -e  # Arrêter à la première erreur

echo "✅ INSTALLATION DES DÉPENDANCES"
pip install -r requirements.txt

echo "📦 COLLECTE DES FICHIERS STATIQUES"
python manage.py collectstatic --noinput

echo "🧩 MIGRATIONS BASE DE DONNÉES"
python manage.py migrate

echo "✅ BUILD TERMINÉ AVEC SUCCÈS"

