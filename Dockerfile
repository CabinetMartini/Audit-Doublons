# Dockerfile.api
# Utilise une image Python comme base
FROM python:3.14.3-slim

# Définir des variables d'environnement pour Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application dans le conteneur
COPY . .

# Exposer le port (par exemple, 8000)
EXPOSE 8023

# Lancer l'application
CMD ["uvicorn", "app.internal.main:app", "--host", "0.0.0.0", "--port", "8023", "--proxy-headers"]
