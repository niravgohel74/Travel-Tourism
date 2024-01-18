from django.db import models


# Create your models here.
class Master(models.Model):
    Username = models.CharField(max_length=20, null=True)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=20, null=True)

    def __str__(self) -> str:
        return self.Email