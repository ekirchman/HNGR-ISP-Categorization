from django.db import models

# TODO: In the "ai output" json that we generate, we should include the path
#       where we have the documents stored,
#       assuming we just locally store them in a directory on the server.
class Document(models.Model):
    f_path = models.FileField(upload_to='documents/')
    year = models.CharField(max_length=5, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    major = models.CharField(max_length=30, null=True, blank=True)
    author = models.CharField(max_length=30, null=True, blank=True)
    advisor = models.CharField(max_length=30, null=True, blank=True)
    themes = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.f_path}"
