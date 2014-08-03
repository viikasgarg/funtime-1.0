from django.db import models

# Create your models here.
class Word(models.Model):
    name = models.CharField(max_length=200)
    dic_name = models.CharField(max_length=200)
    definition = models.TextField()

    def __unicode__(self):
        return self.name

# Create your models here.
class NewWord(models.Model):
    name = models.CharField(max_length=200)
    dic_name = models.CharField(max_length=200)
    definition = models.TextField()

    def __unicode__(self):
        return self.name