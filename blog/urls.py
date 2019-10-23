from django.urls import path
from . import views

urlpatterns = [
    path('accueil/<sexe>/<pseudo>', views.home_blog),
    path('article/<id_article>', views.view_article),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('couleurs', views.display_colors),
    path('squelette', views.squelette),

]

