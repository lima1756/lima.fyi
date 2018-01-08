from django.db import models



class ContactData(models.Model):
    """
        This model describes the data of contact submitted by an user
    """
    date_time = models.DateTimeField(verbose_name='Date-time of submission', auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    answer = models.OneToOneField('ContactData', on_delete=models.CASCADE, default=None, blank=True, null=True)
