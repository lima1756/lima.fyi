from django.db import models
import uuid

class ResumeLog(models.Model):
    """
        This model describes a log of modifications of the resume
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    date_time_edited = models.DateTimeField(verbose_name='Date-time of modification',auto_now=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    resume = models.TextField()


    def __str__(self):
        """
            Returns the date of modification and the title of the modification
        """
        return str(self.date_time_edited) + " : " + self.title


    class Meta:
        ordering = ["-date_time_edited"]
