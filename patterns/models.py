from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Pattern(models.Model):
    name = models.CharField(max_length = 64)
    description = models.TextField(default = '')
    added_by = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)
    category = models.TextField(default = '')
    
    def __str__(self):
        return self.name, self.category
    