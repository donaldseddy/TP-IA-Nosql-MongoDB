from django.http import JsonResponse
from pymongo import MongoClient
from django.conf import settings
from django.shortcuts import render
import json
import os
from dotenv import load_dotenv
from bson import ObjectId
from MongoManager import MongoManager
from config.db_config import DB_NAME, MONGO_URI


mongoManager = MongoManager(MONGO_URI, DB_NAME)

def index(request):
    """Vue pour afficher la page d'accueil"""
    return render(request, 'index.html')

def form_magasin(request):
    """Vue pour afficher le formulaire de création de magasin"""
    return render(request, 'form_magasin.html')

def get_documents_by_collection(request):
    collection_name = request.GET.get('collection_name')
    if not collection_name:
        return JsonResponse({'status': 'error', 'message': 'Missing collection_name parameter'}, status=400)

    try:
        documents = mongoManager.get_documents_from_collection(collection_name)
        return JsonResponse({'status': 'success', 'data': documents})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)



def create_document(request):
    """Crée un nouveau document dans la collection"""
    if request.method == 'POST':
        try:
            document = json.loads(request.body)
            result = mongoManager.create_one_document(document)
            return JsonResponse({'status': 'success', 'id': str(result.inserted_id)})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée'}, status=405)

def update_document(request, document_id):
    """Met à jour un document existant"""
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            result = mongoManager.update_one_document(
                {'_id': document_id},
                {'$set': data}
            )
            return JsonResponse({'status': 'success', 'modified_count': result.modified_count})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée'}, status=405)

def delete_document(request, document_Id):
    """Supprime un document"""
    if request.method == 'DELETE':
        try:
            result = mongoManager.delete_one_document(document_Id)
            if result['deletedCount'] > 0:
                return JsonResponse({'status': 'success', 'message': 'Document supprimé'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Document non trouvé'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée'}, status=405) 