from django.db import models

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.CharField(max_length=255)
    thumbnail = models.ImageField()
    featured = models.BooleanField(default=False)
 
    def __str__(self):
        return self.title