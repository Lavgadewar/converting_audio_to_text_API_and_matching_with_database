from django.db import models

# Create your models here.  

class Audio(models.Model):

     # Defining the primary key 
     id = models.BigAutoField(primary_key=True)

      # Defining the audio file field
     audio_file = models.FileField()

     # Defining the string representation of the model
     def __str__(self) :
             # Returning the audio file name as the string representation
         return self.audio_file   
