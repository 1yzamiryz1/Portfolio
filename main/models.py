from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("created_date",)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    image = models.ImageField(upload_to='certificate/%Y/%m/%d/')
    original_image = models.ImageField(upload_to='certificate/original/%Y/%m/%d/')
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
