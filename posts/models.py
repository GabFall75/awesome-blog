from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    titolo = models.CharField(max_length=120)
    contenuto = models.TextField()
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("singolo", kwargs= {"id": self.id, "slug": self.slug})