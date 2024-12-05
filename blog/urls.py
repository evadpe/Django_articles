from django.urls import path
from . import views

urlpatterns = [
    # Liste des articles de blog
    path('', views.post_list, name='post_list'),
    
    # Détail d'un article de blog
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    # Créer un nouvel article de blog
    path('post/create/', views.create_post, name='create_post'),
    
    # Modifier un article de blog existant
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    
    # Ajouter un commentaire à un article de blog
    path('post/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    
    # Modifier un commentaire existant
    path('comment/<int:comment_pk>/edit/', views.edit_comment, name='edit_comment'),
    
    # Supprimer un article de blog
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    
    # Supprimer un commentaire
    path('comment/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]
