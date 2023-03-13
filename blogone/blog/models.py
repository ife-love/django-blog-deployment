from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author =  models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-published_date']

    def publish(self):
        self.published_date = timezone.now()
        self.status = 'Published'
        self.save()

    def is_published(self):
        return self.published_date <= timezone.now()

    def get_absolute_url(self):
        return reverse('home')
        # return reverse('article-detail', args=(str(self.id)))

    def __str__(self):
        return f'{self.title}'
