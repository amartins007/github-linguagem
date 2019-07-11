from django.db import models


class Linguagem(models.Model):
    linguagem_name = models.CharField("Linguagem", max_length=30)
    forks = models.CharField("Forks", max_length=10, null= True, blank= True)
    watches = models.CharField("Watches", max_length=10, null=True, blank=True)


    def __str__(self):
        return self.linguagem_name + ' ' + self.forks  + ' ' + self.watches






