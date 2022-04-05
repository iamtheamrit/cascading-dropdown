from django.db import models

# Create your models here.
from core.models import DateTimeStampedAbstractModel
from .mixins import UniqueNameMixin

class State(UniqueNameMixin,DateTimeStampedAbstractModel):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.name
    
class District(UniqueNameMixin,DateTimeStampedAbstractModel):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='districts')
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Village(UniqueNameMixin,DateTimeStampedAbstractModel):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='villages')
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    