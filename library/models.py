# -*- coding: utf-8 -*- 

from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
  title = models.CharField(max_length=256, verbose_name='Titre')
  description = models.TextField(verbose_name='Déscription', blank=True)
  def __unicode__(self):
    return self.title

class Author(models.Model):
  surname = models.CharField(max_length=256, verbose_name='Nom')
  givenames = models.CharField(max_length=256, verbose_name='Prénoms')
  def __unicode__(self):
    return self.givenames + ' ' + self.surname

class Book(models.Model):
  title = models.CharField(max_length=256, verbose_name='Titre')
  subtitle = models.CharField(max_length=256, blank=True, verbose_name='Sous-titre')
  description = models.TextField(verbose_name='Déscription', blank=True)
  isbn = models.CharField(max_length=24, blank=True, verbose_name='ISBN')
  oclc = models.CharField(max_length=24, blank=True, verbose_name='ICLC')
  lccn = models.CharField(max_length=24, blank=True, verbose_name='LCCN')
  olid = models.CharField(max_length=24, blank=True, verbose_name='OLID')
  language = models.CharField(max_length=3, choices= (
    ('MUL', 'Plusieurs/Bilingue'),
    ('fra', 'Français'),
    ('eng', 'Anglais'),
    ('esp', 'Espagnol'),
    ('AUT', 'Autre'),
  ))
  category = models.ForeignKey(Category, blank=True, null=True, verbose_name='Catégorie')
  author = models.ForeignKey(Author, blank=True, null=True, verbose_name='Auteur')
  def __unicode__(self):
    return self.title

class Borrower(models.Model):
  name = models.CharField(max_length=256, verbose_name='Nom')
  email = models.EmailField(max_length=256, blank=True, verbose_name='Courriel')
  phone = models.CharField(max_length=24, blank=True, verbose_name='Téléphone')
  notes = models.TextField(blank=True, verbose_name='Notes')
  def __unicode__(self):
    return self.name

class Loan(models.Model):
  book = models.ForeignKey(Book, verbose_name='Livre')
  borrower = models.ForeignKey(Borrower, verbose_name='Emprunteur')
  borrowed = models.DateField(verbose_name="Date de l'emprunt")
  due = models.DateField(verbose_name="Date prévue de retour")
  returned = models.DateField(verbose_name="Date actuel du retour", blank=True, null=True)
  def __unicode__(self):
    return str(self.book) + ' (' + str(self.borrowed) + ' - ' + str(self.returned) + ')'
  def is_late(self):
    return self.due <= datetime.date.today()
      