from django.db import models
from django.db.models.fields import CharField, URLField, DateField, TextField
from django.db.models.fields.files import ImageField


# Create your models here.
class Book(models.Model):
    isbn = CharField(max_length=10, verbose_name="isbn")
    title = CharField(max_lenght=50, verbose_name="Title")
    year = DateField(verbose_name="Year Piblic")
    description = TextField(verbose_name="Description")
    image = ImageField(verbose_name="Description")
    url = URLField(blank=True, verbose_name="url")

    def __str__(self) -> str:
        return self.title

