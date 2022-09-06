from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True,
                              verbose_name='Group',
                              related_name='posts')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='post')
