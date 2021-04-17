from django.db import models


class dna(models.Model):
    dna = models.CharField(max_length=255)

    def __str__(self):
        return self.dna

    class Meta:
        verbose_name_plural = 'DNAs'


class simiosXHumanos(models.Model):
    simios = models.PositiveIntegerField(default=0)
    humanos = models.PositiveIntegerField(default=0)
    ratio = models.DecimalField(max_digits=3, decimal_places=1, default=00.0)

    def __str__(self):
        return str(self.ratio)

    class Meta:
        verbose_name_plural = 'Simios x Humanos'

