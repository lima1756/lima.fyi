from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    """
        This model describes a Tag for projects
    """
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Project(models.Model):
    """
        This model describes a portfolio project
    """
    date_time_created = models.DateTimeField(verbose_name='Creation Date-time', auto_now_add=True)
    date_time_modification = models.DateTimeField(verbose_name='Modification Date-time', auto_now=True)
    name = models.CharField(max_length=100)
    content = models.TextField()
    summary = models.TextField()
    logo = models.ImageField(default=None, blank=True,upload_to='project_logos/')
    tags = models.ManyToManyField(Tag)
    visible = models.BooleanField(default=False)


    @property
    def url_name(self):
        """
            This property returns the name slugified for an URL
        """
        return slugify(self.name)


    class Meta:
        ordering = ["visible", "-date_time_created", "-date_time_modification"]
