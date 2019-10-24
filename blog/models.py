from django.db import models

# Create your models here.
from django.utils import timezone

class Articles(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True) #null=true i.e. this parameter is optional 
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de parution")
    #categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE) # See explanation below 

    class Meta: # adds info proper to the model - Optional 
        verbose_name = "article"
        ordering = ['date'] # defines the order when selecting data using this model
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.titre

# python manage.py makemigrations  -- allows to identify changes/updates in the model to be integrated to the database (think about git status)
# python manage.py migrate -- allows to integrate changes/updates in the database (think about git add or commit)
 
# To create a new document/row in the database : 
#   1 - python manage.py shell
#   2 - from blog.models import Article
#   3 - article = Article(titre="Bonjour", auteur="Maxime")
#   4 - article.contenu = "Les crêpes bretonnes sont trop bonnes !"
#   5 - article.auteur -- to get article's author 
#   6 - article.save() -- to save the article in the database 
# Creating a new document/row can be done in one single line: 
#   Article(auteur="Maxime", titre="La Bretagne", contenu="La Bretagne c'est trop bien").save()
# Article.objects.all() -- to see the content of Articles - Returns a QuerySet which is an iterable container 
# Examples of iterations on the QuerySet : 
#  for article in Article.objects.all():
#      print(article.titre)
#  for article in Article.objects.filter(auteur="Maxime"):
#      print(article.titre, "par", article.auteur)
#  for article in Article.objects.exclude(auteur="Maxime"):
#      print(article.titre, "par", article.auteur)
#  Article.objects.get(auteur="Mathieu").titre
#  Article.objects.get(auteur__startswith="M")
"""
Article.objects.get_or_create(auteur="Mathieu") # Think about create if not exists in SQL
>>> (<Article: Les crêpes>, False) # False to indicate that this document already exists 

Article.objects.get_or_create(auteur="Zozor", titre="Hi han")
>>> (<Article: Hi han>, True)
"""

class Categorie(models.Model):
    nom = models.CharField(max_length=40)

    def __str__(self):
        return self.nom
 
 # To link Categorie to Articles, we need to add category's name into Article as a foreign key 
 #     categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
 # It creates an ID in Categorie which will be shared between Categorie and Article 




