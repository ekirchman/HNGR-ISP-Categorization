from django.db import models

# Create your models here.

class Document(models.Model):
    major = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    year = models.IntegerField()
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    advisor = models.CharField(max_length=200)
    f_path = models.FileField(upload_to='documents/')

    def __str__(self):
        return str(self.f_path)


class Doc_theme(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    theme_name = models.CharField(max_length=200)

    def __str__(self):
        return self.theme_name

