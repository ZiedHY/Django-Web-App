# Create your views here.
from django.http import HttpResponse

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)
    

def view_article(request, id_article):
    """ 
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse(
        "Vous avez demandé l'article n° {0} !".format(id_article)    
    )

from datetime import datetime
from django.shortcuts import render # render processes the template and creates an objet HttpResponse 

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2

    # Returns nombre1, nombre2 and their sum
    return render(request, 'blog/addition.html', locals())

def home_blog(request,pseudo,sexe):
    return render(request, 'blog/accueil.html', locals())

def display_colors(request):
    return render(request, 'blog/colors.html', {'couleurs': ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']})

def squelette(request):
    return render(request, 'blog/squelette.html', locals())

    