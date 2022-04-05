from unicodedata import name
from django.core.management.base import BaseCommand

from location.models import State, District, Village

class Command(BaseCommand):
    help = 'Populate Location sample data'
    
    def handle(self, **kwargs):
        
        data = {
            'Punjab' : {
                "Gurdaspur" : [ "Behrampur", "Dinanagar" ],
                "Amritsar" : ["Majitha"]
            },
            'Uttar pradesh' : {
                "Gautam Buddha Nagar" : [ "Noida", "Vaishali" ]
            }
        }
        
        for state,district in data.items():
            state_obj = State.objects.get_or_create(name=state.upper())[0]
            for district,villages in district.items():
                district_obj = District.objects.get_or_create(name=district.upper(), state=state_obj)[0]
                for village in villages:
                    village_obj = Village.objects.get_or_create(name=village.upper(), district=district_obj)[0]
