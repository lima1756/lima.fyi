from django.db import models

# Create your models here.
class Comment(models.Model):
    """
        Model representing a comment in ardillas_salvajes web
    """
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=240)

class Contact(models.Model):
    """
        Model representing a contact us in ardillas_salvajes web
    """
    email = models.EmailField()
    name = models.CharField(max_length=50)
    content = models.TextField()
