from django.db import models

class book_table(models.Model):
    Name = models.CharField(max_length=55)
    Email = models.CharField(max_length=55)
    Number = models.IntegerField(max_length=10)
    Date = models.DateField()
    Person = models.IntegerField(max_length=2)
