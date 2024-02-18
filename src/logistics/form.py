from django import forms

from .models import Package


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['weight', 'dimensions', 'origin_address', 'destination_address', 'delivery_status', 'client', 'carrier']