from django.db import models



class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    slug = models.SlugField(default="", null=False)
    email = models.EmailField(max_length=255, null=True, blank=True)

    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    
    
    
class Feedback(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        message = models.CharField(max_length=1000, blank=False)
        submitted_at = models.DateTimeField(auto_now_add=True)
        
        def _str_(self):
            return f"Feedback from {self.name} at {self.submitted_at}"
    
    
# Create your models here.
