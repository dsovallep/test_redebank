from django.db import models

class Parameter(models.Model):
    
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)

    values = models.JSONField(null=True, default=dict)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name