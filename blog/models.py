import uuid
from django.db import models


class Tag(models.Model):
    """
        This model describes a blog tag
    """
    name = models.CharField(max_length=30)


class Post(models.Model):
    """
        This model describes a blog post
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    date_time_created = models.DateTimeField(verbose_name='Creation Date-time', auto_now_add=True)
    date_time_modification = models.DateTimeField(verbose_name='Modification Date-time', auto_now=True)
    date_time_published = models.DateTimeField(verbose_name='Date-time of publication')
    title = models.CharField(max_length=100)
    content = models.TextField()
    claps = models.BigIntegerField(default=0,
                                   help_text="This is a representation of how much is "+\
                                              "liked the post, if you like it much you "+\
                                              "can give a lot of claps, if you don't you "+\
                                              "don't give any clap")
    tags = models.ManyToManyField(Tag)
    visible = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date_time_published", "-date_time_modification"]


class Comment(models.Model):
    """
        This model describes a blog post comment or answer to another comment
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    date_time_published = models.DateTimeField(verbose_name='Publication date-time', auto_now=True)
    content = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField(help_text='This is only for stadistics, it will not be shared')
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    answer_to = models.OneToOneField('Comment', on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date_time_published"]
