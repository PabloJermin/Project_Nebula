from django.db import models

# Create your models here.
class Students(models.Model):
    email = models.EmailField(default="email@ymail.com")
    name = models.CharField(max_length=100)
    cohort = models.CharField(max_length=100, null=False)
    
    
    def __str__(self) -> str:
        return self.name
