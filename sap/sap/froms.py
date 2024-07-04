from django import forms
from .models import Producto

class ProductoSearchForm(forms.Form):
    query = forms.CharField(label='Buscar producto')

    def search(self):
        query = self.cleaned_data.get('query')
        return Producto.objects.filter(nombre__icontains=query)
