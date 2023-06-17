from django.db import models

def upload_to(instance, filename):

    return f'media/{instance.id}/{filename}'

class Event(models.Model):

    titre = models.fields.CharField(max_length=60)
    flyer = models.ImageField(upload_to="", blank=True)
    description = models.fields.TextField()

    def __str__(self):

        return f'{self.titre}'
    
class Message(models.Model):

    nom = models.CharField(max_length=100)
    mail = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

            return f'{self.nom} - {self.date}'

class Photo(models.Model):
     
    image = models.ImageField(upload_to='', blank=False)
    artiste = models.fields.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f'{self.artiste} - {self.date}'

