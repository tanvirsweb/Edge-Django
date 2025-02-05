from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    summary = models.TextField(blank=True, null=True)
    bookstore_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # bookstore_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Replace 1 with the actual user ID


    def __str__(self):
        return self.title
