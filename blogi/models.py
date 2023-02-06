from django.db import models


class Postaus(models.Model):
    otsikko = models.CharField(max_length=200)
    teksti = models.TextField()
    luotu = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.otsikko
