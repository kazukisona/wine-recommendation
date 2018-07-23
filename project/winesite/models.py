from django.db import models

# Create your models here.
class Wine(models.Model):
    name = models.CharField(max_length=50, unique=True)
    wine_type = models.CharField(max_length=20)
    region = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.firstname + " " + self.lastname

class WineTable(models.Model):
    wine_id = models.TextField(blank=True, null=False, primary_key=True)
    name = models.TextField(blank=True, null=True)
    winery = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    province = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    varietal = models.TextField(blank=True, null=True)
    vintage = models.TextField(blank=True, null=True)
    style = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wine-table'
