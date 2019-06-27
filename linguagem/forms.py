from django.forms import ModelForm
from .models import Linguagem


class LinguagemForm(ModelForm):
    class Meta:

        model = Linguagem
        ordering = ['linguagem_name']
        fields = ['linguagem_name', 'fabricante', 'rank' ]



