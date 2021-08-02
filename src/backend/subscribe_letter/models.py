from django.db import models


class Newsletter(models.Model):
    """[Model to store newsletter table details]

    Args:
        models ([type]): [django models]

    Returns:
        [str]: [firstname of user]
    """
    firstname = models.CharField(max_length=30)
    email = models.EmailField()
    agree = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.firstname