from django.db import models
from django.conf import settings

# Create your models here.


#Criando o modelo de Autor
class Author(models.Model):
  name = models.CharField(max_length=200,unique=True)

  def __str__(self) -> str:
    return self.name
  

#Criando o modelo de Categoria
class Category(models.Model):
  class Meta:
    verbose_name = "Category"
    verbose_name_plural = 'Categories'
  name = models.CharField(max_length=200,unique=True)

  def __str__(self) -> str:
    return self.name
  

#Criando o modelo de livros

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(Author, on_delete=models.CASCADE) # Relacionamento com Autor
  category = models.ManyToManyField(Category, blank=True) # Relacionamento com Categoria (muitos-para-muitos)
  # isbn = models.CharField(max_length=13,unique=True)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  description = models.TextField()
  publish_date = models.IntegerField(null=True,blank=True)
  publisher = models.CharField(max_length=255,blank=True,null=True)
  pages = models.IntegerField(null=True,blank=True)
  cover_url = models.URLField(max_length=200,null=True,blank=True)

  def __str__(self) -> str:
    return self.title



