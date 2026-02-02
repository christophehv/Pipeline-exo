#!/usr/bin/env python3
"""Application Python minimale pour le TP CI/CD"""

from flask import Flask
import logging
import sys

app = Flask(__name__)

# Configuration des logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

@app.route('/')
def hello():
    """Route par défaut"""
    logger.info("Request reçue sur la route /")
    return {"status": "ok", "message": "Application Python démarrée avec succès"}, 200

@app.route('/health')
def health():
    """Health check endpoint"""
    logger.info("Health check demandé")
    return {"status": "healthy"}, 200

@app.route('/version')
def version():
    """Version endpoint"""
    logger.info("Version demandée")
    return {"version": "1.0.0"}, 200

if __name__ == '__main__':
    logger.info("Démarrage de l'application Flask")
    app.run(host='0.0.0.0', port=5000, debug=False)
