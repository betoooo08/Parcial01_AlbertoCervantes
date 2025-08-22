from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model  = Flight
        fields = ['name', 'type', 'price']

    def clean_price(self):
        price = self.cleaned_data['price']
        if price is None or price <= 0:
            raise forms.ValidationError("El precio debe ser mayor que 0.")
        return price