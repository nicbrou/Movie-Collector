from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

SNACK = (
    ('P', 'Popcorn'),
    ('C', 'Chocolate'),
    ('S', 'Sour Candy'),
)

class Comment(models.Model):
    comment = models.CharField(max_length=2000)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('comments_detail', kwargs={'pk': self.id})

class Movie(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.CharField(max_length=2000)
    year = models.CharField(max_length=4)
    image = models.CharField(default=None, blank=True, null=True, max_length=2000)
    comments = models.ManyToManyField(Comment)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})

class Viewing(models.Model):
    date = models.DateField('Viewing Date')
    snack = models.CharField(max_length=1, choices=SNACK, default=SNACK[0][0])

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"I will watch '{self.movie}' on {self.date} and eat {self.get_snack_display()}."