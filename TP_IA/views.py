from django.http import JsonResponse
from pymongo import MongoClient
from django.conf import settings
from django.shortcuts import render
import json
import os
from dotenv import load_dotenv
from bson import ObjectId

# Charger les variables d'environnement
load_dotenv()

# Configuration de la connexion MongoDB
client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
db = client[os.getenv('MONGODB_DB', 'tp')]
collection = db[os.getenv('MONGODB_COLLECTION', 'magasins')]

def index(request):
    """Vue pour afficher la page d'accueil"""
    return render(request, 'index.html')

def get_all_documents(request):
    """Récupère tous les documents de la collection"""
    try:
        documents = list(collection.find({}))
        # Convertir l'ObjectId en string pour la sérialisation JSON
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        return JsonResponse({'status': 'success', 'data': documents})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def create_document(request):
    """Crée un nouveau document dans la collection"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            result = collection.insert_one(data)
            return JsonResponse({'status': 'success', 'id': str(result.inserted_id)})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée'}, status=405)

def update_document(request, document_id):
    """Met à jour un document existant"""
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            result = collection.update_one(
                {'_id': document_id},
                {'$set': data}
            )
            return JsonResponse({'status': 'success', 'modified_count': result.modified_count})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée'}, status=405)

def delete_document(request, document_id):
    """Supprime un document"""
    if request.method == 'DELETE':
        try:
            print("document_id", document_id)
            result = collection.delete_one({'_id': ObjectId(document_id)})
            return JsonResponse({'status': 'success', 'deleted_count': result.deleted_count})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée'}, status=405) 