from django import forms
from .models import Usuario

class cadastro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nome',
            'sobrenome',
            'username',
            'senha',
        ]


class filtrarreceita(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'alergia',
            'intolerancia',
            'comidadetestavel',
            'filters-date',
        ]