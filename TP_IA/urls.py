"""
URL configuration for TP_IA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TP_IA import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formmagasin/', views.form_magasin, name='form_magasin'),
    path('admin/', admin.site.urls),
    path('api/documents/', views.get_documents_by_collection, name='get_all_documents'),
    path('api/documents/create/', views.create_document, name='create_document'),
    path('api/documents/<str:document_id>/update/', views.update_document, name='update_document'),
    path('api/documents/<str:document_id>/delete/', views.delete_document, name='delete_document'),
]
