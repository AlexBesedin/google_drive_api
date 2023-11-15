from django.db import models


class GoogleDoc(models.Model):
    """Модельс"""
    name = models.CharField(max_length=255)
    document_id = models.CharField(max_length=255, unique=True)
    shared_with = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

