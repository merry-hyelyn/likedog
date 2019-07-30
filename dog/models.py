from django.db import models
# Create your models here.

class Dog(models.Model):
    title = models.CharField(max_length=30, default='SOME STRING')
    image = models.ImageField(upload_to="images/", blank=True)
    dog_kind = models.CharField(max_length=20)
    dog_date = models.DateTimeField('lost date')
    body = models.TextField()
    
    def __str__(self):
        return self.title