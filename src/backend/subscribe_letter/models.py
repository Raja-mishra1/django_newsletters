from django.db import models


class Newsletter(models.Model):
    firstname = models.CharField(max_length=30)
    email = models.EmailField()
    agree = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.firstname