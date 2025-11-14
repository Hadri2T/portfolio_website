from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    message = models.TextField()
    number = models.CharField(max_length=15)

    def __self__(self):
        return(self.name)
