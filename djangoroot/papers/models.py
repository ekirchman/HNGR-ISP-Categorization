from django.db import models

# Create your models here.

class Document(models.Model):
    language = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    f_path = models.CharField(max_length=200)

    def __str__(self):
        return self.f_path


class Doc_theme(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    theme_name = models.CharField(max_length=200)

    def __str__(self):
        return self.theme_name

