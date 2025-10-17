from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    Genre = models.CharField(max_length=225)
    release_date =models.FileField()


    def __str__(self):
      return self.title
class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.title} - {self.user.username}"