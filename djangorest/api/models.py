from django.db import models
from users.models import User
from django.db import models

# Create your models here.

class Template(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    file = models.FileField()
    is_published = models.BooleanField(blank=False, default=False)


    def __str__(self):
        return "{}".format(self.name)

