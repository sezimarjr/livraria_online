from django.db import models
from django.conf import settings

# Create your models here.


#Criando o modelo de Autor
class Author(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self) -> str:
    return self.name
  

#Criando o modelo de Categoria
class Category(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self) -> str:
    return self.name
  

#Criando o modelo de livros

class Livro(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(Author, on_delete=models.CASCADE) # Relacionamento com Autor
  category = models.ManyToManyField(Category, blank=True) # Relacionamento com Categoria (muitos-para-muitos)
  price = models.DecimalField(max_length=6, decimal_places=2)
  description = models.TextField()
  publish_date = models.DateField()
  pages = models.IntegerField(null=True,blank=True)

  def __str__(self) -> str:
    return self.title



