import os

__author__ = 'Jeremy'

from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Choisissez un fichier',
        help_text='Format .txt et .csv accpetes'
    )



