from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, FormMixin
from django.views.generic import TemplateView

# Create your views here.
from .mixins import DropdownMixin
from .models import State, District, Village
from .forms import StateForm

class IndexPageView(FormMixin,TemplateView):
    form_class = StateForm
    template_name = "location/index.html"
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, self.template_name, context={
                'form_submitted':True,
                'form':form
            })
        else:
            return self.form_invalid(form)



class DistrictListByState(DropdownMixin,ListView):
    model = District
    
    def get_queryset(self):
        state = self.request.GET.get('state')
        return super().get_queryset().filter(state=state)
    
class VillageListByDistrict(DropdownMixin,ListView):
    model = Village
    
    def get_queryset(self):
        district = self.request.GET.get('district')
        return super().get_queryset().filter(district=district)