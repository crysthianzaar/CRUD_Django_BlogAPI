from django.db import models
import uuid
from django.utils.text import slugify

STATUS_CHOICES = (
   ('draft', 'Draft'),
   ('published', 'Published'),
)

class Author(models.Model):
    name = models.CharField(max_length=250)
    picture = models.URLField()

    def __str__(self):
        return self.name
    
class Articles(models.Model):
    category = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=250)
    firstParagraph = models.TextField()
    body = models.TextField()
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default ='draft')
    slug = models.SlugField(auto_created= True)
    published_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def save(self, *args, **kwargs):
        self.category = slugify(self.category)
        super(Articles, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
