from django.db import models
import uuid


class ResumeLog(models.Model):
    """
        This model describes a log of modifications of the resume
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    date_time_edited = models.DateTimeField(verbose_name='Date-time of modification', auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    resume = models.TextField()


    def __str__(self):
        """
            Returns the date of modification and the title of the modification
        """
        return str(self.date_time_edited) + " : " + self.title


    class Meta:
        ordering = ["-date_time_edited"]

class Note(models.Model):
    """
        This model describes a note that the admin can create of whatever he wants
    """
    date_time = models.DateTimeField(verbose_name='Date-time of creation', auto_now_add=True)
    active = models.BooleanField(default=True)
    description = models.TextField()

    class Meta:
        ordering = ["-date_time"]
