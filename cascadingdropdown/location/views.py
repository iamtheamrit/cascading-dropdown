from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.views.generic import TemplateView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.
from .mixins import DropdownMixin
from .models import State, District, Village
from .forms import StateForm
from .serializers import VillageModelSerializer

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
    
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def village_list_by_district(request,pk):
    """
    Uses Django REST Framework to provide a list of districts for a given state.
    """
    village = Village.objects.all().filter(district=pk)
    serializer = VillageModelSerializer(village, many=True)
    return Response(serializer.data)
    
class VillageListByDistrict(DropdownMixin,ListView):
    model = Village
    
    def get_queryset(self):
        district = self.request.GET.get('district')
        return super().get_queryset().filter(district=district)