from django.db import models


class Linguagem(models.Model):
    linguagem_name = models.CharField("Linguagem", max_length=30)
    fabricante = models.CharField("Fabricante", max_length=30, null= True, blank= True)
    rank = models.CharField("Rank",max_length=2, null=True, blank=True)


    def __str__(self):
        return self.linguagem_name + ' ' + self.fabricante  + ' ' + self.rank






