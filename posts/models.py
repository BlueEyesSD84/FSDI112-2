from django.db import models
from django.urls import reverse

class Post(models.Model): #the relationship between Post and Model is that of child and parent
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])

        
#  ----NOTES-----
#pthon3 mange.py makemigrations posts, generated migrations->0001_initial.py, created dependcies and operations, also created CreateModel which created table.  

# to run the migration,  python3 manage.py migrate,  creates DB tables.

#dunder method line 9 helps to create admin