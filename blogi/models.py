from django.db import models
from django.utils.translation import gettext_lazy as _


class Postaus(models.Model):
    otsikko = models.CharField(max_length=200)
    ingressi = models.TextField(blank=True)
    teksti = models.TextField()
    kuva = models.ImageField(upload_to="blogi/kuvat", null=True, blank=True)
    luotu = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("postaus")
        verbose_name_plural = _("postaukset")

    def __str__(self):
        return self.otsikko

    def luo_ingressi(self):
        if self.ingressi:
            return self.ingressi
        return self.teksti[:50] + "..."
