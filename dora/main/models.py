from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxLengthValidator



class Good(models.Model):
    name = models.CharField('Имя', max_length=20,validators=[MaxLengthValidator(10)])
    anons = models.CharField('фамилия', max_length=250)
    date = models.DateTimeField('Дата публикации')
    slug = models.SlugField(unique=True, max_length=100, blank=True, null=False)



class VisitedPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} visited {self.page_name} at {self.timestamp}"
