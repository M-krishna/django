from django.db import models

# Create your models here.
class Todo(models.Model):
    complete = models.BooleanField(default=False)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Todo'