from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    blog_text = models.TextField()
    slug = models.SlugField()
    is_draft = models.BooleanField()

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
