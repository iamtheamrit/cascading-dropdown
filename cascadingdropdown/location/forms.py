from django import forms
from django.urls import reverse_lazy

from .models import State, District, Village

class StateForm(forms.Form):
    state = forms.ModelChoiceField(queryset=State.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    district = forms.ModelChoiceField(queryset=District.objects.none(),widget=forms.Select(attrs={'class':'form-control'}))
    village = forms.ModelChoiceField(queryset=Village.objects.none(),widget=forms.Select(attrs={'class':'form-control'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].widget.attrs['data-url'] = reverse_lazy('location:district_list')
        self.fields['village'].widget.attrs['data-url'] = "/api/district/"
        
        try:
            state_id = int(self.data.get('state'))
            self.fields['district'].queryset = District.objects.filter(state=state_id)
        except (ValueError, TypeError):
            pass
        
        try:
            district_id = int(self.data.get('district'))
            self.fields['village'].queryset = Village.objects.filter(district=district_id)
        except (ValueError, TypeError):
            pass
    